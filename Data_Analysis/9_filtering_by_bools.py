import os
import pandas as pd

# Access the data path from the environment variable
data_path = os.getenv('DATA_PATH') or r"C:\Users\wilson.wanderi\Desktop\customer_orders_dataset.xlsx"

# Load your data
data = pd.read_excel(data_path, header=0)
print("\nLoaded data head:")
print(data.head())

# Filter by boolean indexing
filtered_data = data[data['Age'] < 25 ]

# Have the data in ascending order
sorted_data = filtered_data.sort_values(by='Age', ascending=False)

# First 20 records from the filtered data
top_20_on_age = sorted_data.head(20)
print("\nFirst 20 records from the filtered data By Age in Descending order:")
print(top_20_on_age)

# Filter based on age and Loyalty tier and have the data in ascending order
filtered_data_2 = data[(data['Age'] < 25) & (data['LoyaltyTier'] == 'Silver')]
sorted_data_2 = filtered_data_2.sort_values(by='Age', ascending=False)

# First 20 records from the filtered data
top_20_on_age_and_loyalty = sorted_data_2.head(20)
print("\nFirst 20 records from the filtered data By Age and LoyaltyTier(Silver) in Descending order:")
print(top_20_on_age_and_loyalty)
