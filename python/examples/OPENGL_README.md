# OpenGL Enhanced GUI Viewer

## Overview

The `gui_shape_viewer.py` has been enhanced with **OpenGL rendering** for significantly better 3D graphics performance compared to matplotlib.

## Performance Improvements

- **Faster rendering**: OpenGL hardware acceleration provides smooth real-time interaction
- **Better responsiveness**: Mouse rotation and zoom operations are much more fluid
- **Handles larger meshes**: Can easily render complex geometries with thousands of triangles
- **Modern graphics**: Uses shader-based rendering pipeline (OpenGL 3.3 core profile)

## Installation

### Install OpenGL dependencies:

```bash
pip install PyOpenGL PyOpenGL-accelerate moderngl pillow
```

### Optional: For drag-and-drop support:

```bash
pip install tkinterdnd2
```

## Features

### OpenGL Mode (when libraries are installed)
- Hardware-accelerated 3D rendering
- Modern shader-based rendering pipeline
- Real-time lighting with ambient and diffuse components
- Smooth mouse-based rotation and zoom controls
- Dark modern UI theme

### Fallback Mode (matplotlib)
- If OpenGL libraries are not installed, automatically falls back to matplotlib
- Same functionality, but with reduced performance for complex meshes

## Usage

Simply run the viewer:

```bash
python gui_shape_viewer.py
```

The title bar will indicate which rendering mode is active:
- `SHAPE (Python) Viewer - OpenGL` - High performance mode
- `SHAPE (Python) Viewer - Matplotlib` - Fallback mode

## Controls

### Mouse Interactions
- **Left-click + Drag**: Rotate the view
- **Mouse wheel**: Zoom in/out
- **Linux**: Mouse button 4/5 for zoom

### Workflow
1. Browse or drag-and-drop an STL file
2. Select units (auto-detection usually works)
3. Click "Load" to visualize the mesh
4. Check desired metrics
5. Click "Calculate" to compute shape metrics
6. Click "Copy" to copy results to clipboard

## Technical Details

### Rendering Pipeline
- **Vertex Shader**: Transforms vertices using model-view-projection matrix
- **Fragment Shader**: Applies lighting calculations per-pixel
- **Framebuffer**: Renders to offscreen texture, then displays in Tkinter canvas

### Lighting Model
- Ambient lighting: 30% base illumination
- Diffuse lighting: 70% based on surface normal and light direction
- Light direction: (0.5, 0.5, 1.0) - from upper-right-front

### Architecture
- `OpenGLWidget`: Custom Tkinter frame wrapping OpenGL rendering
- `moderngl`: High-level OpenGL context management
- `PIL`: For converting framebuffer to Tkinter-compatible images

## Troubleshooting

### "OpenGL not available" warning
Install the required packages:
```bash
pip install PyOpenGL PyOpenGL-accelerate moderngl pillow
```

### Performance still slow
1. Ensure you have up-to-date graphics drivers
2. Check if `PyOpenGL-accelerate` is installed (provides C-based acceleration)
3. For very large meshes, consider simplifying them first

### Black screen or render errors
- Update graphics drivers
- On Linux, ensure you have proper OpenGL support (`glxinfo | grep "OpenGL version"`)
- On Windows, DirectX and OpenGL should work out of the box with modern drivers

## Comparison: OpenGL vs Matplotlib

| Feature | OpenGL | Matplotlib |
|---------|--------|------------|
| Rendering Speed | ⚡ Very Fast | 🐌 Slow for complex meshes |
| Interaction | 🎮 Real-time | 📊 Laggy with large meshes |
| Visual Quality | ✨ Modern shading | 📈 Basic rendering |
| Memory Usage | 💾 Efficient | 📚 Higher for complex scenes |
| Setup | 📦 Extra dependencies | ✅ Works out of the box |

## Future Enhancements

Possible improvements:
- [ ] Edge highlighting for better geometry visibility
- [ ] Shadow mapping for better depth perception
- [ ] Multiple light sources
- [ ] Material properties (metallic, roughness)
- [ ] Screenshot export
- [ ] Animation recording
- [ ] Point cloud rendering mode
