import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
a = [1, 2, 3, 5, 8]
sample_reviews = reviews.loc[a]
print(sample_reviews)