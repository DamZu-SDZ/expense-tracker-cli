from storage import load_data, save_data
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        # Load data dari JSON bila class dibuat
        self.data = load_data()

    def add_expense(self):
        category = input("Enter category: ")
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount. Try again.")
            return
        description = input("Enter description: ")
        expense = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "category": category,
            "amount": amount,
            "description": description
        }
        self.data.append(expense)
        save_data(self.data)
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.data:
            print("No expenses found.")
            return
        for i, e in enumerate(self.data):
            print(f"{i}. {e['date']} | {e['category']} | RM{e['amount']} | {e['description']}")

    def delete_expense(self):
        if not self.data:
            print("No expenses to delete.")
            return
        self.view_expenses()
        try:
            index = int(input("Enter index to delete: "))
        except ValueError:
            print("Invalid input.")
            return
        if 0 <= index < len(self.data):
            deleted = self.data.pop(index)
            save_data(self.data)
            print("Deleted:", deleted)
        else:
            print("Invalid index.")

    def edit_expense(self):
        if not self.data:
            print("No expenses to edit.")
            return
        self.view_expenses()
        try:
            index = int(input("Enter index to edit: "))
        except ValueError:
            print("Invalid input.")
            return
        if 0 <= index < len(self.data):
            e = self.data[index]
            new_category = input(f"New category ({e['category']}): ") or e['category']
            try:
                new_amount_input = input(f"New amount ({e['amount']}): ")
                new_amount = float(new_amount_input) if new_amount_input else e['amount']
            except ValueError:
                print("Invalid amount.")
                return
            new_description = input(f"New description ({e['description']}): ") or e['description']
            e['category'] = new_category
            e['amount'] = new_amount
            e['description'] = new_description
            save_data(self.data)
            print("Expense updated successfully!")
        else:
            print("Invalid index.")

    def category_summary(self):
        if not self.data:
            print("No expenses found.")
            return
        summary = {}
        for e in self.data:
            summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]
        print("\n=== Category Summary ===")
        for cat, total in summary.items():
            print(f"{cat}: RM{total}")
