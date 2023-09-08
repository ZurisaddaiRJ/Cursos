import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
countries = reviews.country.unique()
print(countries)