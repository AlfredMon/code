import tkinter as tk
window = tk.Tk()
window.title("Book Pages Calculator")

entries = []
varEntry = StringVar()
entry = Entry(frame, textvariable=varEntry)
entry.pack()
entry.bind('Return',addToList)

def addToList():
    entries.append(varEntry)

root.mainloop()
