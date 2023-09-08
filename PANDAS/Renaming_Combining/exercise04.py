import pandas as pd
reviews = pd.read_csv("../CSV/winemag-data-130k-v2.csv")
powerlifting_meets = pd.read_csv("../input/powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("../input/powerlifting-database/openpowerlifting.csv")
left = powerlifting_meets.set_index('MeetID')
right = powerlifting_competitors.set_index('MeetID')
powerlifting_combined = left.join(right)
print()