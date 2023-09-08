import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
first_row = reviews.iloc[0]
print(first_row)