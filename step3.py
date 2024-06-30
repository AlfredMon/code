# Initialize the window
import tkinter as tk
window = tk.Tk()
window.title("Study Calculator")
window.geometry("1000x1000")
# Initialize dictionaries to store book information
book_info = {}
# Initialize Data entry loop
def start_loop():
    global running
    running = True
    while running: 
       il=0
       il=il+1    
def stop_loop():
    global running
    running = False

#Take book values for each item.   
def get_books_values():
    # Given values from input fields
    book_count = int(input_box1.get())
    week_count = int(input_box2.get())
    study_time = int(input_box3.get())
    
    # Create first labels and entry fields for book name and pages
    for i in range(book_count):
        book_name_label = tk.Label(window, text=f"Enter Book Name {i + 1}:")
        book_name_label.grid(row=9 + i, column=0)
        default_book_name = f"Book{i + 1}"
        book_name_var = tk.StringVar()  # Create a StringVar for book name
        book_name_entry = tk.Entry(window, textvariable=book_name_var)
        book_name_entry.grid(row=9 + i, column=1)
        book_name_entry.insert(0, default_book_name)  # Set default value

        pages_label = tk.Label(window, text="Enter Number of Pages:")
        pages_label.grid(row=9 + i, column=2)
        pages_var = tk.StringVar()  # Create a StringVar for page number
        pages_entry = tk.Entry(window, textvariable=pages_var)
        pages_entry.grid(row=9 + i, column=3)
        pages_entry.insert(0, "1")  # Set default value

        book_name = book_name_var.get()
        pages_value = pages_var.get()
        pages = int(pages_value)
        book_info[book_name] = pages
        
   
    # Create a button to calculate pages per week
    calculate_button = tk.Button(window, text="Calculate Pages per Week", command=lambda: calculate_pages_per_week(week_count,book_count))
    calculate_button.grid(row=9+book_count, columnspan=2)

def calculate_pages_per_week(week_count, book_count):
    i=0
    for book_name, pages in book_info.items():
    
        pages_per_week = float(pages) / week_count
        result_label = tk.Label(window, text=f"{book_name}: {pages_per_week:.2f} pages per week")
        result_label.grid(row=9+i, column=5, columnspan=4)
        i=i+1



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

# Create a button for combined actions
combined_button = tk.Button(window, text="Get Values and Clear", command=get_books_values)
combined_button.grid(row=7, columnspan=2)

window.mainloop()
