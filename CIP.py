import json

def load_plan():
    try:
        with open('study_plan.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("No previous study plan found.")
        return None

def book_details(books=None):
    if books is None:
        books = {}
    while True:
        title = input("Enter the book title (or 'quit' to stop): ")
        if title.lower() == 'quit':
            break
        pages = int(input("Enter the number of pages in the book: "))
        time_to_read_10_pages = float(input("Enter how long (in hours) it takes to read 10 pages: "))
        books[title] = {'pages': pages, 'time_to_read_10_pages': time_to_read_10_pages}
    return books

def edit_book_details(books):
    while True:
        title = input("Enter the title of the book you want to edit (or 'quit' to stop): ")
        if title.lower() == 'quit':
            break
        if title not in books:
            print("This book is not in your list. Please try again.")
            continue
        print("Current details: ", books[title])
        new_pages = int(input("Enter the new number of pages for the book: "))
        new_time_to_read_10_pages = float(input("Enter the new time (in hours) it takes to read 10 pages: "))
        books[title] = {'pages': new_pages, 'time_to_read_10_pages': new_time_to_read_10_pages}
    return books

def delete_book(books):
    while True:
        title = input("Enter the title of the book you want to delete (or 'quit' to stop): ")
        if title.lower() == 'quit':
            break
        if title not in books:
            print("This book is not in your list. Please try again.")
            continue
        del books[title]
    return books

def study_plan(books, days, max_hours, min_hours, off_days):
    study_days = days - (days // 7) * off_days
    plan = {}
    total_hours = 0
    for title, book in books.items():
        pages_per_day = book['pages'] / study_days
        hours_per_day = (pages_per_day / 10) * book['time_to_read_10_pages']
        total_hours += hours_per_day
        plan[title] = {'pages_per_day': pages_per_day, 'hours_per_day': hours_per_day}
    
    if total_hours > max_hours:
        extra_days = total_hours / max_hours
        new_deadline = days + extra_days
        print(f"Warning: Your study plan requires {total_hours} hours of study per day, which exceeds your specified maximum of {max_hours} hours. You should consider increasing the number of study days to approximately {new_deadline}.")
    elif total_hours < min_hours:
        less_days = days * (min_hours / total_hours)
        new_deadline = days - less_days
        new_hours = total_hours * (days / new_deadline)
        print(f"Note: Your study plan requires only {total_hours} hours of study per day, which is less than your specified minimum of {min_hours} hours. You have two options:")
        print(f"1. Decrease the number of study days to approximately {new_deadline}, which will increase your daily study hours to {new_hours}.")
        print(f"2. Increase your daily study hours to {min_hours}, which will keep your study days as {days}.")
    return plan

def save_plan(plan):
    with open('study_plan.json', 'w') as f:
        json.dump(plan, f)
    print("Your study plan has been saved to 'study_plan.json'.")

# Call the functions
plan = load_plan()
if plan is None:
    books = book_details()
    days = int(input("Enter the number of days you want to study: "))
    max_hours = float(input("Enter the maximum number of hours you can study in a single day (not exceeding 14 hours): "))
    min_hours = float(input("Enter the minimum number of hours you can study in a single day: "))
    off_days = int(input("Enter the number of off days in a week: "))
    plan = study_plan(books, days, max_hours, min_hours, off_days)

while True:
    print("What would you like to do next?")
    print("1. Edit the books and recalculate the study plan")
    print("2. Change the study hours per day")
    print("3. Change the deadline")
    print("4. Change the number of off days in a week")
    print("5. Save and exit")
    option = int(input("Enter the number of your option: "))
    if option == 1:
        books = edit_book_details(books)
        plan = study_plan(books, days, max_hours, min_hours, off_days)
    elif option == 2:
        max_hours = float(input("Enter the new maximum number of hours you can study in a single day (not exceeding 14 hours): "))
        min_hours = float(input("Enter the new minimum number of hours you can study in a single day: "))
        plan = study_plan(books, days, max_hours, min_hours, off_days)
    elif option == 3:
        days = int(input("Enter the new number of days you want to study: "))
        plan = study_plan(books, days, max_hours, min_hours, off_days)
    elif option == 4:
        off_days = int(input("Enter the new number of off days in a week: "))
        plan = study_plan(books, days, max_hours, min_hours, off_days)
    elif option == 5:
        save_plan(plan)
        break
    else:
        print("Invalid option. Please try again.")
