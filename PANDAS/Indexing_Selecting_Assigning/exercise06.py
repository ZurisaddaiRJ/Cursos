import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
a = [0, 1, 10, 100]
b=['country','province','region_1','region_2']
df = reviews.loc[a,b]
print(df)
