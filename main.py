from expense import add_expense, view_expenses, delete_expense, monthly_total, edit_expense, category_summary

def show_menu():
    print("\n=== STUDENT EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Delete Expense")
    print("4. Edit Expense")
    print("5. Show Monthly Total")
    print("6. Category Summary")
    print("7. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            edit_expense()
        elif choice == "5":
            monthly_total()
        elif choice == "6":
            category_summary()
        elif choice == "7":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
