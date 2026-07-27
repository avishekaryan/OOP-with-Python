import tkinter as tk
from tkinter import ttk, font, colorchooser, messagebox, filedialog
import os

# ================= WINDOW =================
win = tk.Tk()
win.title("Simple Text Editor")
win.geometry("900x700")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ================= FILE =================
url = None
text_changed = False

# ================= TEXT EDITOR FRAME =================
editor_frame = tk.Frame(win)
editor_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

text_editor = tk.Text(editor_frame, wrap="word", undo=True)
text_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scroll_bar = tk.Scrollbar(editor_frame, command=text_editor.yview)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

text_editor.config(yscrollcommand=scroll_bar.set)
text_editor.focus_set()

# ================= STATUS BAR =================
status_bar = ttk.Label(win, text="Characters: 0 | Words: 0") # themed Tkinter
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

def update_status(event=None):
    content = text_editor.get("1.0", "end-1c")
    status_bar.config(
        text=f"Characters: {len(content)} | Words: {len(content.split())}"
    )
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>", update_status) 
### alternatively we could have done here : text_editor.bind("<<Modified>>", lambda e: update_status()) 
### if we had done this the update_status function would not need event=None

# ================= FONT =================
base_font = font.Font(family="Arial", size=12)
text_editor.configure(font=base_font)

# ================= RICH TEXT TAGS =================
text_editor.tag_configure("bold", font=("Arial", 12, "bold"))
text_editor.tag_configure("italic", font=("Arial", 12, "italic"))
text_editor.tag_configure("underline", font=("Arial", 12, "underline"))

# ================= STYLE FUNCTIONS =================
def toggle_tag(tag):
    try:
        start = text_editor.index("sel.first")
        end = text_editor.index("sel.last")

        if tag in text_editor.tag_names("sel.first"):
            text_editor.tag_remove(tag, start, end)
        else:
            text_editor.tag_add(tag, start, end)

    except tk.TclError:
        pass


def change_bold():
    toggle_tag("bold")

def change_italic():
    toggle_tag("italic")

def change_underline():
    toggle_tag("underline")

def color_change():
    color = colorchooser.askcolor()[1]

    if color:
        tag_name = f"color_{color}"
        text_editor.tag_configure(tag_name, foreground=color)
        toggle_tag(tag_name)

# ================= ALIGNMENT (PARAGRAPH) =================
def align(tag, align_type):
    line_start = text_editor.index("insert linestart")
    line_end = text_editor.index("insert lineend")

    # remove other alignment tags
    text_editor.tag_remove("left", line_start, line_end)
    text_editor.tag_remove("center", line_start, line_end)
    text_editor.tag_remove("right", line_start, line_end)

    text_editor.tag_configure(tag, justify=align_type)
    text_editor.tag_add(tag, line_start, line_end)

def left():
    align("left", "left")

def center():
    align("center", "center")

def right():
    align("right", "right")

# ================= TOOLBAR (ICONS) =================
tool_bar = ttk.Frame(win)
tool_bar.pack(side=tk.TOP, fill=tk.X)

# ================= ICONS =================
new_icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "icons/new.png"))
open_icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "icons/open.png"))
save_icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "icons/save.png"))
save_as_icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "icons/save_as.png"))
exit_icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "icons/exit.png"))

copy_icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "icons/copy.png"))
paste_icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "icons/paste.png"))
cut_icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "icons/cut.png"))
find_icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "icons/find.png"))

bold_icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "icons/bold.png"))
italic_icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "icons/italic.png"))
underline_icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "icons/underline.png"))
font_color_icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "icons/font_color.png"))
align_left_icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "icons/align_left.png"))
align_center_icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "icons/align_center.png"))
align_right_icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "icons/align_right.png"))

# ================= BUTTONS =================
ttk.Button(tool_bar, image=bold_icon, command=change_bold).grid(row=0, column=0)
ttk.Button(tool_bar, image=italic_icon, command=change_italic).grid(row=0, column=1)
ttk.Button(tool_bar, image=underline_icon, command=change_underline).grid(row=0, column=2)
ttk.Button(tool_bar, image=font_color_icon, command=color_change).grid(row=0, column=3)

ttk.Button(tool_bar, image=align_left_icon, command=left).grid(row=0, column=4)
ttk.Button(tool_bar, image=align_center_icon, command=center).grid(row=0, column=5)
ttk.Button(tool_bar, image=align_right_icon, command=right).grid(row=0, column=6)

# ================= FILE FUNCTIONS =================
def new_file():
    global url
    url = None
    text_editor.delete("1.0", tk.END)

def open_file():
    global url
    url = filedialog.askopenfilename(filetypes=[("Text", "*.txt")])
    if url:
        with open(url, "r", encoding="utf-8") as f:
            text_editor.delete("1.0", tk.END)
            text_editor.insert("1.0", f.read())

def save_file():
    global url
    if url:
        with open(url, "w", encoding="utf-8") as f:
            f.write(text_editor.get("1.0", tk.END))
    else:
        save_as()

def save_as():
    global url
    url = filedialog.asksaveasfilename(defaultextension=".txt")
    if url:
        with open(url, "w", encoding="utf-8") as f:
            f.write(text_editor.get("1.0", tk.END))

def exit_fun():
    if messagebox.askokcancel("Exit", "Exit editor?"):
        win.destroy()

# ================= FIND =================
def find_func():
    def find():
        word = find_input.get()
        text_editor.tag_remove("match", "1.0", tk.END)

        if word:
            start = "1.0"
            while True:
                pos = text_editor.search(word, start, stopindex=tk.END)
                if not pos:
                    break
                end = f"{pos}+{len(word)}c"
                text_editor.tag_add("match", pos, end)
                start = end

            text_editor.tag_config("match", background="yellow", foreground="red")

    popup = tk.Toplevel()
    popup.title("Find")

    find_input = ttk.Entry(popup)
    find_input.pack()

    ttk.Button(popup, text="Find", command=find).pack()

# ================= MENU =================
main_menu = tk.Menu(win)

file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label="New", image=new_icon, compound="left", command=new_file)
file_menu.add_command(label="Open", image=open_icon, compound="left", command=open_file)
file_menu.add_command(label="Save", image=save_icon, compound="left", command=save_file)
file_menu.add_command(label="Save As", image=save_as_icon, compound="left", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", image=exit_icon, compound="left", command=exit_fun)

edit_menu = tk.Menu(main_menu, tearoff=0)
edit_menu.add_command(label="Copy", image=copy_icon, compound="left",
                      command=lambda: text_editor.event_generate("<Control-c>"))
edit_menu.add_command(label="Paste", image=paste_icon, compound="left",
                      command=lambda: text_editor.event_generate("<Control-v>"))
edit_menu.add_command(label="Cut", image=cut_icon, compound="left",
                      command=lambda: text_editor.event_generate("<Control-x>"))
edit_menu.add_command(label="Find", image=find_icon, compound="left",
                      command=find_func)

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)

win.config(menu=main_menu)

# ================= SHORTCUTS =================
win.bind("<Control-n>", lambda e: new_file())
win.bind("<Control-o>", lambda e: open_file())
win.bind("<Control-s>", lambda e: save_file())
win.bind("<Control-q>", lambda e: exit_fun())
win.bind("<Control-f>", lambda e: find_func())

# ================= RUN =================
win.mainloop()