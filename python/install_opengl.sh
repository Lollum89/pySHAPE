#!/bin/bash
# Installation script for OpenGL-enhanced SHAPE viewer

echo "=========================================="
echo "Installing OpenGL dependencies for SHAPE"
echo "=========================================="
echo ""

# Check Python is available
if ! command -v python &> /dev/null && ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python not found. Please install Python 3.8 or higher."
    exit 1
fi

# Use python3 if available, otherwise python
PYTHON_CMD=$(command -v python3 || command -v python)

echo "Using: $PYTHON_CMD"
echo ""

# Install core dependencies
echo "📦 Installing core OpenGL libraries..."
$PYTHON_CMD -m pip install PyOpenGL PyOpenGL-accelerate moderngl pillow

if [ $? -eq 0 ]; then
    echo "✅ OpenGL libraries installed successfully"
else
    echo "❌ Error installing OpenGL libraries"
    exit 1
fi

echo ""
echo "📦 Installing optional drag-and-drop support..."
$PYTHON_CMD -m pip install tkinterdnd2

if [ $? -eq 0 ]; then
    echo "✅ Drag-and-drop support installed"
else
    echo "⚠️  Warning: Could not install tkinterdnd2 (optional)"
    echo "   Drag-and-drop will not be available"
fi

echo ""
echo "=========================================="
echo "✅ Installation complete!"
echo "=========================================="
echo ""
echo "You can now run the OpenGL-enhanced viewer:"
echo "  cd examples"
echo "  python gui_shape_viewer.py"
echo ""
