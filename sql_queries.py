import pandas as pd
import sqlite3

# Connect to your existing database
conn = sqlite3.connect('ecommerce.db')

# 1. Load the customers dataset into the database
print("Loading customers data into the database...")
customers_df = pd.read_csv('raw_data/olist_customers_dataset.csv')
customers_df.to_sql('customers', conn, if_exists='replace', index=False)

# 2. Write our first Advanced SQL Query
# Business Question: Which top 5 cities have the highest number of successfully delivered orders?
query = """
SELECT 
    c.customer_city, 
    COUNT(o.order_id) AS total_orders
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_city
ORDER BY total_orders DESC
LIMIT 5;
"""

# 3. Execute the SQL query and print the result
print("\nExecuting SQL JOIN query...\n")
top_cities = pd.read_sql(query, conn)

print("--- Top 5 Cities by Delivered Orders ---")
print(top_cities)

# Close the connection
conn.close()