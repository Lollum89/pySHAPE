# SHAPE Viewer App

Tkinter + ModernGL viewer for SHAPE, organized as a small app package for running and packaging.

- Entry script: `viewer_app/main.py`
- Implementation: `viewer_app/gui.py` (ShapeGUI and OpenGLWidget)
- Optional icon: add `viewer_app/assets/app.ico` to brand the executable

## Run from source
From the `python` folder:

```bash
python -m viewer_app.main
```

or

```bash
python viewer_app/main.py
```

## Packaging
Use the Windows build script from the `python` folder:

```bat
build_viewer_exe.bat
```

The PyInstaller spec uses `viewer_app/main.py` as the entry point and will embed the icon automatically if `viewer_app/assets/app.ico` exists.
