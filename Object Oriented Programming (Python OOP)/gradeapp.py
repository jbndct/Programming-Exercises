import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Student:
  def __init__(self, name, grade):
    self.name = name
    self.grade = grade

  @property
  def remark(self):
    if self.grade >= 75:
      return "Passed"
    else:
      return "Failed"
  
  def display(self):
    return f"{self.name} - {self.grade} - {self.remark}"

class GradeApp:
  def submit_action(self):
    name = self.name_entry.get()
    grade = self.grade_entry.get()

    if not name:
      messagebox.showerror("Input Error", "Name cannot be empty.")
      return

    if not grade or not grade.isdigit() or not (0 <= int(grade) <= 100):
      messagebox.showerror("Input Error", "Please enter a valid grade between 0 and 100.")
      return
    
    student = Student(name, int(grade))
    self.listbox.insert(tk.END, student.display())
    self.students.append(student)
    messagebox.showinfo("Success", f"Added: {student.display()}")
    self.name_entry.delete(0, tk.END)
    self.grade_entry.delete(0, tk.END)

  def clear_all(self):
    if not self.students:
      messagebox.showerror("Error", "Records are already empty.")
      return
    
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all records?"):
      self.students.clear()
      messagebox.showinfo("Success", "All records cleared.")
      self.listbox.delete(0, tk.END)

  def __init__(self, main_window):
    self.main_window = main_window
    self.main_window.title("Mr. Dela Cruz's Grade Tracker")
    self.main_window.geometry("400x500")

    self.main_frame = ttk.Frame(self.main_window, padding=20)
    self.main_frame.pack(expand=True, fill=tk.BOTH)

    self.students = []

    self.header_label = ttk.Label(self.main_frame, text="Enter Student Details", font=("Helvetica", 16))
    self.header_label.pack(pady=10)

    self.name_label = ttk.Label(self.main_frame, text="Student Name:")
    self.name_label.pack(pady=(10, 0))
    self.name_entry = ttk.Entry(self.main_frame)
    self.name_entry.pack()
    self.grade_label = ttk.Label(self.main_frame, text="Student Grade:")
    self.grade_label.pack(pady=(10, 0))
    self.grade_entry = ttk.Entry(self.main_frame)
    self.grade_entry.pack()

    self.submit_button = ttk.Button(self.main_frame, text="Add Student", command=self.submit_action)
    self.submit_button.pack(pady=10)

    self.clear_button = ttk.Button(self.main_frame, text="Clear All", command=self.clear_all)
    self.clear_button.pack(pady=10)

    self.listbox_label = ttk.Label(self.main_frame, text="All Records:")
    self.listbox_label.pack(pady=20)

    self.listbox = tk.Listbox(self.main_frame, height=10)
    self.listbox.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
  main_window = tk.Tk()
  app = GradeApp(main_window)

  # --- Style Block ---
  dark_bg = "#2e2e2e"
  light_text = "#f5f5f5"
  entry_bg = "#3a3a3a"
  button_bg = "#4a4a4a"
  button_active_bg = "#5a5a5a"
  listbox_bg = "#3a3a3a"
  listbox_select_bg = "#0078d4" 

  main_window.configure(bg=dark_bg)

  style = ttk.Style()
  style.theme_use('clam')

  style.configure('.',
                  background=dark_bg,
                  foreground=light_text,
                  fieldbackground=entry_bg,
                  bordercolor=dark_bg,
                  font=("Helvetica", 10))

  style.configure('TFrame',
                  background=dark_bg)

  style.configure('TLabel',
                  background=dark_bg,
                  foreground=light_text)

  style.configure('Header.TLabel',
                  font=("Helvetica", 16, "bold")) # Style for the header

  style.configure('TButton',
                  background=button_bg,
                  foreground=light_text,
                  font=("Helvetica", 10, "bold"),
                  borderwidth=0)

  style.map('TButton',
            background=[('active', button_active_bg), ('!disabled', button_bg)],
            foreground=[('active', light_text)])

  style.map('TEntry',
            fieldbackground=[('!focus', entry_bg), ('focus', entry_bg)],
            foreground=[('!focus', light_text), ('focus', light_text)],
            bordercolor=[('!focus', dark_bg), ('focus', listbox_select_bg)],
            insertcolor=[('!focus', light_text), ('focus', light_text)]) # Cursor color

  app.header_label.config(style='Header.TLabel')

  app.listbox.config(
      bg=listbox_bg,
      fg=light_text,
      selectbackground=listbox_select_bg,
      selectforeground=light_text,
      highlightthickness=0,
      borderwidth=0,
      relief=tk.FLAT
  )

  main_window.mainloop()