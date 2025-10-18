#!/bin/bash

# AIUnic Website - Automated GitHub Setup Script
# This script automates the process of pushing to GitHub

echo "🚀 AIUnic Website - GitHub Setup Script"
echo "========================================"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Error: Git is not installed. Please install Git first."
    exit 1
fi

# Get repository URL from user
echo "📝 Enter your GitHub repository URL:"
echo "   Example: https://github.com/yourusername/aiunic-website.git"
read -p "URL: " REPO_URL

if [ -z "$REPO_URL" ]; then
    echo "❌ Error: Repository URL cannot be empty"
    exit 1
fi

# Confirm before proceeding
echo ""
echo "📋 Configuration:"
echo "   Repository: $REPO_URL"
echo ""
read -p "Continue? (y/n): " CONFIRM

if [ "$CONFIRM" != "y" ] && [ "$CONFIRM" != "Y" ]; then
    echo "❌ Setup cancelled"
    exit 0
fi

echo ""
echo "⚙️  Setting up Git repository..."

# Initialize git if not already initialized
if [ ! -d ".git" ]; then
    git init
    echo "✓ Git initialized"
else
    echo "✓ Git already initialized"
fi

# Add all files
git add .
echo "✓ Files staged"

# Create initial commit
git commit -m "Initial commit - AIUnic website"
echo "✓ Initial commit created"

# Add remote origin
git remote add origin "$REPO_URL" 2>/dev/null || git remote set-url origin "$REPO_URL"
echo "✓ Remote origin configured"

# Create and switch to main branch
git branch -M main
echo "✓ Main branch configured"

# Push to GitHub
echo ""
echo "📤 Pushing to GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ SUCCESS! Repository pushed to GitHub"
    echo ""
    echo "📌 Next Steps:"
    echo "   1. Go to your repository on GitHub"
    echo "   2. Settings → Pages"
    echo "   3. Enable GitHub Pages (source: gh-pages branch)"
    echo "   4. Your site will be live in 2-3 minutes"
    echo ""
    echo "🌐 Your website will be available at:"
    echo "   https://yourusername.github.io/repository-name/"
    echo ""
else
    echo ""
    echo "❌ Error pushing to GitHub"
    echo "   Please check:"
    echo "   - Repository URL is correct"
    echo "   - You have push access"
    echo "   - Your Git credentials are configured"
    echo ""
    echo "   Try manually: git push -u origin main"
fi
