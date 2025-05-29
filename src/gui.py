import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence
import threading
import os
import subprocess
from main import run_jarvis as start_jarvis

class JarvisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jarvis AI")
        self.root.configure(bg="black")
        self.root.geometry("600x700")
        self.root.resizable(False, False)

        self.is_running = False
        self.gif_frames = []
        self.current_frame = 0
        self.load_gif("assets/jarvis.gif")

        self.canvas = tk.Canvas(self.root, width=500, height=500, bg="black", highlightthickness=0)
        self.canvas.pack(pady=(10, 5))
        self.gif_on_canvas = self.canvas.create_image(250, 250, image=self.gif_frames[0])

        self.start_button = tk.Label(
            root,
            text="▶ Start Jarvis",
            bg="#1f1f1f",
            fg="white",
            font=("Arial", 12, "bold"),
            bd=2,
            relief="ridge",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.start_button.pack(pady=10)
        self.start_button.bind("<Enter>", lambda e: self.start_button.config(bg="#3a3a3a"))
        self.start_button.bind("<Leave>", lambda e: self.start_button.config(bg="#1f1f1f"))
        self.start_button.bind("<Button-1>", lambda e: self.toggle_jarvis())

        self.cmd_frame = tk.Frame(root, bg="black")
        self.cmd_frame.pack(pady=10)
        self.cmd_output = tk.Text(self.cmd_frame, height=3, width=60, bg="black", fg="white", font=("Consolas", 10))
        self.cmd_output.pack()
        self.cmd_output.insert(tk.END, ">>> Waiting for commands...\n")
        self.cmd_output.config(state=tk.DISABLED)

        self.animate_gif()

    def load_gif(self, gif_path):
        gif = Image.open(gif_path)
        self.gif_frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif)]

    def animate_gif(self):
        self.canvas.itemconfig(self.gif_on_canvas, image=self.gif_frames[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
        self.root.after(100, self.animate_gif)

    def toggle_jarvis(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(text="■ Stop Jarvis", fg="red")
            threading.Thread(target=self.run_jarvis, daemon=True).start()
        else:
            self.is_running = False
            self.start_button.config(text="▶ Start Jarvis", fg="white")
            messagebox.showinfo("Jarvis", "Jarvis has been stopped.\n(You can add a kill-switch in main.py)")

    def run_jarvis(self):
        try:
            start_jarvis()
        except Exception as e:
            messagebox.showerror("Error", f"Error while running Jarvis:\n{e}")
        finally:
            self.is_running = False
            self.start_button.config(text="▶ Start Jarvis", fg="white")

if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisGUI(root)
    root.mainloop()
