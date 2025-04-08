import pandas as pd
from sklearn.impute import SimpleImputer

data = pd.read_excel(r"C:\Users\wilson.wanderi\Desktop\customer_orders_dataset.xlsx", header=0)

# Identify missing values
missing_values = data.isnull().sum()
print("Missing Values:")
print(missing_values)

# Replacing missing values
# Define columns for imputation
numerical_columns = ['Age', 'PurchaseAmount', 'NumPurchases', 'AvgPurchaseValue']
categorical_columns = ['Name', 'Country', 'Gender', 'SatisfactionScore', 'Email', 'LoyaltyTier', 'Category']

# Create imputers
numerical_imputer = SimpleImputer(strategy='median')
categorical_imputer = SimpleImputer(strategy='most_frequent')

# Fit and transform numerical columns
data[numerical_columns] = numerical_imputer.fit_transform(data[numerical_columns])

# Fit and transform categorical columns
data[categorical_columns] = categorical_imputer.fit_transform(data[categorical_columns])

# Display the DataFrame after imputation
print("\nData after imputation:")
print(data)

# Optionally, check for any remaining missing values
print("\nRemaining Missing Values:")
print(data.isnull().sum())