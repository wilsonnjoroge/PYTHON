import os
import pandas as pd

# Access the data path from the environment variable
data_path = os.getenv('DATA_PATH') or r"C:\Users\wilson.wanderi\Desktop\customer_orders_dataset.xlsx"

# Load your data
data = pd.read_excel(data_path, header=0)
print("\nLoaded data head:")
print(data.head())

# Slice with loc to see the first 20 rows for columns between CustomerID and Category
data_loc = data.loc[0:20, 'CustomerID' : 'Category'] # use the exact column names 
print("\nFirst 20 rows for columns: CustomerID to Category using loc:")
print(data_loc)

# Slice with iloc to see the first 20 rows for columns between CustomerID and Category
data_iloc = data.iloc[0:20, 0:7] # column with i[7] will be left out
print("\nFirst 20 rows for columns: CustomerID to Category using iloc:")
print(data_iloc)