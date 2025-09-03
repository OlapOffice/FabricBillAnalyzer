@echo off
echo ================================================
echo Semanticise Inc. Microsoft Fabric Bill Analyzer - Git Setup
echo Visit us at: https://semanticise.com/
echo ================================================
echo.
echo This script will:
echo 1. Initialize Git repository
echo 2. Add remote origin (GitHub)
echo 3. Add all files and commit
echo 4. Push to GitHub repository
echo.
pause

echo Initializing Git repository...
git init

echo Setting up Git user (if not already configured)...
git config user.name "Semanticise Inc."
git config user.email "your-email@example.com"

echo Adding remote repository...
git remote add origin https://github.com/OlapOffice/FabricBillAnalyzer.git

echo Adding all files to staging area...
git add .

echo Creating initial commit...
git commit -m "Semanticise Inc. Enhanced Microsoft Fabric Bill Analyzer with Combined Sorted Report feature

Features added:
- Combined Sorted Report (MeterCategory↑, ConsumedService↑, Cost↓)
- BillSort.csv export functionality
- Enhanced Excel export with Combined_Sorted sheet
- Improved web interface with new export buttons
- Extended CLI with Combined Sorted Report display
- Comprehensive testing and documentation

Ready for production use with backward compatibility maintained."

echo Pushing to GitHub...
git branch -M main
git push -u origin main

echo.
echo ================================================
echo Git setup and push completed!
echo Repository: https://github.com/OlapOffice/FabricBillAnalyzer
echo ================================================
pause