#!/usr/bin/env node

const fs = require('fs-extra');
const path = require('path');
const simpleGit = require('simple-git');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

async function setupGitHub() {
    console.log('🚀 Setting up GitHub sync for SteveSystem PNL...\n');
    
    const git = simpleGit(process.cwd());
    
    try {
        // Check if already a git repository
        const isRepo = await git.checkIsRepo();
        
        if (!isRepo) {
            console.log('📁 Initializing git repository...');
            await git.init();
        }
        
        // Get GitHub repository URL
        const repoUrl = await new Promise((resolve) => {
            rl.question('Enter your GitHub repository URL (e.g., https://github.com/username/pnl-data.git): ', resolve);
        });
        
        if (!repoUrl) {
            console.log('❌ No repository URL provided. Exiting.');
            rl.close();
            return;
        }
        
        // Add remote origin
        try {
            await git.addRemote('origin', repoUrl);
            console.log('✅ Added remote origin:', repoUrl);
        } catch (error) {
            console.log('ℹ️  Remote origin already exists or error adding:', error.message);
        }
        
        // Create .gitignore
        const gitignoreContent = `# Dependencies
node_modules/
npm-debug.log*

# Data files (optional - remove if you want to track data)
# data/

# OS files
.DS_Store
Thumbs.db

# IDE files
.vscode/
.idea/

# Logs
*.log
`;
        
        await fs.writeFile('.gitignore', gitignoreContent);
        console.log('✅ Created .gitignore file');
        
        // Create initial commit
        await git.add('.');
        await git.commit('Initial commit: SteveSystem PNL Dashboard');
        
        // Push to GitHub
        console.log('📤 Pushing to GitHub...');
        await git.push('origin', 'main');
        
        // Update configuration
        const config = {
            githubRepo: repoUrl,
            autoCommit: true,
            lastSync: new Date().toISOString()
        };
        
        await fs.writeJson('config.json', config, { spaces: 2 });
        console.log('✅ Updated configuration');
        
        console.log('\n🎉 GitHub sync setup complete!');
        console.log('📊 Your PNL data will now be automatically saved to files and synced to GitHub');
        console.log('🌐 Repository:', repoUrl);
        
    } catch (error) {
        console.error('❌ Error setting up GitHub sync:', error.message);
    } finally {
        rl.close();
    }
}

// Run setup
setupGitHub();
