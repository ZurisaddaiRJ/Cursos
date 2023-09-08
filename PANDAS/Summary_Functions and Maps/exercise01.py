import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
median_points = reviews.points.median()
print(median_points )