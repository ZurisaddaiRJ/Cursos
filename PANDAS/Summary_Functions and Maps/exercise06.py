import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
tro = reviews.description.map(lambda desc:"tropical"in desc).sum()
fru = reviews.description.map(lambda desc : "fruity"in desc).sum()
descriptor_counts = pd.Series([tro,fru], index = ["tropical", "fruity"])
print(descriptor_counts)