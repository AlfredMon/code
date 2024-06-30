import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json

class StudyPlanner(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Study Planner")
        self.geometry("600x400")
        self.books = {}

        self.title_label = tk.Label(self, text="Book Title:")
        self.title_entry = tk.Entry(self)
        self.pages_label = tk.Label(self, text="Number of Pages:")
        self.pages_entry = tk.Entry(self)
        self.time_label = tk.Label(self, text="Time to Read 10 Pages:")
        self.time_entry = tk.Entry(self)
        self.add_button = tk.Button(self, text="Add Book", command=self.add_book)

        self.days_label = tk.Label(self, text="Number of Study Days:")
        self.days_entry = tk.Entry(self)
        self.max_hours_label = tk.Label(self, text="Max Study Hours per Day:")
        self.max_hours_entry = tk.Entry(self)
        self.min_hours_label = tk.Label(self, text="Min Study Hours per Day:")
        self.min_hours_entry = tk.Entry(self)
        self.off_days_label = tk.Label(self, text="Number of Off Days in a Week:")
        self.off_days_entry = tk.Entry(self)
        self.calculate_button = tk.Button(self, text="Calculate Study Plan", command=self.calculate_plan)

        self.title_label.pack()
        self.title_entry.pack()
        self.pages_label.pack()
        self.pages_entry.pack()
        self.time_label.pack()
        self.time_entry.pack()
        self.add_button.pack()

        self.days_label.pack()
        self.days_entry.pack()
        self.max_hours_label.pack()
        self.max_hours_entry.pack()
        self.min_hours_label.pack()
        self.min_hours_entry.pack()
        self.off_days_label.pack()
        self.off_days_entry.pack()
        self.calculate_button.pack()

    def add_book(self):
        title = self.title_entry.get()
        pages = int(self.pages_entry.get())
        time_to_read_10_pages = float(self.time_entry.get())
        self.books[title] = {'pages': pages, 'time_to_read_10_pages': time_to_read_10_pages}
        messagebox.showinfo("Success", "Book added successfully!")

    def calculate_plan(self):
        days = int(self.days_entry.get())
        max_hours = float(self.max_hours_entry.get())
        min_hours = float(self.min_hours_entry.get())
        off_days = int(self.off_days_entry.get())
        study_days = days - (days // 7) * off_days
        plan = {}
        total_hours = 0
        for title, book in self.books.items():
            pages_per_day = book['pages'] / study_days
            hours_per_day = (pages_per_day / 10) * book['time_to_read_10_pages']
            total_hours += hours_per_day
            plan[title] = {'pages_per_day': pages_per_day, 'hours_per_day': hours_per_day}
        
        if total_hours > max_hours:
            extra_days = total_hours / max_hours
            new_deadline = days + extra_days
            messagebox.showwarning("Warning", f"Your study plan requires {total_hours} hours of study per day, which exceeds your specified maximum of {max_hours} hours. You should consider increasing the number of study days to approximately {new_deadline}.")
        elif total_hours < min_hours:
            less_days = days * (min_hours / total_hours)
            new_deadline = days - less_days
            new_hours = total_hours * (days / new_deadline)
            messagebox.showinfo("Note", f"Your study plan requires only {total_hours} hours of study per day, which is less than your specified minimum of {min_hours} hours. You have two options:\n1. Decrease the number of study days to approximately {new_deadline}, which will increase your daily study hours to {new_hours}.\n2. Increase your daily study hours to {min_hours}, which will keep your study days as {days}.")
        
        with open('study_plan.json', 'w') as f:
            json.dump(plan, f)
        messagebox.showinfo("Success", "Your study plan has been saved to 'study_plan.json'.")

app = StudyPlanner()
app.mainloop()
