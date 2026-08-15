def add_expense(expenses: list, name: str, amount: float, category: str) -> None:
    """
    Creates a expense list and adds the items into it by appending. 
    """
    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    print("\nExpense added!")


def view_expenses(expenses: list) -> None:
    """
    Displays the expenses.
    """
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for exp in expenses:
        print("Name:", exp["name"], "| Amount: ₹", exp["amount"], "| Category:", exp["category"])


def calculate_total(expenses: list) -> float:
    """
    Calculates and returns the total sum of all expenses.
    """
    total = 0.0
    for exp in expenses:
        total += exp["amount"]
    return total


def find_highest_expense(expenses: list) -> dict:
    """
    Finds and returns the expense dictionary with the maximum amount.
    """
    if not expenses:
        return {}

    highest = expenses[0]
    for exp in expenses:
        if exp["amount"] > highest["amount"]:
            highest = exp
    return highest


def filter_by_category(expenses: list, category: str) -> list:
    """
    Filters and returns a list of expenses matching a specific category.
    """
    filtered_list = []
    for exp in expenses:
        if exp["category"].lower() == category.lower():
            filtered_list.append(exp)
    return filtered_list


def main() -> None:
    """
    The main driver function that handles the menu system and user inputs.
    """
    all_expenses = []

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Highest Expense")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            name = input("Expense name: ")
            amount = float(input("Amount: "))
            category = input("Category: ")
            add_expense(all_expenses, name, amount, category)

        elif choice == "2":
            view_expenses(all_expenses)

        elif choice == "3":
            total = calculate_total(all_expenses)
            print("\nTotal Expenses: ₹", total)

        elif choice == "4":
            highest = find_highest_expense(all_expenses)
            if not highest:
                print("\nNo expenses recorded yet.")
            else:
                print("\nHighest Expense Details:")
                print("Name:", highest["name"], "| Amount: ₹", highest["amount"], "| Category:", highest["category"])

        elif choice == "5":
            search = input("Enter category to search: ")
            results = filter_by_category(all_expenses, search)
            if not results:
                print("\nNo expenses found in this category.")
            else:
                print("\n--- Expenses in Category:", search, "---")
                for exp in results:
                    print("Name:", exp["name"], "| Amount: ₹", exp["amount"])

        elif choice == "6":
            print("\nExiting.....")
            break

        else:
            print("\nInvalid choice! Please select between 1 and 6.")


main()