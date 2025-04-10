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

# Count of customers based on payment channel
freq_purchase_channel = data2['PaymentMethod'].value_counts()

# Convert the Series to a DataFrame
freq_df = freq_purchase_channel.reset_index()

# Rename the columns
freq_df.columns = ['PaymentMethod', 'Count']

# Print the DataFrame
print("\nFrequency of payments by payment channel as Count:")
print(freq_df)

# Convert to percentage instead of count
perc_freq = freq_purchase_channel/len(data2['PaymentMethod'])*100

# Convert the Series to a DataFrame
perc_df = perc_freq.reset_index()
perc_df.columns = ['PaymentMethod', 'Percentage']
print("\nFrequency of payments by payment channel as a percentage")
print(perc_df)