


print("Welcome to my finance tracker application!")


expenses = []

def add_expense():
    expense_num = float(input("How much does this cost? "))
    expense_cat = input("What category is this expense? ")
    expense_desc = input("Add a description for this expense: ")
    expense = {
                "amount": expense_num, 
               "category": expense_cat, 
               "description": expense_desc
            }
    expenses.append(expense)
    print("Expense has been added!")
def view_expenses():
    if not expenses:
        print("There are no expenses recorded.")
        return
    print("--------------------------------------")
    for expense in expenses:
        print(f"{expense["category"]} - ${expense["amount"]} description: {expense["description"]}")
    print("--------------------------------------")
def total_spent():
    if not expenses:
        print("There are no expenses recorded")
        return
    totalamt = 0
    for expense in expenses:
        totalamt = expense["amount"] + totalamt
    print(f"You total amount spent is {totalamt}")
def category_filter():
    catsearch = input("Hhat category would you like to search?")
    for expense in expenses:
        if catsearch == expense["category"]:
            print(f"{expense["category"]} - ${expense["amount"]} description: {expense["description"]}")



while True:
    choice = int(input("What action would you like to choose? \n 1. Add expense \n 2. View Expenses \n 3. Total Spent \n 4. Filter by category \n 5. Exit \n Choose a number: "))
    
    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        total_spent()
    elif choice == 4:
        category_filter()
    elif choice == 5:
        print("Expenses are all tracked!")
        break
    else:
        print("Invalid Option")