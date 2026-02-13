from storage import load_data, save_data
from datetime import datetime

def add_expense():
    data = load_data()

    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    description = input("Enter description: ")

    expense = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "category": category,
        "amount": amount,
        "description": description
    }

    data.append(expense)
    save_data(data)

    print("Expense added successfully!")

def view_expenses():
    data = load_data()

    if not data:
        print("No expenses found.")
        return

    for i, expense in enumerate(data):
        print(f"{i}. {expense['date']} | {expense['category']} | RM{expense['amount']} | {expense['description']}")

def delete_expense():
    data = load_data()

    if not data:
        print("No expenses to delete.")
        return

    view_expenses()

    try:
        index = int(input("Enter expense index to delete: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if 0 <= index < len(data):
        deleted = data.pop(index)
        save_data(data)
        print("Deleted:", deleted)
    else:
        print("Invalid index.")

def monthly_total():
    data = load_data()

    month = input("Enter month (YYYY-MM): ")
    total = 0

    for expense in data:
        if expense["date"].startswith(month):
            total += expense["amount"]

    print(f"Total for {month}: RM{total}")


def edit_expense():
    data = load_data()

    if not data:
        print("No expenses to edit.")
        return

    view_expenses()

    try:
        index = int(input("Enter expense index to edit: "))
    except ValueError:
        print("Invalid input.")
        return

    if 0 <= index < len(data):
        expense = data[index]

        new_category = input(f"New category ({expense['category']}): ") or expense['category']

        try:
            new_amount_input = input(f"New amount ({expense['amount']}): ")
            new_amount = float(new_amount_input) if new_amount_input else expense['amount']
        except ValueError:
            print("Invalid amount.")
            return

        new_description = input(f"New description ({expense['description']}): ") or expense['description']

        expense['category'] = new_category
        expense['amount'] = new_amount
        expense['description'] = new_description

        save_data(data)
        print("Expense updated successfully!")
    else:
        print("Invalid index.")

def category_summary():
    data = load_data()

    if not data:
        print("No expenses found.")
        return

    summary = {}

    for expense in data:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]

    print("\n=== Category Summary ===")
    for category, total in summary.items():
        print(f"{category}: RM{total}")
