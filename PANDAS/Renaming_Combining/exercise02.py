import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
reindexed = reviews.rename_axis('wines', axis= 'rows')
print(reindexed)