import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
a = ['country','variety']
df = reviews.loc[:99, a]
print(df)