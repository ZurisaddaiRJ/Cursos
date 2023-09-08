import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']
print(bargain_wine)