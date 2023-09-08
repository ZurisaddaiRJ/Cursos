import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
renamed = reviews.rename(columns={'region_1':'region','region_2':'locale'})
print(renamed )