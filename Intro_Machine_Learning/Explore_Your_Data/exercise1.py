import pandas as pd

# Path of the file to read
iowa_file_path = '../CSV/train.csv'

# Fill in the line below to read the file into a variable home_data
home_data = pd.read_csv(iowa_file_path)

# Call line below with no argument to check that you've loaded the data correctly
print(home_data)