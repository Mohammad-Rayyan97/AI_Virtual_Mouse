import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
import sys
import os

# Get absolute path, compatible with PyInstaller and development mode
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp dir
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Run the virtual mouse app in a separate thread
def run_mouse_app():
    try:
        script_path = resource_path("AI_virtualmouse.py")
        subprocess.Popen([sys.executable, script_path], shell=False)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run AI Virtual Mouse:\n{e}")


def start_mouse_app():
    threading.Thread(target=run_mouse_app, daemon=True).start()

# Create GUI
root = tk.Tk()
root.title("AI Virtual Mouse")

# Center the window
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.resizable(False, False)

# Widgets
label = tk.Label(root, text="AI Virtual Mouse App", font=("Helvetica", 16))
label.pack(pady=20)

start_button = tk.Button(root, text="Start", command=start_mouse_app, font=("Helvetica", 14), bg="lightgreen")
start_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Helvetica", 14), bg="salmon")
exit_button.pack(pady=10)

root.mainloop()
