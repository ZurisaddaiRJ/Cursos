import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
country_variety_counts = reviews.groupby(['country','variety']).size().sort_values(ascending=False)
print(country_variety_counts)