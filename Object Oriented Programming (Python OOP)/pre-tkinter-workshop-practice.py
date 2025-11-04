import tkinter as tk
from tkinter import ttk, messagebox
import io, sys

class MessageApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Message to the World Application")
        self.geometry("400x450")
        self.configure(bg="lightblue")
                
        ttk.Label(self, text="What's Your Message? ", font=("Comic Sans MS", 16, "bold")).pack(pady=15)
        
        form = ttk.Frame(self)
        form.pack(pady=10)
        
        ttk.Label(form, text="Message to the World: ").grid(row=0, column=0, padx=5, pady=5)
        
        self.message = tk.StringVar()
        
        ttk.Entry(form, textvariable=self.message, width=25).grid(row=0, column=1)
        ttk.Button(self, text="Show Message", command=self.messagecommand).pack(pady=10)
    
    def messagecommand(self):
        messagebox.showinfo("Message", f"{self.message.get()}")
        
if __name__ == "__main__":
    app = MessageApp()
    app.mainloop()