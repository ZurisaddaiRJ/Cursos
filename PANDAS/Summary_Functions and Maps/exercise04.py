import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
centered_price = reviews.price - reviews.price.mean()
print(centered_price)