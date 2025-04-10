import os
import pandas as pd

# Access the data path from the environment variable
data_path = os.getenv('DATA_PATH') or r"C:\Users\wilson.wanderi\Desktop\customer_orders_dataset.xlsx"
# Load your data
data1 = pd.read_excel(data_path, sheet_name='Customers', header=0)
data2 = pd.read_excel(data_path,sheet_name='Orders', header=0)

print("\nLoaded data1 (Customers sheet) head:")
print(data1.head())

print("\nLoaded data2 (Orders sheet) head:")
print(data2.head())

# Describe the Customers Data
cust_data_description = round(data1.describe(),2) # Round off to minimize decimal points to 2
print("\nDescriptive analysis of Customer Data:")
print(cust_data_description)

# Describe the Orders Data
order_data_description = round(data2.describe(),2) # Round off to minimize decimal points to 2
print("\nDescriptive analysis of Order Data:")
print(order_data_description)