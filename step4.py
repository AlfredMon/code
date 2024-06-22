import tkinter as tk

# Initialize an empty dictionary to store book information
book_info = {}

def get_values_and_clear():
    # Get values from input fields
    book_count = int(input_box1.get())
    week_count = int(input_box2.get())
    study_time = int(input_box3.get())

    # Clear the input fields
    input_box1.delete(0, tk.END)
    input_box2.delete(0, tk.END)
    input_box3.delete(0, tk.END)

    # Create entry fields for book names and pages
    for i in range(book_count):
        book_name_label = tk.Label(window, text=f"Enter Book Name {i+1}:")
        book_name_label.grid(row=9+i, column=0)
        book_name_entry = tk.Entry(window)
        book_name_entry.grid(row=9+i, column=1)

        pages_label = tk.Label(window, text="Enter Number of Pages:")
        pages_label.grid(row=9+i, column=2)
        pages_entry = tk.Entry(window)
        pages_entry.grid(row=9+i, column=3)

        # Store book information in the dictionary
        book_info[book_name_entry] = pages_entry

    # Create a button to calculate pages per week
    calculate_button = tk.Button(window, text="Calculate Pages per Week", command=calculate_pages_per_week)
    calculate_button.grid(row=9+book_count, columnspan=2)

def calculate_pages_per_week():
    for book_name, pages in book_info.items():
        try:
            total_pages = int(pages.get())
            pages_per_week = total_pages / week_count
            result_label = tk.Label(window, text=f"{book_name.get()}: {pages_per_week:.2f} pages per week")
            result_label.grid(row=9+book_count, column=0, columnspan=4)
        except ValueError:
            print(f"Invalid input for {book_name.get()} pages. Please enter a valid number.")

window = tk.Tk()
window.geometry("1000x1000")

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

window.mainloop()
