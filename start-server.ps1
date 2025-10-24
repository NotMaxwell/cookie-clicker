# Cookie Clicker Local Server Starter
Write-Host "Starting Cookie Clicker local server..." -ForegroundColor Green
Write-Host ""

# Check if Python is available
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Using: $pythonVersion" -ForegroundColor Cyan
} catch {
    Write-Host "Python not found! Please install Python 3.x" -ForegroundColor Red
    Write-Host "Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Start the server
try {
    python serve.py
} catch {
    Write-Host "Error starting server: $_" -ForegroundColor Red
    Read-Host "Press Enter to exit"
}
