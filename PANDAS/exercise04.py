import pandas as pd
reviews = pd.read_csv("CSV/winemag-data_first150k.csv", index_col=0)
# Check your answer
reviews.head()
print(reviews)