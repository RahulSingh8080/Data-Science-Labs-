# ✅ Lab: Automated Daily Sales Report Pipeline (SQL Server → Python → Email)

## 📘 Problem Statement

You are working in a company where daily sales data is stored in a **SQL Server database**.  
Your task is to build an automated Python pipeline that:

- Connects to SQL Server and fetches the previous day's sales
- Formats that data as a report list/table
- Sends the report via email every day at **8:00 AM** automatically

---

## 🎯 Objectives

- Connect SQL Server from Python using `pyodbc` or `sqlalchemy`
- Automate SQL queries and extract raw data
- Format result into a list or HTML table using `pandas` or `tabulate`
- Send email using `smtplib` or `yagmail`
- Schedule the task to run daily using `schedule` or Windows Task Scheduler

---

## 🛠️ Tech Stack & Concepts Covered

| Concept             | Tool/Module              |
|---------------------|--------------------------|
| SQL Server Access   | `pyodbc`, `sqlalchemy`   |
| Data Processing     | `pandas`, `datetime`     |
| Email Sending       | `smtplib`, `email.mime`  |
| Automation          | `schedule`, `time`, `cron` |
| Error Handling      | `try-except` blocks      |

---

## 📦 Sample Output

### 🐍 Python Output

```python
[
    {'Date': '2025-07-20', 'Product': 'Laptop', 'Qty': 5, 'Amount': 250000},
    {'Date': '2025-07-20', 'Product': 'Phone', 'Qty': 10, 'Amount': 150000}
]
📧 Email Body

Subject: 📊 Daily Sales Report – 20 July 2025

Date        | Product   | Qty | Amount
---------------------------------------
2025-07-20  | Laptop    | 5   | ₹250000
2025-07-20  | Phone     | 10  | ₹150000

sales_report_pipeline/
│
├── config.py          # DB config & email credentials
├── db_connection.py   # SQL query logic
├── report_builder.py  # Transform SQL result to report
├── email_sender.py    # Email logic
├── scheduler.py       # Scheduling logic
└── main.py            # Main runner script
