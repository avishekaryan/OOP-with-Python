## Importing

```python
import tkinter as tk
from tkinter import ttk, font, colorchooser, messagebox, filedialog
import os
```

## WINDOW

```python
win = tk.Tk()
win.title("Simple Text Editor")
win.geometry("900x700")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
```

## TEXT EDITOR FRAME

```python
editor_frame = tk.Frame(win)
editor_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
```

- Creates a Frame widget inside the main window (win)
- Acts as a container for the text editor and scrollbar
- `pack(fill=tk.BOTH, expand=True):`
    - Expands the frame in both horizontal and vertical directions
    - Allows it to resize with the window

```python
text_editor = tk.Text(editor_frame, wrap="word", undo=True)
text_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
```

- Creates a multi-line text input area
- editor_frame is the parent container
- wrap="word":
    - Wraps text at word boundaries (no breaking words in half)
- undo=True:
    - Enables undo/redo functionality (Ctrl+Z, Ctrl+Y)

```python
scroll_bar = tk.Scrollbar(editor_frame, command=text_editor.yview)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

text_editor.config(yscrollcommand=scroll_bar.set)
text_editor.focus_set()
```

- Create a scollbar widget and then Link it to the text box using `command=text_editor.yview`
- `text_editor.config(yscrollcommand=scroll_bar.set)`: 
    - Links the text box back to the scrollbar
    - Ensures:
        - When text scrolls → scrollbar moves
        - When scrollbar is dragged → text scrolls
- `text_editor.focus_set()`: 
    - Automatically places the cursor inside the text box
    - User can start typing immediately without clicking

## STATUS BAR

```python
status_bar = ttk.Label(win, text="Characters: 0 | Words: 0")  # themed Tkinter
status_bar.pack(side=tk.BOTTOM, fill=tk.X)
```

- Creates a status bar using `ttk.Label`
- Displays text: "Characters: 0 | Words: 0"
- Uses themed Tkinter widget for better UI appearance
- Placed inside the main window (`win`)
- Positioned at the bottom of the window
- Stretches horizontally across the full width (`fill=tk.X`)
- Acts as an information display area like in real text editors

```python
def update_status(event=None):
    content = text_editor.get("1.0", "end-1c")
    status_bar.config(
        text=f"Characters: {len(content)} | Words: {len(content.split())}"
    )
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>", update_status)
```

- Alternatively we could have done here : text_editor.bind("<<Modified>>", lambda e: update_status()) 
- If we had done this the update_status function would not need event=None
- Defines a function `update_status` to update the status bar
- Accepts an optional `event` parameter (required for Tkinter event binding)
- Retrieves full text from the text editor (`1.0` to `end-1c`)
- Calculates number of characters using `len(content)`
- Calculates number of words using `len(content.split())`
- Updates the status bar label with the new values
- Resets the modified flag using `text_editor.edit_modified(False)`
- Prevents continuous triggering of the modified event
- Binds the function to the `<<Modified>>` event of the text widget
- This event triggers whenever the text is changed
- Alternative approach shown using a lambda function
- Lambda removes the need for the `event` parameter in the function
- In that case, `update_status` would not need `event=None`

## FONT
```python
base_font = font.Font(family="Arial", size=12)
text_editor.configure(font=base_font)
```

- Creates a font object using `tkinter.font`
- Sets font family to Arial and size to 12
- Applies the font to the text editor widget
- Ensures all typed text uses the defined base font

## TEXT TAGS
```python
text_editor.tag_configure("bold", font=("Arial", 12, "bold"))
text_editor.tag_configure("italic", font=("Arial", 12, "italic"))
text_editor.tag_configure("underline", font=("Arial", 12, "underline"))
```

- Defines a "bold" text `tag` with Arial 12 bold styling
- Defines an "italic" text `tag` with Arial 12 italic styling
- Defines an "underline" text `tag` with Arial 12 underline styling
- These tags allow formatting selected text in the editor
- Each `tag` can be applied to specific text ranges independently

## STYLE FUNCTIONS
```python
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
```

- Defines `toggle_tag` function to apply/remove text styles
- Gets selected text start (`sel.first`) and end (`sel.last`) positions
- Checks if the selected text already has the given tag
- If tag exists, removes it from the selection
- If tag does not exist, applies it to the selection
- Uses `try/except` to handle cases where no text is selected
- Ignores `tk.TclError` when selection is empty

```python
def change_bold():
    toggle_tag("bold")

def change_italic():
    toggle_tag("italic")

def change_underline():
    toggle_tag("underline")

def color_change():
    color = colorchooser.askcolor()[1]
    if color:
        text_editor.config(fg=color)
```

- Defines `change_bold` to apply/remove bold formatting using `toggle_tag`
- Defines `change_italic` to apply/remove italic formatting using `toggle_tag`
- Defines `change_underline` to apply/remove underline formatting using `toggle_tag`

Color Change: 
- Defines `color_change` to change text color
- Opens a color picker dialog using `colorchooser.askcolor()`
- Extracts selected color value
- Applies chosen color to all text using `fg=color`
- Only updates color if a valid selection is made

## ALIGNMENT (PARAGRAPH)

```python
def align(tag, align_type):
    line_start = text_editor.index("insert linestart")
    line_end = text_editor.index("insert lineend")

    # remove other alignment tags
    text_editor.tag_remove("left", line_start, line_end)
    text_editor.tag_remove("center", line_start, line_end)
    text_editor.tag_remove("right", line_start, line_end)

    text_editor.tag_configure(tag, justify=align_type)
    text_editor.tag_add(tag, line_start, line_end)
```

- Defines `align` function to set paragraph alignment
- Gets current line start (`insert linestart`) and end (`insert lineend`)
- Removes existing alignment tags (left, center, right)
- Configures the selected alignment tag with `justify` option
- Applies the tag to the current line only

```python
def left():
    align("left", "left")

def center():
    align("center", "center")

def right():
    align("right", "right")
```

- `left()` applies left alignment using `"left"` tag
- `center()` applies center alignment using `"center"` tag
- `right()` applies right alignment using `"right"` tag

## TOOLBAR

```python
tool_bar = ttk.Frame(win)
tool_bar.pack(side=tk.TOP, fill=tk.X)
```

- Creates a toolbar frame using `ttk.Frame`
- Acts as a container for formatting buttons/icons
- Placed inside the main window (`win`)
- Positioned at the top of the window
- Stretches horizontally across the full width (`fill=tk.X`)

## ICON

```python
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
```

- Loads image icons using `tk.PhotoImage`
- Uses `os.path.join(BASE_DIR, "icons/...")` to build correct file paths
- Stores each icon in a variable for later use in buttons
- Includes file operation icons: new, open, save, save as, exit
- Includes edit icons: copy, paste, cut, find
- Includes formatting icons: bold, italic, underline, font color
- Includes alignment icons: left, center, right
- Ensures all icons are loaded from a centralized `icons` folder

## BUTTONS

```python

ttk.Button(tool_bar, image=bold_icon, command=change_bold).grid(row=0, column=0)
ttk.Button(tool_bar, image=italic_icon, command=change_italic).grid(row=0, column=1)
ttk.Button(tool_bar, image=underline_icon, command=change_underline).grid(row=0, column=2)
ttk.Button(tool_bar, image=font_color_icon, command=color_change).grid(row=0, column=3)

ttk.Button(tool_bar, image=align_left_icon, command=left).grid(row=0, column=4)
ttk.Button(tool_bar, image=align_center_icon, command=center).grid(row=0, column=5)
ttk.Button(tool_bar, image=align_right_icon, command=right).grid(row=0, column=6)
```

- Creates a button for making text bold.
- Creates a button for making text italic.
- Creates a button for underlining text.
- Creates a button for changing the text color.
- Creates a button for aligning text to the left.
- Creates a button for centering text.
- Creates a button for aligning text to the right.
- Places all buttons in the first row of the toolbar across consecutive columns.

```python
def new_file():
    global url
    url = None
    text_editor.delete("1.0", tk.END)
```

- Defines a function to create a new file.
- Resets the current file reference by setting the file path to `None`.
- Clears all text from the text editor.

```python
def open_file():
    global url
    url = filedialog.askopenfilename(filetypes=[("Text", "*.txt")])
    if url:
        with open(url, "r", encoding="utf-8") as f:
            text_editor.delete("1.0", tk.END)
            text_editor.insert("1.0", f.read())
```

- Defines a function to open a text file.
- Prompts the user to select a `.txt` file.
- Stores the selected file path.
- Opens the selected file using UTF-8 encoding.
- Clears the existing text in the editor.
- Loads the file content into the text editor.

```python
def save_file():
    global url
    if url:
        with open(url, "w", encoding="utf-8") as f:
            f.write(text_editor.get("1.0", tk.END))
    else:
        save_as()
```

- Defines a function to save the current file.
- Checks whether a file path already exists.
- Writes the editor content to the existing file using UTF-8 encoding.
- Calls the **Save As** function if no file path is available.

```python
def save_as():
    global url
    url = filedialog.asksaveasfilename(defaultextension=".txt")
    if url:
        with open(url, "w", encoding="utf-8") as f:
            f.write(text_editor.get("1.0", tk.END))
```

- Defines a function to save the file with a new name.
- Prompts the user to choose a save location and filename.
- Sets the default file extension to `.txt`.
- Stores the selected file path.
- Writes the editor content to the selected file using UTF-8 encoding.

```python
def exit_fun():
    if messagebox.askokcancel("Exit", "Exit editor?"):
        win.destroy()
```

- Defines a function to exit the application.
- Displays a confirmation dialog before closing.
- Closes the application if the user confirms.

## FIND

```python
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
```

- Defines a function to open the Find dialog.
- Creates a nested function to search for text.
- Gets the search keyword from the input field.
- Removes any previous search highlights.
- Searches the editor for all occurrences of the keyword.
- Highlights each matching word.
- Displays matches with a yellow background and red text.
- Creates a pop-up window for the Find feature.
- Adds a text input field for entering the search term.
- Adds a **Find** button to start the search.

## MENU

```python
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
```

- Creates the main menu for the application.
- Creates a **File** menu.
- Adds a **New** option to create a new file.
- Adds an **Open** option to open an existing file.
- Adds a **Save** option to save the current file.
- Adds a **Save As** option to save the file with a new name.
- Adds a separator to organize the File menu.
- Adds an **Exit** option to close the application.
- Creates an **Edit** menu.
- Adds a **Copy** option to copy selected text.
- Adds a **Paste** option to paste copied text.
- Adds a **Cut** option to remove and copy selected text.
- Adds a **Find** option to search for text in the editor.
- Adds the **File** and **Edit** menus to the main menu bar.
- Attaches the menu bar to the application window.

## SHORTCUTS

```python
win.bind("<Control-n>", lambda e: new_file())
win.bind("<Control-o>", lambda e: open_file())
win.bind("<Control-s>", lambda e: save_file())
win.bind("<Control-q>", lambda e: exit_fun())
win.bind("<Control-f>", lambda e: find_func())
```

- Assigns **Ctrl + N** as the shortcut for creating a new file.
- Assigns **Ctrl + O** as the shortcut for opening a file.
- Assigns **Ctrl + S** as the shortcut for saving the current file.
- Assigns **Ctrl + Q** as the shortcut for exiting the application.
- Assigns **Ctrl + F** as the shortcut for opening the Find dialog.

## RUN

```python
win.mainloop()
```

- Starts the Tkinter event loop.
- Keeps the application window running and responsive.