from pathlib import Path
import sys

# Ensure repo root/python is importable when running from source
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from viewer_app.gui import ShapeGUI


def main() -> None:
    app = ShapeGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
