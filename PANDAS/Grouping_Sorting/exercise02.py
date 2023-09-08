import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()
print(best_rating_per_price)