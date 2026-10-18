#---------STEP-1----- 
#-------------------FIND--MISSING--VALUE---


# import pandas as pd

# # CSV files ko read karna
# orders_df = pd.read_csv('raw_data/olist_orders_dataset.csv')
# customers_df = pd.read_csv('raw_data/olist_customers_dataset.csv')

# # Dataset ki basic information check karna
# print("--- Orders Table Info ---")
# print(orders_df.info()) 

# print("\n--- Orders Table Missing Values ---")
# print(orders_df.isnull().sum())



#------STEP--2--------



# import pandas as pd

# # 1. Load the data
# orders_df = pd.read_csv('raw_data/olist_orders_dataset.csv')

# # 2. Convert text columns to actual datetime objects
# date_columns = [
#     'order_purchase_timestamp', 'order_approved_at', 
#     'order_delivered_carrier_date', 'order_delivered_customer_date', 
#     'order_estimated_delivery_date'
# ]

# for col in date_columns:
#     orders_df[col] = pd.to_datetime(orders_df[col])

# print("Data types after conversion:")
# print(orders_df.dtypes)

# # 3. Investigate the missing delivery dates
# missing_delivery = orders_df[orders_df['order_delivered_customer_date'].isnull()]

# print("\n--- Status of Orders with Missing Delivery Dates ---")
# print(missing_delivery['order_status'].value_counts())





#-----------STEP--3------------


import pandas as pd

# 1. Load the raw data
orders_df = pd.read_csv('raw_data/olist_orders_dataset.csv')

# 2. Convert text columns to actual datetime objects
date_columns = [
    'order_purchase_timestamp', 'order_approved_at', 
    'order_delivered_carrier_date', 'order_delivered_customer_date', 
    'order_estimated_delivery_date'
]
for col in date_columns:
    orders_df[col] = pd.to_datetime(orders_df[col])

# 3. Filter the data based on Business Logic
# Keep ONLY orders that have a status of 'delivered'
clean_orders = orders_df[orders_df['order_status'] == 'delivered'].copy()

# 4. Handle the Anomalies
# Drop those 8 specific rows where delivery date is still missing
clean_orders.dropna(subset=['order_delivered_customer_date'], inplace=True)

# 5. Save the cleaned dataset to a new CSV file
clean_orders.to_csv('raw_data/cleaned_orders.csv', index=False)

print(f"Original row count: {len(orders_df)}")
print(f"Cleaned row count: {len(clean_orders)}")
print("Cleaned dataset saved successfully as 'cleaned_orders.csv'!")
























































































































