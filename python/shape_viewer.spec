# -*- mode: python ; coding: utf-8 -*-

import os
from pathlib import Path

# Base path is the 'python' folder; we invoke PyInstaller from here.
BASE_DIR = Path.cwd()

# Use the viewer_app entry exclusively (implementation now lives there)
ENTRY = str(BASE_DIR / 'viewer_app' / 'main.py')

a = Analysis(
    [ENTRY],
    pathex=[str(BASE_DIR), str(BASE_DIR / 'viewer_app')],
    binaries=[],
    datas=[
        # Bundle viewer assets (optional) if they exist
        *(
            [(str(BASE_DIR / 'viewer_app' / 'assets'), 'viewer_app/assets')]
            if (BASE_DIR / 'viewer_app' / 'assets').exists() else []
        ),
    ],
    hiddenimports=[
        # Common OpenGL hidden imports
        'OpenGL.GL',
        'OpenGL.GLU',
        'OpenGL.platform.win32',
        # Pillow plugins
        'PIL',
        'PIL._imaging',
        'PIL.Image',
        'PIL.ImageTk',
        # Optional drag-and-drop; ignore if missing
        # 'tkinterdnd2',
        'moderngl',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Exclude heavy modules we don't use in the GUI
        'pytest', 'scipy', 'matplotlib', 'ipykernel', 'notebook'
    ],
    noarchive=False,
)

pyz = PYZ(a.pure)

_exe_kwargs = {}
ICON_PATH = BASE_DIR / 'viewer_app' / 'assets' / 'app.ico'
if ICON_PATH.exists():
    _exe_kwargs['icon'] = str(ICON_PATH)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='SHAPE-Viewer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,   # windowed mode
    disable_windowed_traceback=True,
    **_exe_kwargs,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='SHAPE-Viewer'
)
