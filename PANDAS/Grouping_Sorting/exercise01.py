import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()
print(reviews_written)