import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"
combined_products = pd.concat([gaming_products,movie_products])
print(combined_products)