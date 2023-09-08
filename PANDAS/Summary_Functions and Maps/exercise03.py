import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
reviews_per_country = reviews.country.value_counts()
print(reviews_per_country )