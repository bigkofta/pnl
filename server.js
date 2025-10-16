const express = require('express');
const cors = require('cors');
const fs = require('fs-extra');
const path = require('path');
const simpleGit = require('simple-git');
const cron = require('node-cron');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('.'));

// Data storage paths
const DATA_DIR = path.join(__dirname, 'data');
const PNL_FILE = path.join(DATA_DIR, 'pnl_data.json');
const CONFIG_FILE = path.join(__dirname, 'config.json');

// Ensure data directory exists
fs.ensureDirSync(DATA_DIR);

// Initialize git repository if it doesn't exist
const git = simpleGit(__dirname);

// Load configuration
let config = {};
if (fs.existsSync(CONFIG_FILE)) {
    config = fs.readJsonSync(CONFIG_FILE);
}

// Auto-save to files every 30 seconds
cron.schedule('*/30 * * * * *', () => {
    console.log('Auto-syncing data to files...');
    // This will be handled by the sync endpoint
});

// API Routes

// Get all PNL data
app.get('/api/pnl-data', async (req, res) => {
    try {
        if (fs.existsSync(PNL_FILE)) {
            const data = await fs.readJson(PNL_FILE);
            res.json(data);
        } else {
            res.json({});
        }
    } catch (error) {
        console.error('Error reading PNL data:', error);
        res.status(500).json({ error: 'Failed to read PNL data' });
    }
});

// Save PNL data
app.post('/api/pnl-data', async (req, res) => {
    try {
        const data = req.body;
        
        // Save to file
        await fs.writeJson(PNL_FILE, data, { spaces: 2 });
        
        // Auto-commit to git if enabled
        if (config.autoCommit === true) {
            try {
                await git.add('.');
                await git.commit(`Auto-save PNL data: ${new Date().toISOString()}`);
            } catch (gitError) {
                console.warn('Git auto-commit failed (this is normal if git is not configured):', gitError.message);
            }
        }
        
        res.json({ success: true, message: 'Data saved successfully' });
    } catch (error) {
        console.error('Error saving PNL data:', error);
        res.status(500).json({ error: 'Failed to save PNL data' });
    }
});

// Get specific day data
app.get('/api/pnl-data/:year/:month/:day', async (req, res) => {
    try {
        const { year, month, day } = req.params;
        const key = `${year}-${month}-${day}`;
        
        if (fs.existsSync(PNL_FILE)) {
            const data = await fs.readJson(PNL_FILE);
            res.json(data[key] || {});
        } else {
            res.json({});
        }
    } catch (error) {
        console.error('Error reading day data:', error);
        res.status(500).json({ error: 'Failed to read day data' });
    }
});

// Save specific day data
app.post('/api/pnl-data/:year/:month/:day', async (req, res) => {
    try {
        const { year, month, day } = req.params;
        const key = `${year}-${month}-${day}`;
        const dayData = req.body;
        
        // Load existing data
        let data = {};
        if (fs.existsSync(PNL_FILE)) {
            data = await fs.readJson(PNL_FILE);
        }
        
        // Update specific day
        data[key] = dayData;
        
        // Save back to file
        await fs.writeJson(PNL_FILE, data, { spaces: 2 });
        
        // Auto-commit to git if enabled
        if (config.autoCommit === true) {
            try {
                await git.add('.');
                await git.commit(`Update PNL data for ${key}: ${new Date().toISOString()}`);
            } catch (gitError) {
                console.warn('Git auto-commit failed (this is normal if git is not configured):', gitError.message);
            }
        }
        
        res.json({ success: true, message: 'Day data saved successfully' });
    } catch (error) {
        console.error('Error saving day data:', error);
        res.status(500).json({ error: 'Failed to save day data' });
    }
});

// Sync to GitHub
app.post('/api/sync-github', async (req, res) => {
    try {
        if (!config.githubRepo) {
            return res.status(400).json({ error: 'GitHub repository not configured' });
        }
        
        // Add all changes
        await git.add('.');
        
        // Commit changes
        await git.commit(`Manual sync: ${new Date().toISOString()}`);
        
        // Push to GitHub
        await git.push('origin', 'main');
        
        res.json({ success: true, message: 'Successfully synced to GitHub' });
    } catch (error) {
        console.error('Error syncing to GitHub:', error);
        res.status(500).json({ error: 'Failed to sync to GitHub' });
    }
});

// Pull from GitHub
app.post('/api/pull-github', async (req, res) => {
    try {
        if (!config.githubRepo) {
            return res.status(400).json({ error: 'GitHub repository not configured' });
        }
        
        // Pull latest changes
        await git.pull('origin', 'main');
        
        res.json({ success: true, message: 'Successfully pulled from GitHub' });
    } catch (error) {
        console.error('Error pulling from GitHub:', error);
        res.status(500).json({ error: 'Failed to pull from GitHub' });
    }
});

// Get configuration
app.get('/api/config', (req, res) => {
    res.json(config);
});

// Update configuration
app.post('/api/config', async (req, res) => {
    try {
        config = { ...config, ...req.body };
        await fs.writeJson(CONFIG_FILE, config, { spaces: 2 });
        res.json({ success: true, message: 'Configuration updated' });
    } catch (error) {
        console.error('Error updating config:', error);
        res.status(500).json({ error: 'Failed to update configuration' });
    }
});

// Health check
app.get('/api/health', (req, res) => {
    res.json({ 
        status: 'healthy', 
        timestamp: new Date().toISOString(),
        dataFile: fs.existsSync(PNL_FILE),
        configFile: fs.existsSync(CONFIG_FILE)
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`🚀 SteveSystem PNL Server running on http://localhost:${PORT}`);
    console.log(`📊 Data will be saved to: ${PNL_FILE}`);
    console.log(`⚙️  Configuration: ${CONFIG_FILE}`);
    console.log(`🌐 Open http://localhost:${PORT} to access the dashboard`);
});

module.exports = app;
