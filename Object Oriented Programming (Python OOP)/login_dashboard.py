import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    if (entered_username == username) and (entered_password == password):
        messagebox.showinfo("Login Successful", "You have successfully logged in!")
        dashboard_window.deiconify()
        login_window.withdraw()
        welcome_label.config(text=f"Welcome, {entered_username}!")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

def logout():
    dashboard_window.withdraw()
    login_window.deiconify()
    messagebox.showinfo("Logged Out", "You have been logged out.")

print(f"SIGN UP:")
username = input("Create a username: ")
password = input("Create a password: ")

login_window = tk.Tk()
login_window.title("Login Window")
login_window.geometry("300x300")

login_frame = ttk.Frame(login_window, padding=20)
login_frame.pack(expand=True)

header_label = ttk.Label(login_frame, text="Enter your credentials:", font=("Helvetica", 16))
header_label.pack(pady=10)

username_label = ttk.Label(login_frame, text="Username: ")
username_label.pack(pady=5)
username_entry = ttk.Entry(login_frame)
username_entry.pack(pady=5)
password_label = ttk.Label(login_frame, text="Password: ")
password_label.pack(pady=5)
password_entry = ttk.Entry(login_frame, show="*")
password_entry.pack(pady=5)

submit_button = ttk.Button(login_frame, text="Submit", command=login)
submit_button.pack(pady=20)

dashboard_window = tk.Toplevel(login_window)
dashboard_window.title("Dashboard Window")
dashboard_window.geometry("300x300")
dashboard_window.withdraw()

dashboard_frame = ttk.Frame(dashboard_window, padding=20)
dashboard_frame.pack(expand=True)

welcome_label = ttk.Label(dashboard_frame, text = "", font=("Helvetica", 16))
welcome_label.pack(pady=10)

logout_button = ttk.Button(dashboard_frame, text="Log Out", command=logout)
logout_button.pack(pady=20)

#Styles
style = ttk.Style()

style.theme_use('clam')

dark_bg = "#2b2b2b"
light_text = "#fafafa"
entry_bg = "#3c3c3c"
button_bg = "#4a4a4a"
button_active_bg = "#5a5a5a"
border_color = "#4a4a4a"

style.configure('.',
                background=dark_bg,
                foreground=light_text,
                fieldbackground=entry_bg,
                bordercolor=border_color,
                font=("Helvetica", 10))

style.configure('TFrame',
                background=dark_bg)

style.configure('TLabel',
                background=dark_bg,
                foreground=light_text,
                font=("Helvetica", 10)) 

style.configure('Header.TLabel',
                font=("Helvetica", 16)) 

header_label.config(style='Header.TLabel')
welcome_label.config(style='Header.TLabel')

style.configure('TButton',
                background=button_bg,
                foreground=light_text,
                bordercolor=border_color,
                font=("Helvetica", 10))

style.map('TButton',
          background=[('active', button_active_bg), ('!disabled', button_bg)],
          foreground=[('active', light_text)])

style.map('TEntry',
          fieldbackground=[('!focus', entry_bg), ('focus', entry_bg)],
          foreground=[('!focus', light_text), ('focus', light_text)],
          bordercolor=[('!focus', border_color), ('focus', light_text)])

login_window.configure(bg=dark_bg)
dashboard_window.configure(bg=dark_bg)

login_window.mainloop()