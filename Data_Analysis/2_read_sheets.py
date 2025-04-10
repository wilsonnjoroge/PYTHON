import os
import pandas as pd

# Access the data path from the environment variable
data_path = os.getenv('DATA_PATH') or r"C:\Users\wilson.wanderi\Desktop\customer_orders_dataset.xlsx"

# Load your Customers Sheet data
customers_data = pd.read_excel(data_path,sheet_name='Customers', header=0)
print("\nData read from Customers Sheet using Sheet Name:")
print(customers_data.head(20)) # To confirm the data is loaded, read first 20 rows

# Load your Orders Sheet data
orders_data = pd.read_excel(data_path,sheet_name='Orders', header=0)
print("\nData read from Orders Sheet using Sheet Name:")
print(orders_data.head(20)) # To confirm the data is loaded, read first 20 rows

# Load your Products Sheet data
products_data = pd.read_excel(data_path,sheet_name='Products', header=0)
print("\nData read from Products Sheet using Sheet Name:")
print(products_data.head(20)) # To confirm the data is loaded, read first 20 rows
