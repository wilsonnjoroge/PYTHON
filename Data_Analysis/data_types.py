import pandas as pd

data = pd.read_excel(r"C:\Users\wilson.wanderi\Desktop\customer_orders_dataset.xlsx", header=0)

# See the Data Types
data.dtypes
print("\nData types before correction: Focus on Age")
print(data.dtypes)

unique_age = data['Age'].unique()
print("\nUnique Ages:")
print(unique_age)

# Convert 'Age' to numeric, coercing errors to NaN
data['Age'] = pd.to_numeric(data['Age'], errors='coerce')

# Print unique ages after conversion
print("\nUnique Ages after conversion to Numeric Datatype:")
print(data['Age'].unique())

# Remove inconsistent data: Keep only valid ages (non-null and greater than or equal to 0)
data = data[(data['Age'].notna()) & (data['Age'] >= 0)]

# Print unique ages after removal of inconsistent data
print("\nUnique Ages after removal of inconsistent data:")
print(data['Age'].unique())

# Assign the new data type
data['Age'] = data['Age'].astype(int)

print("\nData types after correction: Focus on Age")
print(data.dtypes)

