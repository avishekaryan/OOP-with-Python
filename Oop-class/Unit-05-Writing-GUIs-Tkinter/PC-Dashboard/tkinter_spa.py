import tkinter as tk
from tkinter import messagebox
import json
from collections import deque, defaultdict
from dataclasses import dataclass
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ----------------------------
# Data Model (optional clean structure)
# ----------------------------
@dataclass
class Note:
    title: str
    content: str

# ----------------------------
# Base Frame (OOP Reusability)
# ----------------------------
class BaseFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller


# ----------------------------
# App Controller
# ----------------------------
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter SPA App")
        self.geometry("700x450")

        # ------------------------
        # State Management
        # ------------------------
        self.history = deque()
        self.forward_stack = deque()

        self.app_data = defaultdict(list)
        self.notes = []

        self.file_path = "app_data.json"
        self.file_path=os.path.join(BASE_DIR, self.file_path)

        # ------------------------
        # Container for Frames
        # ------------------------
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (HomePage, NotesPage, SettingsPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.load_data()
        self.navigate(HomePage)

    # ------------------------
    # SPA Navigation System
    # ------------------------
    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise() #moves the selected frame above the others, making it the visible page

    def navigate(self, frame_class):
        self.history.append(frame_class)
        self.forward_stack.clear()
        self.show_frame(frame_class)

    def go_back(self):
        if len(self.history) > 1:
            self.forward_stack.append(self.history.pop())
            self.show_frame(self.history[-1])

    def go_forward(self):
        if self.forward_stack:
            frame = self.forward_stack.pop()
            self.history.append(frame)
            self.show_frame(frame)

    # ------------------------
    # File Handling
    # ------------------------
    def save_data(self):
        try:
            data = {
                "notes": [note.__dict__ for note in self.notes]
            }

            with open(self.file_path, "w") as f:
                json.dump(data, f, indent=4)

        except Exception as e:
            messagebox.showerror("Save Error", str(e))

    def load_data(self):
        if not os.path.exists(self.file_path):
            return

        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)

            self.notes = [Note(**n) for n in data.get("notes", [])]

        except json.JSONDecodeError:
            messagebox.showerror("Error", "Corrupted JSON file")
            self.notes = []

        except Exception as e:
            messagebox.showerror("Error", str(e))


# ----------------------------
# Home Page
# ----------------------------
class HomePage(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        tk.Label(self, text="🏠 Home Page", font=("Arial", 20)).pack(pady=20)

        tk.Button(self, text="Go to Notes",
                  command=lambda: controller.navigate(NotesPage)).pack(pady=5)

        tk.Button(self, text="Settings",
                  command=lambda: controller.navigate(SettingsPage)).pack(pady=5)

        tk.Button(self, text="Back", command=controller.go_back).pack(pady=5)

        tk.Button(self, text="Forward", command=controller.go_forward).pack(pady=5)


# ----------------------------
# Notes Page (Mini Feature)
# ----------------------------
class NotesPage(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.controller = controller

        tk.Label(self, text="📝 Notes", font=("Arial", 18)).pack(pady=10)

        self.title_entry = tk.Entry(self, width=40)
        self.title_entry.pack(pady=5)
        self.title_entry.insert(0, "Title")

        self.text_entry = tk.Text(self, height=8, width=50)
        self.text_entry.pack(pady=5)

        tk.Button(self, text="Add Note", command=self.add_note).pack(pady=5)
        tk.Button(self, text="Save Notes", command=self.save_notes).pack(pady=5)
        tk.Button(self, text="Load Notes", command=self.load_notes).pack(pady=5)

        self.notes_list = tk.Listbox(self, width=60)
        self.notes_list.pack(pady=10)

        tk.Button(self, text="Back", command=controller.go_back).pack()

        self.refresh_notes()

    def add_note(self):
        title = self.title_entry.get()
        content = self.text_entry.get("1.0", tk.END).strip()

        if not title or not content:
            messagebox.showerror("Error", "Title and content required")
            return

        note = Note(title, content)
        self.controller.notes.append(note)

        self.refresh_notes()

    def refresh_notes(self):
        self.notes_list.delete(0, tk.END)

        for n in self.controller.notes:
            self.notes_list.insert(tk.END, f"{n.title}: {n.content[:30]}...")

    def save_notes(self):
        self.controller.save_data()
        messagebox.showinfo("Saved", "Notes saved successfully")

    def load_notes(self):
        self.controller.load_data()
        self.refresh_notes()
        messagebox.showinfo("Loaded", "Notes loaded successfully")


# ----------------------------
# Settings Page
# ----------------------------
class SettingsPage(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        tk.Label(self, text="⚙️ Settings", font=("Arial", 18)).pack(pady=20)

        tk.Button(self, text="Clear Notes", command=self.clear_notes).pack(pady=5)
        tk.Button(self, text="Save Data", command=controller.save_data).pack(pady=5)

        tk.Button(self, text="Back", command=controller.go_back).pack(pady=20)

    def clear_notes(self):
        self.controller.notes.clear()
        messagebox.showinfo("Cleared", "All notes deleted")


# ----------------------------
# Run App
# ----------------------------
if __name__ == "__main__":
    app = App()
    app.mainloop()