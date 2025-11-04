import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def login(event=None):
    if username_entry.get() == signup_username and password_entry.get() == signup_password:
        dashboard_frame.deiconify()  
        login_frame.withdraw()
        welcome_label.config(text=f"Hello, {username_entry.get()}!")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")

def logout():
    dashboard_frame.withdraw()
    login_frame.deiconify()

def close():
    login_frame.destroy()

print("=== Sign Up ===")
signup_username = input("Create a username: ")
signup_password = input("Create a password: ")
print("\nAccount created! Now open the GUI window to log in.\n")

# --- Main Login Window ---
login_frame = tk.Tk()
login_frame.title("Login Window")
login_frame.geometry("300x300")

# --- Dark Mode Style ---
# Define colors
BG_COLOR = "#2E2E2E"       # Dark grey background
TEXT_COLOR = "#FFFFFF"     # White text
ENTRY_BG = "#4A4A4A"       # Lighter grey for entry fields
BUTTON_BG = "#5A5A5A"       # Medium grey for buttons
BUTTON_ACTIVE = "#6A6A6A"  # Lighter grey for active/hovered button

# Apply style
style = ttk.Style()
style.theme_use('clam')  # Use 'clam' theme as a base (it's easily configurable)

# Configure root window background
login_frame.config(bg=BG_COLOR)

# Configure ttk widget styles
style.configure("TFrame", background=BG_COLOR)
style.configure("TLabel", background=BG_COLOR, foreground=TEXT_COLOR)
style.configure("TButton", background=BUTTON_BG, foreground=TEXT_COLOR, borderwidth=0)
style.map("TButton",
    background=[('active', BUTTON_ACTIVE)],  # Color when button is pressed
    foreground=[('active', TEXT_COLOR)]
)

style.configure("TEntry",
    fieldbackground=ENTRY_BG,
    foreground=TEXT_COLOR,
    insertcolor=TEXT_COLOR,  # This is the typing cursor
    borderwidth=0
)
# --- End of Style ---

content = ttk.Frame(login_frame, padding=20)
content.pack(expand=True)

# Title
title_label = ttk.Label(content, text="User Login", font=("Segoe UI", 16, "bold"))
title_label.pack(pady=10)

# Username
username_label = ttk.Label(content, text="Username:")
username_label.pack(anchor="center", pady=(5, 0))
username_entry = ttk.Entry(content, width=25)
username_entry.pack(pady=5)

# Password
password_label = ttk.Label(content, text="Password:")
password_label.pack(anchor="center", pady=(5, 0))
password_entry = ttk.Entry(content, width=25, show="*")
password_entry.pack(pady=5)

# Login button
login_btn = ttk.Button(content, text="Login", command=login)
login_btn.pack(pady=15)
login_frame.bind("<Return>", login)

# --- Dashboard Window ---
dashboard_frame = tk.Toplevel(login_frame)
dashboard_frame.title("Dashboard Window")
dashboard_frame.geometry("400x200")
dashboard_frame.withdraw()

# Apply dark mode to the dashboard window as well
dashboard_frame.config(bg=BG_COLOR)

# Widgets in the dashboard will automatically use the style
welcome_label = ttk.Label(dashboard_frame, text="", font=("Segoe UI", 16, "bold"))
welcome_label.pack(pady=20)

logout_btn = ttk.Button(dashboard_frame, text="Logout", command=logout)
logout_btn.pack(pady=20)

# Proper close handling
login_frame.protocol("WM_DELETE_WINDOW", close)
dashboard_frame.protocol("WM_DELETE_WINDOW", close)

login_frame.mainloop()