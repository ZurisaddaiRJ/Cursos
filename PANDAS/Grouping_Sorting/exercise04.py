import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
sorted_varieties = reviews.groupby('variety').price.agg([min,max]).sort_values(by=['min', 'max'], ascending=False)
print(sorted_varieties)