import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
first_description = reviews.description.iloc[0]
# Check your answer
print(first_description)