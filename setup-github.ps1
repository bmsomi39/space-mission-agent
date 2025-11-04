# GitHub Repository Setup Script
# Run this script after Git is installed

Write-Host "🚀 Setting up GitHub repository..." -ForegroundColor Green

# Check if Git is available
try {
    $gitVersion = git --version
    Write-Host "✅ Git found: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Git from: https://git-scm.com/download/win" -ForegroundColor Yellow
    Write-Host "Or install GitHub Desktop from: https://desktop.github.com/" -ForegroundColor Yellow
    exit 1
}

# Initialize git repository if not already initialized
if (-not (Test-Path .git)) {
    Write-Host "📦 Initializing git repository..." -ForegroundColor Cyan
    git init
    Write-Host "✅ Repository initialized" -ForegroundColor Green
} else {
    Write-Host "✅ Git repository already initialized" -ForegroundColor Green
}

# Add all files
Write-Host "📝 Adding all files..." -ForegroundColor Cyan
git add .
Write-Host "✅ Files added" -ForegroundColor Green

# Check if there are changes to commit
$status = git status --porcelain
if ($status) {
    Write-Host "💾 Creating initial commit..." -ForegroundColor Cyan
    git commit -m "Initial commit - Space Mission Agent"
    Write-Host "✅ Initial commit created" -ForegroundColor Green
} else {
    Write-Host "ℹ️  No changes to commit" -ForegroundColor Yellow
}

# Check if remote already exists
$remote = git remote get-url origin 2>$null
if ($remote) {
    Write-Host "✅ Remote already configured: $remote" -ForegroundColor Green
    Write-Host "📤 Pushing to GitHub..." -ForegroundColor Cyan
    git branch -M main
    git push -u origin main
    Write-Host "✅ Successfully pushed to GitHub!" -ForegroundColor Green
    Write-Host "🔗 Repository URL: $remote" -ForegroundColor Cyan
} else {
    Write-Host "⚠️  No remote repository configured" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "To add a remote repository, run:" -ForegroundColor Cyan
    Write-Host "  git remote add origin https://github.com/YOUR_USERNAME/space-mission-agent.git" -ForegroundColor White
    Write-Host "  git branch -M main" -ForegroundColor White
    Write-Host "  git push -u origin main" -ForegroundColor White
    Write-Host ""
    Write-Host "Or create a repository on GitHub first:" -ForegroundColor Cyan
    Write-Host "  1. Go to https://github.com/new" -ForegroundColor White
    Write-Host "  2. Repository name: space-mission-agent" -ForegroundColor White
    Write-Host "  3. Make it Public (recommended for competitions)" -ForegroundColor White
    Write-Host "  4. Don't initialize with README (we already have one)" -ForegroundColor White
    Write-Host "  5. Copy the repository URL and run the commands above" -ForegroundColor White
}

Write-Host ""
Write-Host "🎉 Setup complete!" -ForegroundColor Green

