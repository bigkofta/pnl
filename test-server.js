const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = 3002; // Different port for stress testing

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
            console.log('📊 STRESS TEST SERVER: Sending data immediately');
            res.json(JSON.parse(data));
        } else {
            console.log('📊 STRESS TEST SERVER: No data file, sending empty structure');
            res.json({});
        }
    } catch (error) {
        console.error('STRESS TEST SERVER ERROR:', error);
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
            execSync(`git commit -m "Stress Test: Update PNL data - ${timestamp}"`, { stdio: 'pipe' });
            console.log('✅ STRESS TEST: Data auto-committed to repository');
        } catch (gitError) {
            console.log('⚠️ STRESS TEST: Auto-commit failed:', gitError.message);
        }
        
        res.json({ success: true });
    } catch (error) {
        console.error('STRESS TEST SERVER ERROR:', error);
        res.status(500).json({ error: 'Failed to save data' });
    }
});

// Diagnostic endpoint
app.get('/api/debug', (req, res) => {
    try {
        const dataPath = path.join(__dirname, 'data.json');
        
        const data = fs.existsSync(dataPath) ? 
            JSON.parse(fs.readFileSync(dataPath, 'utf8')) : null;
            
        res.json({
            dataExists: !!data,
            dataKeys: data ? Object.keys(data) : [],
            totalPNL: data ? Object.values(data).reduce((sum, day) => sum + (day.pnl || 0), 0) : 0,
            totalDays: data ? Object.keys(data).length : 0,
            message: "Stress Test Server - Debug information"
        });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.listen(PORT, () => {
    console.log(`🧪 STRESS TEST SERVER running at http://localhost:${PORT}`);
    console.log('📊 Testing data persistence and cross-environment functionality');
    console.log('🌐 Open http://localhost:3002 to test the dashboard');
});
