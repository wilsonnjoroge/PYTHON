import os
import pandas as pd

# Access the data path from the environment variable
data_path = os.getenv('DATA_PATH') or r"C:\Users\wilson.wanderi\Desktop\customer_orders_dataset.xlsx"

# Load your data
data = pd.read_excel(data_path, header=0)
print("\nLoaded data head:")
print(data.head())

# Filter the data on age 
filtered_data = data.query('Age < 25')

# Sort the data on age in descending order
sorted_data_1 = filtered_data.sort_values(by='Age', ascending=False)
print("\nSorted the data on age in descending order:")
print(sorted_data_1)

# Print the first 20 records
top_20_by_age = sorted_data_1.head(20)
print("\nThe first 20 records on age in descending order")
print(top_20_by_age)

# Filter the data on age and Loyalty Tier
filtered_data_2 = data.query('Age < 25 & LoyaltyTier == "Silver"')

# Sort the data on age and Loyalty Tier in descending order
sorted_data_2 = filtered_data_2.sort_values(by='Age', ascending=False)
print("\nSorted the data on age and LoyaltyTier(Silver) in descending order:")
print(sorted_data_2)