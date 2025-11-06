@echo off
REM Installation script for OpenGL-enhanced SHAPE viewer (Windows)

echo ==========================================
echo Installing OpenGL dependencies for SHAPE
echo ==========================================
echo.

REM Check Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python not found. Please install Python 3.8 or higher.
    exit /b 1
)

echo Using: python
python --version
echo.

REM Install core dependencies
echo Installing core OpenGL libraries...
python -m pip install PyOpenGL PyOpenGL-accelerate moderngl pillow

if errorlevel 1 (
    echo Error installing OpenGL libraries
    exit /b 1
)
echo OpenGL libraries installed successfully
echo.

REM Install optional drag-and-drop
echo Installing optional drag-and-drop support...
python -m pip install tkinterdnd2

if errorlevel 1 (
    echo Warning: Could not install tkinterdnd2 (optional^)
    echo    Drag-and-drop will not be available
) else (
    echo Drag-and-drop support installed
)

echo.
echo ==========================================
echo Installation complete!
echo ==========================================
echo.
echo You can now run the OpenGL-enhanced viewer:
echo   cd examples
echo   python gui_shape_viewer.py
echo.
pause
