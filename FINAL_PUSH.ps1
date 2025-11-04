# Final GitHub Push Script
# Run this after creating your GitHub repository

param(
    [Parameter(Mandatory=$true)]
    [string]$GitHubUsername
)

$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

Write-Host "🚀 Final GitHub Push Setup" -ForegroundColor Green
Write-Host ""

# Check if Git is available
try {
    $gitVersion = git --version
    Write-Host "✅ Git found: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git is not installed" -ForegroundColor Red
    exit 1
}

# Check if repository is initialized
if (-not (Test-Path .git)) {
    Write-Host "❌ Git repository not initialized. Run setup-github.ps1 first." -ForegroundColor Red
    exit 1
}

# Set repository URL
$repoUrl = "https://github.com/$GitHubUsername/space-mission-agent.git"
Write-Host "📦 Repository URL: $repoUrl" -ForegroundColor Cyan

# Add remote
Write-Host ""
Write-Host "🔗 Adding remote repository..." -ForegroundColor Cyan
git remote remove origin 2>$null
git remote add origin $repoUrl
Write-Host "✅ Remote added" -ForegroundColor Green

# Push to GitHub
Write-Host ""
Write-Host "📤 Pushing to GitHub..." -ForegroundColor Cyan
Write-Host "   (You may be prompted for GitHub credentials)" -ForegroundColor Yellow

$branch = git branch --show-current
if ($branch -ne "main") {
    Write-Host "🔄 Renaming branch to main..." -ForegroundColor Cyan
    git branch -M main
}

git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ Successfully pushed to GitHub!" -ForegroundColor Green
    Write-Host ""
    Write-Host "🔗 Repository URL for submission:" -ForegroundColor Cyan
    Write-Host "   https://github.com/$GitHubUsername/space-mission-agent" -ForegroundColor White
    Write-Host ""
    Write-Host "📋 Copy this URL and paste it in your submission form!" -ForegroundColor Yellow
} else {
    Write-Host ""
    Write-Host "❌ Push failed. Common issues:" -ForegroundColor Red
    Write-Host "   1. Repository doesn't exist on GitHub - create it first at https://github.com/new" -ForegroundColor Yellow
    Write-Host "   2. Authentication failed - use Personal Access Token instead of password" -ForegroundColor Yellow
    Write-Host "   3. Repository already exists - check if it's already pushed" -ForegroundColor Yellow
}

