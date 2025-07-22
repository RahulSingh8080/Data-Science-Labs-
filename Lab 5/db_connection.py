import mysql.connector
from config import DB_CONFIG
from datetime import datetime, timedelta

def fetch_sales_data():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)

    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    query = """
        SELECT Date, Category, Amount, Description, EmailID, Status, Campaign
        FROM SalesReport
        WHERE Date = %s
    """
    cursor.execute(query, (yesterday,))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows