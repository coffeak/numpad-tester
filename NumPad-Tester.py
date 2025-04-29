import tkinter as tk
from tkinter import ttk
import keyboard
import threading
import ctypes  #

pressed_keys = []

def on_key_event(e):
    key = e.name.upper()
    if key.startswith('NUM') or key in ['ENTER', 'PLUS', 'MINUS', 'SLASH', 'ASTERISK', 'DOT']:
        display_label.config(text=f"Pressed: {key}")
        if len(pressed_keys) > 9:
            pressed_keys.pop(0)
        pressed_keys.append(key)
        history_var.set("History: " + ", ".join(pressed_keys))

def start_listening():
    keyboard.on_press(on_key_event)

def is_numlock_on():

    VK_NUMLOCK = 0x90
    return bool(ctypes.windll.user32.GetKeyState(VK_NUMLOCK))

def check_numlock():
    state = is_numlock_on()
    numlock_status.config(text=f"NumLock: {'ON' if state else 'OFF'}", foreground='green' if state else 'red')
    root.after(1000, check_numlock)

# GUI
root = tk.Tk()
root.title("NumPad Tester - coffeak.com")
root.geometry("400x300")
root.resizable(False, False)

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 16))

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

display_label = ttk.Label(frame, text="Press a NumPad Key", font=("Helvetica", 18, "bold"))
display_label.pack(pady=10)

numlock_status = ttk.Label(frame, text="Checking NumLock...", font=("Helvetica", 14))
numlock_status.pack(pady=5)

history_var = tk.StringVar()
history_var.set("History: -")
history_label = ttk.Label(frame, textvariable=history_var, font=("Helvetica", 12))
history_label.pack(pady=5)

footer = ttk.Label(root, text="Developed by coffeak.com", font=("Arial", 10, "italic"))
footer.pack(side=tk.BOTTOM, pady=10)

# Başlat
threading.Thread(target=start_listening, daemon=True).start()
check_numlock()
root.mainloop()
