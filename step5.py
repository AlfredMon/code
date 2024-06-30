import tkinter as tk
window = tk.Tk()
window.title("Book Pages Calculator")

def collect_book_info():
    for i in range(book_count - 1):
        popup = tk.Toplevel(window)  # Create a modal dialog
        popup.title(f"Book {i + 1} Info")

        book_name_label = tk.Label(popup, text=f"Enter Book Name {i + 1}:")
        book_name_label.pack()
        book_name_entry = tk.Entry(popup)
        book_name_entry.pack()

        pages_label = tk.Label(popup, text="Enter Number of Pages:")
        pages_label.pack()
        pages_entry = tk.Entry(popup)
        pages_entry.pack()

        done_button = tk.Button(popup, text="DONE", command=popup.destroy)
        done_button.pack()

        popup.wait_window(popup)  # Wait for user input
        def store_info():
            book_name = book_name_entry.get()
            pages_value = pages_entry.get()
            pages = int(pages_value)
            book_info[book_name] = pages

root = tk.Tk()
book_count = 5  # Adjust as needed
book_info = {}  # Dictionary to store book info

collect_book_info()  # Call the function to collect book info

# Your other tkinter setup and main loop here
root.mainloop()
