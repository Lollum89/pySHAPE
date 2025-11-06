"""
Deprecated location for the viewer GUI.

This example now forwards to the packaged module in `viewer_app.gui`.
Please prefer running one of these from the `python` folder:
  - python -m viewer_app.main
  - python viewer_app/main.py
"""
from pathlib import Path
import sys

# Ensure repo root/python on path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from viewer_app.gui import ShapeGUI  # type: ignore


if __name__ == '__main__':
    print("Note: 'examples/gui_shape_viewer.py' is deprecated. Launching viewer_app.gui…")
    app = ShapeGUI()
    app.mainloop()
