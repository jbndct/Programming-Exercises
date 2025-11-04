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

    def __str__(self):
        return f"{self.name} - {self.grade} - {self.remark}"

class GradeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mr. Dela Cruz's Grade Tracker")
        self.root.geometry("400x500")

        self.students = []

        content = ttk.Frame(self.root, padding=20)
        content.pack(expand=True, fill=tk.BOTH)

        input_frame = ttk.Frame(content)
        input_frame.pack(fill='x')

        name_label = ttk.Label(input_frame, text="Student Name:")
        name_label.pack(pady=(0, 5))
        self.name_entry = ttk.Entry(input_frame, width=30)
        self.name_entry.pack()

        grade_label = ttk.Label(input_frame, text="Student Grade:")
        grade_label.pack(pady=(10, 5))
        self.grade_entry = ttk.Entry(input_frame, width=30)
        self.grade_entry.pack()

        button_frame = ttk.Frame(content)
        button_frame.pack(pady=20)

        submit_btn = ttk.Button(button_frame, text="Add Student", command=self.submit_action)
        submit_btn.grid(row=0, column=0, padx=10)

        clear_btn = ttk.Button(button_frame, text="Clear All", command=self.clear_all)
        clear_btn.grid(row=0, column=1, padx=10)

        view_frame = ttk.Frame(content)
        view_frame.pack(fill=tk.BOTH, expand=True)

        view_label = ttk.Label(view_frame, text="All Records:")
        view_label.pack(anchor="w", pady=(0, 5))

        scrollbar = ttk.Scrollbar(view_frame, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(view_frame, height=10, yscrollcommand=scrollbar.set)
        
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def submit_action(self):
        """Validates input and adds a new student."""
        name = self.name_entry.get()
        grade_str = self.grade_entry.get()

        if not name:
            messagebox.showerror("Input Error", "Name cannot be empty.")
            return
        
        try:
            # --- CHANGE 1: Convert to int, not float ---
            grade = int(grade_str)
            
            if not (0 <= grade <= 100):
                raise ValueError
        except ValueError:
            # --- CHANGE 2: Updated error message ---
            messagebox.showerror("Input Error", "Grade must be a whole number between 0 and 100.")
            return

        # Create student and add to list
        student = Student(name, grade)
        self.students.append(student)

        self.update_listbox()

        # Clear input fields
        self.name_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)
        self.name_entry.focus()

    def update_listbox(self):
        """Clears and repopulates the listbox with all student records."""
        self.listbox.delete(0, tk.END)
        for student in self.students:
            self.listbox.insert(tk.END, str(student))

    def clear_all(self):
        """
        Clears the student list and the listbox.
        Prints confirmation to the console.
        """
        if not self.students:
            messagebox.showinfo("Info", "Records are already empty.")
            return

        if messagebox.askyesno("Confirm", "Are you sure you want to clear all records?"):
            self.students = []
            self.update_listbox()
            
            # Prints to the console/terminal
            print("All Records Cleared!")

# --- Main execution ---
if __name__ == "__main__":
    main_window = tk.Tk()
    app = GradeApp(main_window)
    main_window.mainloop()