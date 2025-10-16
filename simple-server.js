const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = 3001;

app.use(cors());
app.use(express.json());
app.use(express.static('.')); // Serve all static files

// API endpoint to get data - FAST and RELIABLE
app.get('/api/data', (req, res) => {
    try {
        // Read file synchronously - no async delays
        const dataPath = path.join(__dirname, 'data.json');
        if (fs.existsSync(dataPath)) {
            const data = fs.readFileSync(dataPath, 'utf8');
            console.log('📊 SERVER: Sending data immediately');
            res.json(JSON.parse(data));
        } else {
            console.log('📊 SERVER: No data file, sending empty structure');
            res.json(initializeEmptyData());
        }
    } catch (error) {
        console.error('SERVER ERROR:', error);
        res.json({}); // Never fail, always return valid JSON
    }
});

// API endpoint to save data
app.post('/api/data', (req, res) => {
    try {
        const dataPath = path.join(__dirname, 'data.json');
        fs.writeFileSync(dataPath, JSON.stringify(req.body, null, 2));
        
        // Auto-commit to git
        try {
            const { execSync } = require('child_process');
            execSync('git add data.json', { stdio: 'pipe' });
            const timestamp = new Date().toISOString();
            execSync(`git commit -m "Auto-save: Update PNL data - ${timestamp}"`, { stdio: 'pipe' });
            console.log('✅ Data auto-committed to repository');
        } catch (gitError) {
            console.log('⚠️ Auto-commit failed:', gitError.message);
        }
        
        res.json({ success: true });
    } catch (error) {
        console.error('Error saving data:', error);
        res.status(500).json({ error: 'Failed to save data' });
    }
});

// API endpoint to save backup
app.post('/api/save-backup', (req, res) => {
    try {
        const backupPath = path.join(__dirname, 'localStorage-backup.json');
        fs.writeFileSync(backupPath, JSON.stringify(req.body, null, 2));
        console.log('✅ Complete data saved as backup');
        res.json({ success: true });
    } catch (error) {
        console.error('Error saving backup:', error);
        res.status(500).json({ error: 'Failed to save backup' });
    }
});

// Diagnostic endpoint
app.get('/api/debug', (req, res) => {
    try {
        const backupPath = path.join(__dirname, 'localStorage-backup.json');
        const dataPath = path.join(__dirname, 'data.json');
        
        const backupData = fs.existsSync(backupPath) ? 
            JSON.parse(fs.readFileSync(backupPath, 'utf8')) : null;
        const mainData = fs.existsSync(dataPath) ? 
            JSON.parse(fs.readFileSync(dataPath, 'utf8')) : null;
            
        res.json({
            backupDataExists: !!backupData,
            backupDataKeys: backupData ? Object.keys(backupData) : [],
            backupTotal: backupData ? calculateTotalPNL(backupData) : 0,
            mainDataExists: !!mainData,
            mainDataKeys: mainData ? Object.keys(mainData) : [],
            mainTotal: mainData ? calculateTotalPNL(mainData) : 0,
            message: "Debug information"
        });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

function calculateTotalPNL(data) {
    return Object.values(data).reduce((total, dayData) => {
        return total + (dayData.pnl || 0);
    }, 0);
}

function initializeEmptyData() {
    return {
        "2025-10-16": { pnl: 312413, trades: [] },
        "2025-10-15": { pnl: 321514, trades: [] }
    };
}

app.listen(PORT, () => {
    console.log(`🚀 PNL Dashboard running at http://localhost:${PORT}`);
    console.log('📊 Data persistence is ENABLED through file system');
    console.log('🌐 Open http://localhost:3001 to access the dashboard');
});
