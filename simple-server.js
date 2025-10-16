const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = 3001; // Use different port to avoid conflicts

app.use(cors());
app.use(express.json());
app.use(express.static('.'));

// Save data endpoint
app.post('/api/save-data', (req, res) => {
    try {
        const data = req.body;
        const filePath = path.join(__dirname, 'data.json');
        
        fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
        console.log('Data saved to file:', filePath);
        
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
        
        res.json({ success: true, message: 'Data saved successfully' });
    } catch (error) {
        console.error('Error saving data:', error);
        res.status(500).json({ success: false, error: error.message });
    }
});

// Get data endpoint
app.get('/api/get-data', (req, res) => {
    try {
        const filePath = path.join(__dirname, 'data.json');
        
        if (fs.existsSync(filePath)) {
            const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
            res.json(data);
        } else {
            res.json({ pnl_data: {}, priorities: [], last_updated: new Date().toISOString() });
        }
    } catch (error) {
        console.error('Error loading data:', error);
        res.status(500).json({ success: false, error: error.message });
    }
});

app.listen(PORT, () => {
    console.log(`🚀 Simple Data Server running on http://localhost:${PORT}`);
    console.log(`📊 Data will be saved to: ${path.join(__dirname, 'data.json')}`);
    console.log(`🌐 Open http://localhost:${PORT} to access the dashboard`);
});
