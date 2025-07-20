✅ Lab: Personal Expense Tracker using Python Classes and File Handling
📘 Problem Statement:
You are building a simple command-line based tool that allows users to track their daily expenses, save them to a file, and view summaries.

🎯 Objectives:
✅ Use Python classes to represent expenses
✅ Use file handling (CSV format) to store and retrieve data
✅ Implement a simple CLI menu to interact with the user
✅ Perform basic aggregation (like total by category)

🧱 Concepts Covered:
Python classes and objects

Instance methods

File I/O (open(), read, write)

CSV handling

with statement (context manager)

Basic input validation and error handling (try-except)

Simple menu-based CLI application

🛠️ Tasks to Implement:
🔹 Task 1: Create an Expense class
Attributes: date, category, amount, description

Method: to_csv_row() – returns a list to write to CSV

🔹 Task 2: Define Functions
add_expense() – get input from user and save to expenses.csv

view_expenses() – display all rows from the CSV in tabular form

summary_by_category() – show total spending in each category

🔹 Task 3: Implement CLI Menu
text
Copy
Edit
1. Add New Expense  
2. View All Expenses  
3. View Summary by Category  
4. Exit
Let the user choose what to do.

🔹 Task 4: CSV File Handling
Use the built-in csv module

Append new expenses to the file

Read and process data for display

💡 Bonus Features (Optional):
Validate date using datetime module

Pretty-print tables using tabulate module

Save monthly summaries in a separate file

🖥️ Sample CLI Output:
bash
Copy
Edit
Welcome to Expense Tracker

1. Add Expense
2. View All Expenses
3. View Summary by Category
4. Exit
