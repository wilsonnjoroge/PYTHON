import os
import pandas as pd

# Access the data path from the environment variable
data_path = os.getenv('DATA_PATH') or r"C:\Users\wilson.wanderi\Desktop\customer_orders_dataset.xlsx"

# Load your data
data = pd.read_excel(data_path, header=0)
print("\nLoaded data head:")
print(data.head())

# Check if there are duplicates
duplicates = data.duplicated()
print("\nDuplicates in the data:")
print(duplicates)

# Drop duplicates
data.drop_duplicates(inplace= True)
print("\nAfter removing duplicates from the data:")
print(duplicates)