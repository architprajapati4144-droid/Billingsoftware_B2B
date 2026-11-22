"""Entry point for BillCraft Freelance & B2B Invoicing Desktop App."""

from __future__ import annotations

import ctypes
import sys

from app.ui.main_window import MainWindow


def _enable_windows_dpi_awareness() -> None:
    if sys.platform == "win32":
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            pass


def main() -> None:
    _enable_windows_dpi_awareness()
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
