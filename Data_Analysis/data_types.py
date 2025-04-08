import pandas as pd

data = pd.read_excel(r"C:\Users\wilson.wanderi\Desktop\customer_orders_dataset.xlsx", header=0)

# See the Data Types
data.dtypes
print(data.dtypes)