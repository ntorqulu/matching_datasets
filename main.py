import pandas as pd

# matches between grammy and msd
grammy = pd.read_csv('tables/grammy_1958_2019.csv')
msd = pd.read_csv('tables/msd_summary.csv')
combined = pd.merge(grammy, msd, left_on='nominee', right_on='title')
print(combined)
