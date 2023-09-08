import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
top_oceania_wines = reviews.loc [(reviews.country.isin(['Australia','New Zealand'])) & (reviews.points>=95)]
print(top_oceania_wines)