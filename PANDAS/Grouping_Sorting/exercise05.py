import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()
print(reviewer_mean_ratings )