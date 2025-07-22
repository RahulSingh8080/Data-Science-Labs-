✅ Lab: Automated Daily Sales Report Pipeline (SQL Server → Python → Email)
📘 **Problem Statement:
You are working in a company where daily sales data is stored in a SQL Server database.**
Your task is to build an automated Python pipeline that:

Connects to SQL Server and fetches the previous day's sales

Formats that data as a report list/table

Sends the report via email every day at 8:00 AM automatically

🎯 Objectives:
Connect SQL Server from Python using pyodbc or sqlalchemy

Automate SQL queries and extract raw data

Format result into a list or HTML table using pandas or tabulate

Send email using smtplib or yagmail

Schedule the task to run daily using schedule or Windows Task Scheduler

🛠️ Tech Stack & Concepts Covered:
Concept	Tool/Module
SQL Server Access	pyodbc or sqlalchemy
Data Processing	pandas, datetime
Email Sending	smtplib, email.mime
Automation	schedule, time, or cron (Linux)
Error Handling	try-except blocks

📦 Sample Output:
python
Copy
Edit
[
    {'Date': '2025-07-20', 'Product': 'Laptop', 'Qty': 5, 'Amount': 250000},
    {'Date': '2025-07-20', 'Product': 'Phone', 'Qty': 10, 'Amount': 150000}
]
Email body:

yaml
Copy
Edit
Subject: 📊 Daily Sales Report – 20 July 2025

Date        | Product   | Qty | Amount
---------------------------------------
2025-07-20  | Laptop    | 5   | ₹250000
2025-07-20  | Phone     | 10  | ₹150000
⏰ Daily Execution:
Use Python’s schedule module:

python
Copy
Edit
import schedule
schedule.every().day.at("08:00").do(run_report_pipeline)
Or use Windows Task Scheduler / Linux cron job to call the script daily at 8:00 AM.

✅ Project Structure:
graphql
Copy
Edit
sales_report_pipeline/
│
├── config.py          # DB config & email credentials
├── db_connection.py   # SQL query logic
├── report_builder.py  # Transform SQL result to report
├── email_sender.py    # Email logic
├── scheduler.py       # Scheduling logic
└── main.py            # Main runner script
🔐 Security Tips:
Store email & DB passwords in .env file or keyring

Don’t hard-code sensitive data

🧠 Bonus Enhancements:
Attach report as Excel file using xlsxwriter

Save reports daily to a folder

Add retry logic in case of failure

✅ Real-World Use Cases:
Daily Sales Reports to Managers

Automated Inventory Alerts

Scheduled Customer Follow-up Lists

DataOps Monitoring Pipelines
