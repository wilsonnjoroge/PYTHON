import pandas as pd
import os

# Access the data path from the environment variable
data_path = os.getenv('DATA_PATH') or r"C:\Users\wilson.wanderi\Desktop\customer_orders_dataset.xlsx"

# Load your data
data = pd.read_excel(data_path, header=0)

###########################
# Find the unique values per Country
unique_country_values = data['Country'].unique()
print("\nUnique Country values before replacement:")
print(unique_country_values)

# Drop the Country inconsistent data
data = data[(data['Country'].notna()) & (data['Country'] != '123')]
print("\nUnique Country values after dropping:")
print(data['Country'].unique())

# Find the unique values per Gender
unique_gender_values = data['Gender'].unique()
print("\nUnique Gender values before replacement:")
print(unique_gender_values)

# Drop the Country inconsistent data
data = data[(data['Gender'].notna() & (data['Gender'] != 'Unknown'))]
print("\nUnique Gender values after dropping:")
print(data['Gender'].unique())

print(data.dtypes)