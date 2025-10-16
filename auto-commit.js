const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

function autoCommit() {
    try {
        // Check if there are changes to data.json
        const gitStatus = execSync('git status --porcelain data.json', { encoding: 'utf8' });
        
        if (gitStatus.trim()) {
            console.log('📊 Data changes detected, auto-committing...');
            
            // Add the data file
            execSync('git add data.json', { stdio: 'inherit' });
            
            // Commit with timestamp
            const timestamp = new Date().toISOString();
            execSync(`git commit -m "Auto-save: Update PNL data - ${timestamp}"`, { stdio: 'inherit' });
            
            console.log('✅ Data auto-committed to repository');
        } else {
            console.log('📊 No data changes to commit');
        }
    } catch (error) {
        console.log('⚠️ Auto-commit failed:', error.message);
    }
}

// Run auto-commit
autoCommit();
