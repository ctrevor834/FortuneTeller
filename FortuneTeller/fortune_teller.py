# file: fortune_teller.py

import random
import tkinter as tk
from tkinter import messagebox
import os
import sys
import shutil
from pathlib import Path
import ctypes
from win32com.client import Dispatch
from datetime import datetime

VERSION = "1.0"
BUILD_DATE = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_random_fortune() -> str:
    fortunes = [
        "You will have a great day today!",
        "A surprise is waiting for you soon.",
        "Your hard work will pay off.",
        "Trust your instincts today.",
        "Adventure is around the corner!",
        "You will make a valuable new connection.",
        "Today is a good day to start something new.",
        "You will find what you've been seeking.",
        "Smile! Good fortune is smiling back."
    ]
    return random.choice(fortunes)

def show_fortune(fortune: str) -> None:
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(f"Fortune Teller Bot v{VERSION}", f"{fortune}\n\nBuilt: {BUILD_DATE}")
    root.destroy()

def install_to_startup() -> None:
    script_path = Path(sys.executable if getattr(sys, 'frozen', False) else __file__).resolve()
    startup_dir = Path(os.getenv("APPDATA")) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"

    shortcut_path = startup_dir / (script_path.stem + ".lnk")
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(str(shortcut_path))
    shortcut.Targetpath = str(script_path)
    shortcut.WorkingDirectory = str(script_path.parent)
    shortcut.IconLocation = str(script_path)
    shortcut.save()

    print(f"✅ Installed to startup: {shortcut_path}")

def uninstall_from_startup() -> None:
    script_path = Path(sys.executable if getattr(sys, 'frozen', False) else __file__).resolve()
    startup_dir = Path(os.getenv("APPDATA")) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"

    shortcut_path = startup_dir / (script_path.stem + ".lnk")

    if shortcut_path.exists():
        shortcut_path.unlink()
        print(f"🗑️ Removed from startup: {shortcut_path}")
    else:
        print("⚠️ No startup shortcut found.")

def main() -> None:
    if len(sys.argv) > 1:
        if sys.argv[1] == "--install":
            install_to_startup()
        elif sys.argv[1] == "--uninstall":
            uninstall_from_startup()
    else:
        fortune = get_random_fortune()
        show_fortune(fortune)

if __name__ == "__main__":
    main()
