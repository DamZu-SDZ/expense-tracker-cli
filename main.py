from expense import ExpenseTracker

tracker = ExpenseTracker()

def show_menu():
    print("\n=== STUDENT EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Delete Expense")
    print("4. Edit Expense")
    print("5. Category Summary")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose (1-6): ")
        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.delete_expense()
        elif choice == "4":
            tracker.edit_expense()
        elif choice == "5":
            tracker.category_summary()
        elif choice == "6":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
