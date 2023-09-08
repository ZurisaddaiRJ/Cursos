import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
price_extremes = reviews.groupby('variety').price.agg([min,max])
print(price_extremes)