import tkinter as tk
from tkinter import Canvas, Frame, Scrollbar

window = tk.Tk()
window.geometry("500x500")

# Create a canvas and a scrollbar
canvas = Canvas(window)
scrollbar = Scrollbar(window, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

# Configure the canvas
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Place the canvas and scrollbar in the window
canvas.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

# Add input boxes and labels to the scrollable frame
label = tk.Label(scrollable_frame, text="How many books do you have?")
label.grid(row=1, column=1)
input_box1 = tk.Entry(scrollable_frame)
input_box1.grid(row=1, column=0)
input_box1.insert(0, "0")

label = tk.Label(scrollable_frame, text="How many weeks do you have?")
label.grid(row=3, column=1)
input_box2 = tk.Entry(scrollable_frame)
input_box2.grid(row=3, column=0)
input_box2.insert(0, "0")

for i in range(22):
    label = tk.Label(scrollable_frame, text=f"How long in a day do you study? {i+1}")
    label.grid(row=4+i, column=1)
    input_box3 = tk.Entry(scrollable_frame)
    input_box3.grid(row=4+i, column=0)
    input_box3.insert(0, "0")

# Make the grid expandable
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

window.mainloop()
