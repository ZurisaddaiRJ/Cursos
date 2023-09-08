import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
first_descriptions = reviews.description.head(10)
print(first_descriptions)