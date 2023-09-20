import pandas as pd
# Path of the file to read
iowa_file_path = '../CSV/train.csv'
home_data = pd.read_csv(iowa_file_path)
# Create the list of features below
feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

# Select data corresponding to features in feature_names
X = home_data[feature_names]

print(X)