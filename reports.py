def view_income_report(income_data):
    total_income = sum(item['amount'] for item in income_data)
    print("\nIncome Report")
    print("-------------")
    for item in income_data:
        print(f"Source: {item['source']}, Amount: ${item['amount']}")
    print(f"Total Income: ${total_income}")

def view_expense_report(expense_data):
    total_expenses = sum(item['amount'] for item in expense_data)
    print("\nExpense Report")
    print("--------------")
    for item in expense_data:
        print(f"Category: {item['category']}, Description: {item['description']}, Amount: ${item['amount']}")
    print(f"Total Expenses: ${total_expenses}")

def view_budget_report(budget_data):
    print("\nBudget Report")
    print("-------------")
    for category, amount in budget_data.items():
        print(f"Category: {category}, Budget: ${amount}")

def view_savings_report(savings_data):
    goal = savings_data['goal']
    saved = savings_data['saved']
    print("\nSavings Report")
    print("--------------")
    print(f"Goal: ${goal}")
    print(f"Saved: ${saved}")
    print(f"Remaining: ${goal - saved}")
