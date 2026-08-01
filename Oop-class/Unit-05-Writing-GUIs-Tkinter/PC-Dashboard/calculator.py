from tkinter import Tk, StringVar, Entry, Button 

# ---------------- WINDOW SETUP ----------------
win = Tk()
win.title("iPhone Style Calculator")
win.geometry("180x260")
win.resizable(False, False)
win.configure(bg="black")

# ---------------- GLOBAL STATE ----------------
expression = ""   # stores the full math expression

# ---------------- DISPLAY UPDATE FUNCTION ----------------
def update_display(value):
    """Updates the calculator screen"""
    display_var.set(value)

# ---------------- BUTTON CLICK ----------------
def btn_click(value):
    """
    Adds clicked button value to expression
    """
    global expression
    expression += str(value)
    update_display(expression)

# ---------------- CLEAR ----------------
def clear():
    """Clears everything"""
    global expression
    expression = ""
    update_display("")

# ---------------- EVALUATE ----------------
def calculate():
    """
    Evaluates expression safely
    """
    global expression
    try:
        result = str(eval(expression)) # interprets the expression as code and returns the executed answer
        update_display(result)
        expression = result  # allows chaining calculations
    except:
        update_display("Error")
        expression = ""

# ---------------- DISPLAY ----------------
display_var = StringVar()

display = Entry(
    win,
    textvariable=display_var,
    font=("Helvetica", 14),
    bg="black",
    fg="white",
    bd=0,
    justify="right"
)
display.grid(row=0, column=0, columnspan=4, ipadx=4, ipady=12.5, sticky="nsew")
# nsew means the widget stretches in all directions inside its grid cell.

# ---------------- BUTTON STYLE HELPERS ----------------
def create_button(text, row, col, command, bg, fg="white", colspan=1):
    """Reusable button creator to reduce repetition"""
    btn = Button(
        win,
        text=text,
        font=("Helvetica", 12, "bold"),
        bg=bg,
        fg=fg,
        bd=0,
        command=command,
        activebackground=bg,
        activeforeground=fg
    )
    btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)
    return btn

# ---------------- BUTTON COLORS (IPHONE STYLE) ----------------
num_color = "#333333"     # dark gray
op_color = "#ff9f0a"      # orange (iPhone operator buttons)
clear_color = "#a5a5a5"   # light gray
bg_color = "black"

# ---------------- ROW 1 ----------------
create_button("7", 1, 0, lambda: btn_click(7), num_color)
create_button("8", 1, 1, lambda: btn_click(8), num_color)
create_button("9", 1, 2, lambda: btn_click(9), num_color)
create_button("+", 1, 3, lambda: btn_click("+"), op_color)

# ---------------- ROW 2 ----------------
create_button("4", 2, 0, lambda: btn_click(4), num_color)
create_button("5", 2, 1, lambda: btn_click(5), num_color)
create_button("6", 2, 2, lambda: btn_click(6), num_color)
create_button("-", 2, 3, lambda: btn_click("-"), op_color)

# ---------------- ROW 3 ----------------
create_button("1", 3, 0, lambda: btn_click(1), num_color)
create_button("2", 3, 1, lambda: btn_click(2), num_color)
create_button("3", 3, 2, lambda: btn_click(3), num_color)
create_button("*", 3, 3, lambda: btn_click("*"), op_color)

# ---------------- ROW 4 ----------------
create_button("0", 4, 0, lambda: btn_click(0), num_color)
create_button("C", 4, 1, clear, clear_color)
create_button(".", 4, 2, lambda: btn_click("."), num_color)
create_button("/", 4, 3, lambda: btn_click("/"), op_color)

# ---------------- EQUAL BUTTON ----------------
create_button("=", 5, 0, calculate, op_color, colspan=4)

# ---------------- GRID RESPONSIVENESS ----------------
# If the window grows or shrinks, how should each row and column expand?
for i in range(6):
    win.grid_rowconfigure(i, weight=1) # weight=1 means all rows get equal share of extra height
for i in range(4):
    win.grid_columnconfigure(i, weight=1)

# ---------------- RUN APP ----------------
win.mainloop()