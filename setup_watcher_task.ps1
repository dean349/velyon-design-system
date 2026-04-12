# setup_watcher_task.ps1
# Registers the Antigravity Inventory Watcher as a Windows Scheduled Task
# It will auto-start when you log into Windows.
# Run this script ONCE as Administrator.

$taskName   = "Antigravity Inventory Watcher"
$scriptPath = "C:\ANTIGRAVITY PROJECTS\VELYON - LEGAL COMMAND CENTER\inventory_watcher.py"
$workingDir = "C:\ANTIGRAVITY PROJECTS\VELYON - LEGAL COMMAND CENTER"

# Find Python executable
$pythonPath = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $pythonPath) {
    $pythonPath = (Get-Command pythonw -ErrorAction SilentlyContinue).Source
}
if (-not $pythonPath) {
    Write-Error "Python not found in PATH. Please install Python 3.9+ and add it to PATH."
    exit 1
}

# Use pythonw.exe to run without a console window (silent background)
$pythonwPath = $pythonPath -replace "python\.exe$", "pythonw.exe"
if (-not (Test-Path $pythonwPath)) {
    $pythonwPath = $pythonPath  # fall back to python.exe
}

Write-Host "Creating scheduled task: '$taskName'" -ForegroundColor Cyan
Write-Host "Python: $pythonwPath"
Write-Host "Script: $scriptPath"

# Remove existing task if present
Unregister-ScheduledTask -TaskName $taskName -Confirm:$false -ErrorAction SilentlyContinue

# Create the task
$action = New-ScheduledTaskAction `
    -Execute $pythonwPath `
    -Argument "`"$scriptPath`"" `
    -WorkingDirectory $workingDir

# Trigger: run at login + restart if it crashes
$trigger = New-ScheduledTaskTrigger -AtLogOn

$settings = New-ScheduledTaskSettingsSet `
    -ExecutionTimeLimit 0 `
    -RestartCount 5 `
    -RestartInterval (New-TimeSpan -Minutes 2) `
    -StartWhenAvailable `
    -RunOnlyIfNetworkAvailable

$principal = New-ScheduledTaskPrincipal `
    -UserId "$env:USERDOMAIN\$env:USERNAME" `
    -LogonType Interactive `
    -RunLevel Highest

Register-ScheduledTask `
    -TaskName  $taskName `
    -Action    $action `
    -Trigger   $trigger `
    -Settings  $settings `
    -Principal $principal `
    -Force | Out-Null

Write-Host ""
Write-Host "  ✅ Task registered successfully!" -ForegroundColor Green
Write-Host "  The watcher will start automatically the next time you log in to Windows."
Write-Host ""
Write-Host "  To start it NOW (without rebooting), run:" -ForegroundColor Yellow
Write-Host "  Start-ScheduledTask -TaskName '$taskName'" -ForegroundColor White
Write-Host ""
Write-Host "  To stop it:" -ForegroundColor Yellow
Write-Host "  Stop-ScheduledTask  -TaskName '$taskName'" -ForegroundColor White
Write-Host ""
Write-Host "  To view the log:" -ForegroundColor Yellow
Write-Host "  notepad '$workingDir\inventory_watcher.log'" -ForegroundColor White
