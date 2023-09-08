import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1
star_ratings = reviews.apply(stars, axis='columns')
print(star_ratings)