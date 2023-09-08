import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
print(reviews_per_region)