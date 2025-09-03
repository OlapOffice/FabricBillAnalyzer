# Microsoft Fabric Bill Analyzer - Git Setup PowerShell Script

Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "Microsoft Fabric Bill Analyzer - Git Setup" -ForegroundColor Yellow
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Check if Git is installed
try {
    $gitVersion = git --version
    Write-Host "✅ Git found: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Git from https://git-scm.com/" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Change to project directory
$projectDir = "C:\Users\OLAPS\OneDrive\Personal\fabric-bill-analyzer-enhanced"
Set-Location $projectDir

Write-Host "📂 Working in: $projectDir" -ForegroundColor Blue

# Initialize Git repository
Write-Host "🔧 Initializing Git repository..." -ForegroundColor Yellow
try {
    git init
    Write-Host "✅ Git repository initialized" -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to initialize Git repository" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Configure Git user (update with your details)
Write-Host "👤 Configuring Git user..." -ForegroundColor Yellow
git config user.name "OLAP Office"
git config user.email "olapoffice@example.com"  # Update with your email

# Add remote repository
Write-Host "🌐 Adding remote repository..." -ForegroundColor Yellow
try {
    git remote add origin https://github.com/OlapOffice/FabricBillAnalyzer.git
    Write-Host "✅ Remote repository added" -ForegroundColor Green
} catch {
    Write-Host "⚠️ Remote might already exist, continuing..." -ForegroundColor Yellow
}

# Check if there are any files to add
$files = git status --porcelain
if ($files) {
    # Add all files
    Write-Host "📁 Adding files to staging area..." -ForegroundColor Yellow
    git add .
    
    # Create commit
    Write-Host "💾 Creating initial commit..." -ForegroundColor Yellow
    $commitMessage = @"
Enhanced Microsoft Fabric Bill Analyzer with Combined Sorted Report

🆕 NEW FEATURES:
- Combined Sorted Report (MeterCategory↑, ConsumedService↑, Cost↓)
- BillSort.csv export functionality
- Enhanced Excel export with Combined_Sorted sheet
- Improved web interface with new export buttons
- Extended CLI with Combined Sorted Report display
- Comprehensive testing and documentation

✅ HIGHLIGHTS:
- Production-ready with backward compatibility
- Sample data and test scripts included
- Multiple usage options (Web, CLI, Python API)
- Complete documentation and usage guides

🚀 Ready for deployment and sharing!
"@
    
    git commit -m $commitMessage
    Write-Host "✅ Commit created successfully" -ForegroundColor Green
} else {
    Write-Host "ℹ️ No files to commit" -ForegroundColor Blue
}

# Set main branch and push
Write-Host "🚀 Pushing to GitHub..." -ForegroundColor Yellow
try {
    git branch -M main
    git push -u origin main --force
    Write-Host "✅ Successfully pushed to GitHub!" -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to push to GitHub" -ForegroundColor Red
    Write-Host "This might be due to:" -ForegroundColor Yellow
    Write-Host "- Repository doesn't exist on GitHub" -ForegroundColor Yellow
    Write-Host "- Authentication issues" -ForegroundColor Yellow
    Write-Host "- Network connectivity problems" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "🎉 Git Setup Complete!" -ForegroundColor Green
Write-Host "Repository: https://github.com/OlapOffice/FabricBillAnalyzer" -ForegroundColor Blue
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Show repository status
Write-Host "📊 Repository Status:" -ForegroundColor Yellow
git status

Write-Host ""
Write-Host "📋 Recent commits:" -ForegroundColor Yellow
git log --oneline -5

Read-Host "Press Enter to exit"
