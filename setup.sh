#!/bin/bash

echo "🚀 Setting up SteveSystem PNL with File Storage & Cloud Sync..."
echo ""

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js first:"
    echo "   Visit: https://nodejs.org/"
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed. Please install npm first."
    exit 1
fi

echo "✅ Node.js and npm are installed"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
npm install

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "✅ Dependencies installed successfully"
echo ""

# Create data directory
echo "📁 Creating data directory..."
mkdir -p data

# Create initial config
echo "⚙️  Creating initial configuration..."
cat > config.json << EOF
{
  "githubRepo": "",
  "autoCommit": true,
  "lastSync": null
}
EOF

echo "✅ Initial configuration created"
echo ""

# Make setup script executable
chmod +x scripts/setup-github.js

echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Start the server: npm start"
echo "2. Open http://localhost:3000 in your browser"
echo "3. (Optional) Set up GitHub sync: node scripts/setup-github.js"
echo ""
echo "Your PNL data will now be saved to files in the 'data' directory"
echo "and can be synced to GitHub for cloud backup!"
