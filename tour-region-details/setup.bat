@echo off
SETLOCAL

echo ================================
echo API Key Setup for City Info App
echo ================================

:: Ask user for OpenWeather API key
set /p OPENWEATHER_KEY="Enter your OpenWeather API Key: "

:: Ask user for Google Places API key
set /p GOOGLE_API_KEY="Enter your Google Places API Key: "

:: Save the keys to .env (always)
(
    echo OPENWEATHER_KEY=%OPENWEATHER_KEY%
    echo GOOGLE_API_KEY=%GOOGLE_API_KEY%
) > ".env"

echo.
echo Keys saved successfully to .env
echo ================================
pause
ENDLOCAL
