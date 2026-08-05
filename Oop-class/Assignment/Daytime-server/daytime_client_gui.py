import socket
import tkinter as tk
from tkinter import messagebox

HOST = "localhost"
PORT = 17000


def get_server_time():
    output_text.delete("1.0", tk.END)

    try:
        # Create socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect
        client_socket.connect((HOST, PORT))

        output_text.insert(tk.END, f"Connected to {HOST}:{PORT}\n\n")

        # Receive data
        data = client_socket.recv(1024)

        # Display
        output_text.insert(
            tk.END,
            "Server Time:\n\n" + data.decode("utf-8").strip()
        )

        client_socket.close()

    except Exception as e:
        messagebox.showerror("Connection Error", str(e))


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Daytime Client")
root.geometry("450x300")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Daytime Client",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

btn = tk.Button(
    root,
    text="Get Server Time",
    width=20,
    command=get_server_time
)
btn.pack(pady=10)

output_text = tk.Text(
    root,
    width=50,
    height=10
)
output_text.pack(padx=10, pady=10)

root.mainloop()