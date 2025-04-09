import os
import pandas as pd

# Access the data path from the environment variable
data_1_path = os.getenv('DATA_PATH') or r"C:\Users\wilson.wanderi\Desktop\customer_orders_dataset.xlsx"
data_2_path = os.getenv('DATA_PATH2') or r"C:\\Users\\wilson.wanderi\\Desktop\\Bank+Churn+Data-Solution.xlsx"
# Load your data
data1 = pd.read_excel(data_1_path, sheet_name='Customers', header=0)
data2 = pd.read_excel(data_1_path,sheet_name='Orders', header=0)

print("\nLoaded data1 (Customers sheet) head:")
print(data1.head())

print("\nLoaded data2 (Orders sheet) head:")
print(data2.head())

# Inner joins
inner_join_on_customerid = pd.merge(data1,data2, on='CustomerID', how='inner')
print("\nInner join on CustomerID column between Customers and Orders sheets:")
print(inner_join_on_customerid)