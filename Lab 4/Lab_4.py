import csv
from datetime import datetime
from collections import defaultdict
from tabulate import tabulate

# Create a Expense Class
class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.description = description

    def to_csv_row(self):
        return [self.date, self.category, self.amount, self.description]

# Define Functions

def add_expense(filename="expenses.csv"):
    try:
        date_input = input("Enter date (YYYY-MM-DD): ")
        # Validate date
        datetime.strptime(date_input, "%Y-%m-%d")
        
        category = input("Enter category (e.g., Food, Travel): ").strip()
        amount = float(input("Enter amount: "))
        description = input("Enter description: ").strip()

        expense = Expense(date_input, category, amount, description)

        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(expense.to_csv_row())

        print("Expense added successfully!\n")
    except ValueError as e:
        print(f"Error: {e}. Please try again.\n")

def view_expenses(filename="expenses.csv"):
    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded.\n")
                return

            print("\n All Expenses:\n")
            print(tabulate(expenses, headers=["Date", "Category", "Amount", "Description"], tablefmt="pretty"))
            print()
    except FileNotFoundError:
        print("No expenses file found.\n")

def summary_by_category(filename="expenses.csv"):
    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            summary = defaultdict(float)

            for row in reader:
                if len(row) >= 3:
                    category = row[1]
                    amount = float(row[2])
                    summary[category] += amount

            print("\n Expense Summary by Category:\n")
            table = [[cat, amt] for cat, amt in summary.items()]
            print(tabulate(table, headers=["Category", "Total Amount"], tablefmt="fancy_grid"))
            print()
    except FileNotFoundError:
        print("No expenses file found.\n")

# Implement CLI Menu
def main():
    print("Welcome to Expense Tracker\n")
    while True:
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Summary by Category")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summary_by_category()
        elif choice == '4':
            print("Exiting... Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()