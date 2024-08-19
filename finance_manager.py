import income
import expenses
import budget
import savings
import reports
import export

def display_menu():
    print("\nPersonal Finance Manager")
    print("1. Manage Income")
    print("2. Manage Expenses")
    print("3. Manage Budget")
    print("4. Track Savings")
    print("5. Generate Reports")
    print("6. Exit")

def manage_income():
    while True:
        print("\nManage Income")
        print("1. Add Income")
        print("2. View Income")
        print("3. Back to Menu")
        choice = input("Enter choice: ")
        if choice == '1':
            source = input("Enter source of income: ")
            amount = float(input("Enter amount: "))
            income.add_income(source, amount)
            print("Income added successfully.")
        elif choice == '2':
            data = income.view_income()
            reports.view_income_report(data)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_expenses():
    while True:
        print("\nManage Expenses")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Back to Menu")
        choice = input("Enter choice: ")
        if choice == '1':
            category = input("Enter expense category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            expenses.add_expense(category, description, amount)
            print("Expense added successfully.")
        elif choice == '2':
            data = expenses.view_expenses()
            reports.view_expense_report(data)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_budget():
    while True:
        print("\nManage Budget")
        print("1. Set Budget")
        print("2. View Budget")
        print("3. Back to Menu")
        choice = input("Enter choice: ")
        if choice == '1':
            category = input("Enter budget category: ")
            amount = float(input("Enter budget amount: "))
            budget.set_budget(category, amount)
            print("Budget set successfully.")
        elif choice == '2':
            data = budget.view_budget()
            reports.view_budget_report(data)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def track_savings():
    while True:
        print("\nTrack Savings")
        print("1. Set Savings Goal")
        print("2. Add to Savings")
        print("3. View Savings")
        print("4. Back to Menu")
        choice = input("Enter choice: ")
        if choice == '1':
            goal = float(input("Enter savings goal: "))
            savings.set_savings_goal(goal)
            print("Savings goal set successfully.")
        elif choice == '2':
            amount = float(input("Enter amount to add to savings: "))
            savings.add_savings(amount)
            print("Savings updated successfully.")
        elif choice == '3':
            data = savings.view_savings()
            reports.view_savings_report(data)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def generate_reports():
    export.export_to_excel()

def exit_program():
    print("Exiting...")
    return True

def invalid_choice():
    print("Invalid choice. Please try again.")
    return False

def main():
    actions = {
        '1': manage_income,
        '2': manage_expenses,
        '3': manage_budget,
        '4': track_savings,
        '5': generate_reports,
        '6': exit_program
    }

    while True:
        display_menu()
        choice = input("Enter choice: ")
        action = actions.get(choice, invalid_choice)
        if action() and choice == '6':
            break

if __name__ == '__main__':
    main()
