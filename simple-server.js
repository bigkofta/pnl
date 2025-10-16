const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = 3001;

app.use(cors());
app.use(express.json());
app.use(express.static('.')); // Serve all static files

// API endpoint to get data
app.get('/api/data', (req, res) => {
    try {
        const dataPath = path.join(__dirname, 'data.json');
        if (fs.existsSync(dataPath)) {
            const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
            res.json(data);
        } else {
            res.json(initializeEmptyData());
        }
    } catch (error) {
        console.error('Error loading data:', error);
        res.status(500).json({ error: 'Failed to load data' });
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
