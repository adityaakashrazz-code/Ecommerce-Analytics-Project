import pandas as pd
import sqlite3

# Connect to the database
conn = sqlite3.connect('ecommerce.db')

# 1. Load the payments dataset
print("Loading payments data into the database...")
payments_df = pd.read_csv('raw_data/olist_order_payments_dataset.csv')
payments_df.to_sql('payments', conn, if_exists='replace', index=False)

# 2. Advanced SQL Query: CTE and Window Function
# Business Question: What is the monthly revenue, and what is the running total of revenue over time?
query = """
WITH MonthlyRevenue AS (
    SELECT 
        strftime('%Y-%m', o.order_purchase_timestamp) AS order_month,
        SUM(p.payment_value) AS monthly_revenue
    FROM orders o
    JOIN payments p ON o.order_id = p.order_id
    GROUP BY order_month
    HAVING order_month IS NOT NULL
)
SELECT 
    order_month,
    ROUND(monthly_revenue, 2) AS monthly_revenue,
    ROUND(SUM(monthly_revenue) OVER (ORDER BY order_month), 2) AS running_total_revenue
FROM MonthlyRevenue
ORDER BY order_month;
"""

print("\nExecuting CTE and Window Function query...\n")
revenue_trends = pd.read_sql(query, conn)

print("--- Monthly Revenue & Running Total ---")
print(revenue_trends.head(10)) # Printing the first 10 months to keep the terminal clean


# Export the result to a CSV file for Power BI / Tableau
revenue_trends.to_csv('raw_data/dashboard_revenue_trends.csv', index=False)
print("Dashboard data exported successfully as 'dashboard_revenue_trends.csv'!")


conn.close()