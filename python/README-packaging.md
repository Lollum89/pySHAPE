# Packaging SHAPE Viewer (Windows)

This guide creates a standalone Windows executable for the Tkinter-based OpenGL viewer located in `viewer_app/`.

## Prerequisites
- Windows with Python 3.9+ installed (the `py` launcher recommended)
- GPU drivers with OpenGL support (ModernGL uses a hidden OpenGL context)

The build script will create a virtual environment and install all dependencies, including PyInstaller.

## One‑click build
From the repository root in a terminal:

```bat
cd python
build_viewer_exe.bat
```

When it finishes, the executable will be in:

```
python\dist\SHAPE-Viewer\SHAPE-Viewer.exe
```

Distribute the entire `SHAPE-Viewer` folder (it includes runtime files such as Tcl/Tk and Python libs). For convenience, the script also copies `SHAPE-Viewer.exe` into the `python\` folder.

## Notes
- Drag‑and‑drop support via `tkinterdnd2` is optional. If you want it, install it before building. The app auto-detects it at runtime.
- The app renders offscreen (ModernGL) and displays frames inside a Tkinter widget using Pillow. No native OpenGL window is required.
- If target machines lack a working OpenGL driver, rendering may be slow/fallback. Update GPU drivers if you see issues.
- STL loading and metrics use the `pyshape` package bundled inside the executable by PyInstaller via import analysis.
- To brand the executable, place an icon file at `viewer_app/assets/app.ico` before building; the spec will include it automatically.

## Troubleshooting
- If you see a blank window on a different machine, ensure GPU drivers are installed. You can also try running with an environment variable to force ANGLE/DirectX if available on the system.
- Antivirus can block unsigned executables. Add an exception or sign the binary for distribution.
- If you need a single‐file exe, add `--onefile` to the build command in the batch script. This makes startup a bit slower and may increase AV false positives.
