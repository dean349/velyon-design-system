@echo off
title Antigravity Inventory Watcher
color 0A
echo.
echo  ████████████████████████████████████████████████
echo  ██  ANTIGRAVITY INVENTORY WATCHER v1.0        ██
echo  ████████████████████████████████████████████████
echo.
echo  Watches for new files and auto-publishes to:
echo  https://dean349.github.io/los-romeros-wincham-antigravity-files/
echo.
echo  Press Ctrl+C to stop the watcher.
echo  Log file: inventory_watcher.log
echo.

cd /d "C:\ANTIGRAVITY PROJECTS\VELYON - LEGAL COMMAND CENTER"

:: Check Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo  ERROR: Python not found. Please install Python 3.9+
    pause
    exit /b 1
)

:: Install watchdog if needed (silently)
python -c "import watchdog" >nul 2>&1
if errorlevel 1 (
    echo  Installing watchdog dependency...
    pip install watchdog -q
)

echo  Starting watcher...
echo.
python inventory_watcher.py

:: If it exits, pause so user can see any error
if errorlevel 1 (
    echo.
    echo  ERROR: Watcher exited unexpectedly. Check inventory_watcher.log
    pause
)
