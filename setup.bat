@echo off
REM AIUnic Website - Automated GitHub Setup Script (Windows)

echo ======================================
echo AIUnic Website - GitHub Setup Script
echo ======================================
echo.

REM Check if git is installed
where git >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Error: Git is not installed. Please install Git first.
    pause
    exit /b 1
)

REM Get repository URL
echo Enter your GitHub repository URL:
echo Example: https://github.com/yourusername/aiunic-website.git
set /p REPO_URL="URL: "

if "%REPO_URL%"=="" (
    echo Error: Repository URL cannot be empty
    pause
    exit /b 1
)

echo.
echo Configuration:
echo   Repository: %REPO_URL%
echo.
set /p CONFIRM="Continue? (y/n): "

if /i not "%CONFIRM%"=="y" (
    echo Setup cancelled
    pause
    exit /b 0
)

echo.
echo Setting up Git repository...

REM Initialize git if not already initialized
if not exist ".git" (
    git init
    echo Git initialized
) else (
    echo Git already initialized
)

REM Add all files
git add .
echo Files staged

REM Create initial commit
git commit -m "Initial commit - AIUnic website"
echo Initial commit created

REM Add remote origin
git remote add origin "%REPO_URL%" 2>nul
if %ERRORLEVEL% NEQ 0 (
    git remote set-url origin "%REPO_URL%"
)
echo Remote origin configured

REM Create and switch to main branch
git branch -M main
echo Main branch configured

REM Push to GitHub
echo.
echo Pushing to GitHub...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo SUCCESS! Repository pushed to GitHub
    echo.
    echo Next Steps:
    echo   1. Go to your repository on GitHub
    echo   2. Settings -^> Pages
    echo   3. Enable GitHub Pages (source: gh-pages branch^)
    echo   4. Your site will be live in 2-3 minutes
    echo.
    echo Your website will be available at:
    echo   https://yourusername.github.io/repository-name/
    echo.
) else (
    echo.
    echo Error pushing to GitHub
    echo   Please check:
    echo   - Repository URL is correct
    echo   - You have push access
    echo   - Your Git credentials are configured
    echo.
    echo   Try manually: git push -u origin main
)

pause
