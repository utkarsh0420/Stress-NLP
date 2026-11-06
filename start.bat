@echo off
title Stress Detection App Launcher
echo ========================================================
echo   Launching Stress Detection Backend and Frontend
echo ========================================================
echo.
echo 1. Starting Flask Backend (port 5000)...
start "Stress Backend (Flask)" cmd /k "title Flask Backend && .venv\Scripts\python.exe app.py"

echo 2. Starting React Frontend (port 3000)...
start "Stress Frontend (Vite)" cmd /k "title React Frontend && npm run dev"

echo.
echo ========================================================
echo Both services are starting!
echo Frontend URL: http://localhost:3000
echo Backend API:  http://localhost:5000/predict
echo ========================================================
echo.
timeout /t 3 >nul
start http://localhost:3000
