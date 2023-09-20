import pandas as pd
# Path of the file to read
iowa_file_path = '../CSV/train.csv'
home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice
print(y)