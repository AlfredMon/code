import tkinter as tk
window = tk.Tk()
window.geometry("500x500")
input_box1 = tk.Entry(window)
input_box1.grid(row=1, column=0) # column is optional here since there's only 1 column
input_box1.insert(0, "0") 

label = tk.Label(window, text="How many books do you have?")
label.grid(row=1, column=1)

input_box2 = tk.Entry(window)
input_box2.grid(row=3, column=0) 
input_box2.insert(0, "0") 
label = tk.Label(window, text="How many weeks do you have?")
label.grid(row=3, column=1)
for i in range(22):
    input_box3 = tk.Entry(window)
    input_box3.grid(row=4+i, column=0)
    input_box3.insert(0, "0") 
    label = tk.Label(window, text="How long in a day do you study?")
    label.grid(row=4+i, column=1)


window.mainloop()