import re

expenses=[]

def add_expense(): # adding expenses
    name=input("enter name:\n").strip().lower()
    if not name:
        print("name cannot be empty")
        return
    amount=float(input("enter amount:\n"))
    if amount<=0:
        print("Inavlid amount")
        return
    category=input("enter category:\n").strip().lower()
    if category=="":
        print("Category name cannot be empty")
        return
    date=input("enter date in (DD/MM/YYYY) format:\n")
    pattern=r"^\d{2}/\d{2}/\d{4}$"
    if not re.match(pattern,date):
        print("Invalid date format")
        return

    if len(expenses)==0:
        expense_id=1
    else:
        expense_id=expenses[-1]["id"]+1

    expense={
        "id":expense_id,
        "name":name,
        "amt":amount,
        "category":category,
        "date":date
    }
    expenses.append(expense)

def view_expense():
    if len(expenses)==0:
        print("No expenses")
    for expense in expenses:
        print(
            expense["id"],
            expense["name"],
            expense["amt"],
            expense["category"],
            expense["date"]
        )

def search_expense():
    search=input("enter name:\n").strip().lower()
    found=False
    for expense in expenses:
        if search in expense["name"]:
            print(
             expense["id"],
            expense["name"],
            "₹",expense["amt"],
            expense["category"],
            expense["date"]
            )
            found=True

    if not found:
        print("No matches found")

def filter_category():
    category=input("enter category name:\n").strip().lower()
    found=False

    for expense in expenses:
        if expense["category"]==category:
            print(
                expense["name"],
                "₹",expense["amt"]
            )
            found=True
    if not found:
        print("No matches found")

def calculate_total():
    total=0

    for expense in expenses:
        total+=expense["amt"]
    print("Total expense:₹",total)

def find_highest():
    if len(expenses)==0:
        print("No expenses")

    highest=expenses[0]

    for expense in expenses:
        if expense["amt"]>highest["amt"]:
            highest=expense
            print(
                highest["name"],
                highest["amt"]
            )

def category_analysis():
    category_totals={}

    category = expense["category"]
    amount= expense["amount"]

    for expense in expenses:
        if category in category_totals:
            category_totals["category"]+=amount
        else:
            category_totals[category]=amount

    for category in category_totals:
        print(category,"₹",category_totals[category])

def remove_expense():
    id=int(input("enter id to be removed"))

    for expense in expenses:
        if expense["id"]==id:
            expenses.remove(expense)
            print("removed expense successfully")
            return

    print("No matches found")

def display_summary():
    total=0
    highest=expenses[0]

    for expense in expenses:
        total+=expense["amt"]

        if expense["amt"]>highest["amt"]:
            highest=expense

    average=total/len(expenses)

    print("~~~~~SUMMARY~~~~~~~")
    print("Total expense:₹",total)
    print("no of expenses:",len(expenses))
    print("Highest:",highest["amt"])
    print("Average:₹",average)
    print("Categories:")
    category_analysis()

def main():
    while True:
        print("~~~~~~PERSONAL FINANCE MANAGER~~~~~~~~~")
        print("1.ADD EXPENSE")
        print("2.VIEW EXPENSE")
        print("3.SEARCH EXPENSE")
        print("4.FILTER EXPENSE")
        print("5.CALCULATE TOTAL")
        print("6.FIND HIGHEST")
        print("7.CATEGORY ANALYSIS")
        print("8.REMOVE EXPENSES")
        print("9.EXPENSE SUMMARY")
        print("10.EXIT")

        choice=int(input("enter your choice:\n"))
        match choice:
            case 1:
                add_expense()

            case 2:
                view_expense()

            case 3:
                search_expense()

            case 4:
                filter_category()

            case 5:
                calculate_total()

            case 6:
                find_highest()

            case 7:
                category_analysis()

            case 8:
                remove_expense()

            case 9:
                display_summary()

            case 10:
                print("thank you")
                break

            case _:
                print("invalid choice")


main()