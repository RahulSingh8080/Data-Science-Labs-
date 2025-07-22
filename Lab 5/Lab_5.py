import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aditi@77",
    database="sys"
)

query = "SELECT * FROM SalesReport"
df = pd.read_sql(query, conn)

print(df.head())  
