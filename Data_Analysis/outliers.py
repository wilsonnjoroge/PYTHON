
import pandas as pd # type: ignore
import numpy as np # type: ignore
import os

# Access the data path from the environment variable
data_path = os.getenv('DATA_PATH') or r"C:\Users\wilson.wanderi\Desktop\customer_orders_dataset.xlsx"

# Load your data
data = pd.read_excel(data_path, header=0)

final_data = pd.DataFrame(data)

########################################################
# Method 1
# Calculate the Z-scores
mean = final_data['purchase'].mean()
std_dev = final_data['purchase'].std()
final_data['z_score'] = (final_data['purchase'] - mean) / std_dev

# Identify outliers (Z-score > 3 or < -3)
outliers = final_data[final_data['z_score'].abs() > 3]
print(outliers)


########################################################
# Method 2
# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = final_data['purchase'].quantile(0.25)
Q3 = final_data['purchase'].quantile(0.75)
IQR = Q3 - Q1

# Define the bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = final_data[(final_data['purchase'] < lower_bound) | (final_data['purchase'] > upper_bound)]
print(outliers)

########################################################
# Method 3
import matplotlib.pyplot as plt # type: ignore

# Create a box plot
plt.boxplot(final_data['purchase'])
plt.title('Box Plot of Purchases')
plt.ylabel('Purchase Amount')
plt.show()

