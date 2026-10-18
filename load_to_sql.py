import pandas as pd
import sqlite3

# 1. Read the cleaned CSV file
clean_orders = pd.read_csv('raw_data/cleaned_orders.csv')

# 2. Connect to a new SQLite database (this will create a file named 'ecommerce.db')
conn = sqlite3.connect('ecommerce.db')

# 3. Load the dataframe into a SQL table named 'orders'
# If the table already exists, it will replace it.
clean_orders.to_sql('orders', conn, if_exists='replace', index=False)

# 4. Verify the data was loaded by writing our first SQL query!
print("--- Testing SQL Connection ---")
query = "SELECT count(*) AS total_clean_orders FROM orders;"
result = pd.read_sql(query, conn)
print(result)

# Close the database connection
conn.close()
print("\nSuccess! Data loaded into SQLite database 'ecommerce.db'")