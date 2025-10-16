# SteveSystem PNL Dashboard

A comprehensive Profit & Loss tracking dashboard with file-based storage and cloud sync capabilities.

## 🚀 Features

- **Day-specific Priorities** - Each day has its own priority list
- **PNL Tracking** - Daily profit/loss monitoring
- **Individual Trades** - Detailed trade logging
- **Daily Journal** - Morning intentions, evening reflections, focus areas
- **File-based Storage** - Data saved to actual files (not just browser storage)
- **Cloud Sync** - Automatic backup to GitHub
- **Cross-device Access** - Access your data from any computer

## 📁 Data Storage

Your data is now saved to actual files in the repository:

- **`data/pnl_data.json`** - All your PNL data, priorities, trades, and journal entries
- **`config.json`** - Configuration settings including GitHub sync preferences
- **Git History** - Every change is automatically committed and can be synced to GitHub

## 🛠️ Setup

### Quick Start

1. **Run the setup script:**
   ```bash
   ./setup.sh
   ```

2. **Start the server:**
   ```bash
   npm start
   ```

3. **Open your browser:**
   ```
   http://localhost:3000
   ```

### Manual Setup

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start the server:**
   ```bash
   npm start
   ```

3. **Open in browser:**
   ```
   http://localhost:3000
   ```

## ☁️ Cloud Sync (Optional)

To enable automatic backup to GitHub:

1. **Create a GitHub repository** for your PNL data
2. **Run the GitHub setup:**
   ```bash
   node scripts/setup-github.js
   ```
3. **Follow the prompts** to connect your repository

### Manual GitHub Setup

1. **Initialize git repository:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: SteveSystem PNL Dashboard"
   ```

2. **Add your GitHub repository:**
   ```bash
   git remote add origin https://github.com/yourusername/pnl-data.git
   git push -u origin main
   ```

3. **Update config.json:**
   ```json
   {
     "githubRepo": "https://github.com/yourusername/pnl-data.git",
     "autoCommit": true,
     "lastSync": "2024-01-01T00:00:00.000Z"
   }
   ```

## 🔄 Data Persistence

### What Gets Saved

- ✅ **Day-specific Priorities** - Each day's priority list
- ✅ **PNL Data** - Daily profit/loss amounts
- ✅ **Individual Trades** - Detailed trade information
- ✅ **Daily Journal** - Morning intentions, evening reflections, focus areas
- ✅ **Patterns & Improvements** - What you learned and what could be better
- ✅ **Win Rate & Stats** - Trading performance metrics

### Where It's Saved

- **Local Files**: `data/pnl_data.json`
- **Git History**: Every change is automatically committed
- **GitHub** (if configured): Automatic backup to cloud
- **Cross-device**: Pull changes on any computer

## 🚀 Usage

### Daily Workflow

1. **Morning**: Set your priorities and intentions
2. **During Day**: Log trades and update PNL
3. **Evening**: Reflect on the day and note improvements
4. **Automatic**: Everything saves to files and syncs to GitHub

### Adding Data

- **Priorities**: Click "Manage" or "Add" in the Top Priorities section
- **PNL**: Click on any day in the calendar to add/edit data
- **Trades**: Use the individual trades section in the daily modal
- **Journal**: Fill in morning intentions, evening reflections, etc.

### Syncing Data

- **Automatic**: Data saves every 30 seconds
- **Manual**: Use the sync buttons in the interface
- **GitHub**: Automatic commits and pushes (if configured)

## 🔧 Configuration

Edit `config.json` to customize:

```json
{
  "githubRepo": "https://github.com/yourusername/pnl-data.git",
  "autoCommit": true,
  "lastSync": "2024-01-01T00:00:00.000Z"
}
```

## 📊 API Endpoints

The server provides REST API endpoints:

- `GET /api/pnl-data` - Get all PNL data
- `POST /api/pnl-data` - Save all PNL data
- `GET /api/pnl-data/:year/:month/:day` - Get specific day data
- `POST /api/pnl-data/:year/:month/:day` - Save specific day data
- `POST /api/sync-github` - Manual GitHub sync
- `POST /api/pull-github` - Pull from GitHub
- `GET /api/health` - Health check

## 🛡️ Data Safety

- **Local Backup**: Data is saved to files in the repository
- **Git History**: Every change is tracked in git
- **Cloud Backup**: Automatic sync to GitHub (if configured)
- **No Data Loss**: Multiple layers of data protection

## 🔍 Troubleshooting

### Server Won't Start
- Check if port 3000 is available
- Run `npm install` to ensure dependencies are installed
- Check Node.js version (requires Node.js 14+)

### Data Not Saving
- Check if the server is running
- Look for errors in the browser console
- Verify the `data` directory exists and is writable

### GitHub Sync Issues
- Verify your GitHub repository URL is correct
- Check if you have push access to the repository
- Ensure git is properly configured with your credentials

## 📝 License

MIT License - Feel free to use and modify as needed.

## 🤝 Contributing

This is a personal project, but suggestions and improvements are welcome!

---

**Happy Trading! 📈**