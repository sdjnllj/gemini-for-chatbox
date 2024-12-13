@echo off
echo Starting OpenRouter proxy server...

REM 检查 Python 是否已安装
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM 检查 proxy.py 是否存在
if not exist proxy.py (
    echo Error: proxy.py not found in current directory
    pause
    exit /b 1
)

REM 检查必要的 Python 包
python -c "import flask" >nul 2>nul
if %errorlevel% neq 0 (
    echo Installing required package: flask...
    pip install flask
)

python -c "import requests" >nul 2>nul
if %errorlevel% neq 0 (
    echo Installing required package: requests...
    pip install requests
)

echo Starting proxy server on http://localhost:8080
python proxy.py

pause 