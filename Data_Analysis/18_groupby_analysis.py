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

# Find Average Age of Customers based on Loyalty Tier
average_age_silver_cust = data1.groupby('LoyaltyTier')['Age'].mean()
rounded_off_date = round(average_age_silver_cust, 2)

# Convert to a Data Frame
average_age_silver_cust_df = rounded_off_date.reset_index()
average_age_silver_cust_df.columns = ['Loyalty Tier', 'Average Age']
print("\nAverage Age of Customers based on Loyalty Tier:")
print(average_age_silver_cust_df)