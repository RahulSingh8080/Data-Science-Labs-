from db_connection import fetch_sales_data
from report_builder import build_html_report
from email_sender import send_email
from datetime import datetime

def run_pipeline():
    print("Running Sales Report Pipeline...")
    data = fetch_sales_data()
    if not data:
        print("No data found for yesterday.")
        return
    
    report = build_html_report(data)
    subject = f"Daily Sales Report  {datetime.now().strftime('%d %B %Y')}"
    send_email(subject, report)

if __name__ == "__main__":
    run_pipeline()
    