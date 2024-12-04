import socket
import tkinter as tk
from tkinter import messagebox

def center_window(window, width, height):
    """Center the window on the screen."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width // 2) - (width // 2)
    y_coordinate = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

def check_port():
    """Check if the port is in use on the given IP/hostname."""
    address = address_entry.get().strip()
    port = port_entry.get().strip()

    if not address or not port.isdigit():
        result_label.config(text="Error: Enter valid IP/hostname and port.", fg="red")
        return

    port = int(port)

    try:
        with socket.create_connection((address, port), timeout=3):
            result_label.config(text=f"Port {port} on {address} is in use.", fg="green")
    except socket.timeout:
        result_label.config(text=f"Port {port} on {address} is not reachable (timeout).", fg="orange")
    except socket.error:
        result_label.config(text=f"Port {port} on {address} is not in use.", fg="blue")

def show_about():
    """Show the author details."""
    messagebox.showinfo(
        "About",
        "Port Checker v1.0\nAuthor: Your Name\nEmail: your.email@example.com\n© 2024 Your Company"
    )

def show_help():
    """Show the help information."""
    messagebox.showinfo(
        "Help",
        "1. Enter the IP address or hostname in the first field.\n"
        "2. Enter the port number in the second field.\n"
        "3. Click 'Check Port' to verify if the port is in use."
    )

# Create the GUI
root = tk.Tk()
root.title("Port Checker")
root.geometry("400x250")
center_window(root, 400, 250)  # Center the main window

# Add a menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add "Help" menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Help", command=show_help)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Add GUI elements
tk.Label(root, text="IP Address or Hostname:", font=("Arial", 12)).pack(pady=10)
address_entry = tk.Entry(root, font=("Arial", 12))
address_entry.pack(fill="x", padx=20)

tk.Label(root, text="Port Number:", font=("Arial", 12)).pack(pady=10)
port_entry = tk.Entry(root, font=("Arial", 12))
port_entry.pack(fill="x", padx=20)

tk.Button(root, text="Check Port", font=("Arial", 12), command=check_port).pack(pady=10)

# Result display label
result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=380, justify="center")
result_label.pack(pady=20)

# Start the application
root.mainloop()
