import tkinter as tk

def get_values():
    book_count = input_box1.get()
    week_count = input_box2.get()
    study_time = input_box3.get()
    # You can now use these values as needed (e.g., store them in variables or perform calculations).
def pages():
   for i in range(5):
    input_box3 = tk.Entry(window)
    input_box3.grid(row=4+i, column=0)
    input_box3.insert(0, "0") 
    label = tk.Label(window, text="How long in a day do you study?")
    label.grid(row=4+i, column=1)

window = tk.Tk()
window.geometry("500x500")

input_box1 = tk.Entry(window)
input_box1.grid(row=1, column=0)
input_box1.insert(0, "0")

label = tk.Label(window, text="How many books do you have?")
label.grid(row=1, column=1)

input_box2 = tk.Entry(window)
input_box2.grid(row=3, column=0)
input_box2.insert(0, "0")
label = tk.Label(window, text="How many weeks do you have?")
label.grid(row=3, column=1)

input_box3 = tk.Entry(window)
input_box3.grid(row=5, column=0)
input_box3.insert(0, "0")
label = tk.Label(window, text="How long in a day do you study?")
label.grid(row=5, column=1)

# Create a button to retrieve input values
submit_button = tk.Button(window, text="Get Values", command=pages())
submit_button.grid(row=7, columnspan=2)

window.mainloop()
