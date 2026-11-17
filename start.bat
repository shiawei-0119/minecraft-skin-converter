@echo off
chcp 65001 >nul
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 server.py
  goto done
)
where python >nul 2>nul
if %errorlevel%==0 (
  python server.py
  goto done
)
echo This website requires Python 3 for localhost mode.
echo You can also open index.html directly in your browser without Python.
echo Python: https://www.python.org/downloads/
pause
:done
