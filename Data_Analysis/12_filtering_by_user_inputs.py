import os
import pandas as pd

# Access the data path from the environment variable
data_path = os.getenv('DATA_PATH') or r"C:\Users\wilson.wanderi\Desktop\customer_orders_dataset.xlsx"

# Load your data
data = pd.read_excel(data_path, header=0)
print(data.head())

# Get user input
age_input = int(input("Enter the age: "))
operation = input("Enter the operation (>, <): ").strip().lower()
loyalty_tier_input = input("Enter the loyalty tier (e.g., Silver, Gold, Bronze): ").strip()

# Construct the query based on user input
if operation == "<":
    query_string = f'Age < {age_input} & LoyaltyTier == "{loyalty_tier_input}"'
elif operation == ">":
    query_string = f'Age > {age_input} & LoyaltyTier == "{loyalty_tier_input}"'
else:
    print("Invalid operation. Please use 'less than' or 'greater than'.")
    query_string = None

# Filter the data if the query string is valid
if query_string:
    filtered_data = data.query(query_string)
    print("\nFiltered records:")
    print(filtered_data)
