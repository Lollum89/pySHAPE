@echo off
setlocal enabledelayedexpansion

REM Build SHAPE Viewer into a standalone Windows executable using PyInstaller

REM Change to this script's directory (the 'python' folder)
cd /d "%~dp0"

echo [1/7] Locating Python interpreter
REM Prefer Python launcher, fallback to python on PATH
set "PY_CMD="
where py >nul 2>nul && set "PY_CMD=py -3"
if not defined PY_CMD (
    where python >nul 2>nul && set "PY_CMD=python"
)
if not defined PY_CMD (
    echo ERROR: No Python interpreter found. Install Python 3.9+ and ensure 'python' is on PATH.
    exit /b 1
)
for /f "tokens=*" %%v in ('%PY_CMD% --version 2^>^&1') do set PY_VER=%%v
echo Using %PY_CMD% (%PY_VER%)

echo [2/7] Checking virtual environment
REM Create venv if not exists (optional)
if not exist .venv (
    echo Creating virtual environment...
    %PY_CMD% -m venv .venv
)

REM Use venv's pip
set PIP=.venv\Scripts\pip.exe
set PYTHON=.venv\Scripts\python.exe

if not exist "%PYTHON%" (
    echo ERROR: Virtual environment creation failed. Expected interpreter not found at %PYTHON%
    exit /b 1
)

echo [3/7] Installing/Updating dependencies
REM Upgrade pip and install dependencies
"%PIP%" install --upgrade pip
if errorlevel 1 (
    echo ERROR: Failed to upgrade pip.
    exit /b 1
)
"%PIP%" install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install requirements from requirements.txt
    exit /b 1
)
"%PIP%" install pyinstaller
if errorlevel 1 (
    echo ERROR: Failed to install PyInstaller
    exit /b 1
)

echo [4/8] Cleaning previous builds
REM Clean previous builds
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

echo [5/8] Building executable (this may take a minute)
REM Build using spec for stable results
"%PYTHON%" -m PyInstaller shape_viewer.spec --noconfirm --clean

if errorlevel 1 (
    echo Build failed.
    exit /b 1
)

echo.
echo [6/8] Build succeeded.
set DIST_DIR=%cd%\dist\SHAPE-Viewer
set EXE_NAME=SHAPE-Viewer.exe
echo Primary output folder: %DIST_DIR%

REM Convenience: copy the exe to the current folder as well
if exist "%DIST_DIR%\%EXE_NAME%" (
    copy /Y "%DIST_DIR%\%EXE_NAME%" "%cd%\%EXE_NAME%" >nul
    echo Also copied executable to: %cd%\%EXE_NAME%
) else (
    echo WARNING: Expected output not found: %DIST_DIR%\%EXE_NAME%
)

echo.
echo [7/8] Removing legacy OpenGL VC9 DLLs (if present)
set DLL_DIR=%DIST_DIR%\OpenGL\DLLS
if exist "%DLL_DIR%\*.vc9.dll" (
    del /q "%DLL_DIR%\*.vc9.dll"
    echo Removed VC9-era DLLs from: %DLL_DIR%
) else (
    echo No VC9 DLLs found to remove in: %DLL_DIR%
)

echo.
echo [8/8] Distribute the entire folder at: %DIST_DIR%
echo To run, double-click: %EXE_NAME%

endlocal@echo off
setlocal enabledelayedexpansion

REM Build SHAPE Viewer into a standalone Windows executable using PyInstaller

REM Change to this script's directory (the 'python' folder)
cd /d "%~dp0"

echo [1/5] Checking virtual environment
REM Create venv if not exists (optional)
if not exist .venv (
    echo Creating virtual environment...
    py -3 -m venv .venv
)

REM Use venv's pip
set PIP=.venv\Scripts\pip.exe
set PYTHON=.venv\Scripts\python.exe

echo [2/5] Installing/Updating dependencies
REM Upgrade pip and install dependencies
"%PIP%" install --upgrade pip
"%PIP%" install -r requirements.txt
"%PIP%" install pyinstaller

echo [3/5] Cleaning previous builds
REM Clean previous builds
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

echo [4/5] Building executable (this may take a minute)
REM Build using spec for stable results
"%PYTHON%" -m PyInstaller shape_viewer.spec --noconfirm --clean

if errorlevel 1 (
    echo Build failed.
    exit /b 1
)

echo.
echo [5/5] Build succeeded.
set DIST_DIR=%cd%\dist\SHAPE-Viewer
set EXE_NAME=SHAPE-Viewer.exe
echo Primary output folder: %DIST_DIR%

REM Convenience: copy the exe to the current folder as well
if exist "%DIST_DIR%\%EXE_NAME%" (
    copy /Y "%DIST_DIR%\%EXE_NAME%" "%cd%\%EXE_NAME%" >nul
    echo Also copied executable to: %cd%\%EXE_NAME%
) else (
    echo WARNING: Expected output not found: %DIST_DIR%\%EXE_NAME%
)

echo.
echo Distribute the entire folder at: %DIST_DIR%
echo To run, double-click: %EXE_NAME%

endlocal
