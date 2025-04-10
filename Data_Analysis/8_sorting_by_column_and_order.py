import os
import pandas as pd

# Access the data path from the environment variable
data_path = os.getenv('DATA_PATH') or r"C:\Users\wilson.wanderi\Desktop\customer_orders_dataset.xlsx"

# Load your data
data = pd.read_excel(data_path, header=0)
print(data.head()) # To confirm the data is loaded

# Sort data by CustomerID column
sorted_data = data.sort_values(by='CustomerID', ascending=False)

# Print the first 20 records
top_20 = sorted_data.head(20)
print("\nThe Top 20 records after sorting:")
print(top_20)