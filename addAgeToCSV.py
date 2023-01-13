import pandas as pd
import numpy as np

df = pd.read_csv('100m_breaststroke.csv')

# convert dates to datetime object
df["swim_date"] = pd.to_datetime(df["swim_date"])
df["birth_date"] = pd.to_datetime(df["birth_date"])

# finding difference between dates and converting to years
df['age_at_meet'] = df['swim_date'] - df['birth_date']
df['age_at_meet'] = df.age_at_meet / np.timedelta64(1, 'Y')

# rounding years to 2 decimals
df['age_at_meet'] = df['age_at_meet'].round(decimals=1)

# adding new age column to csv
df.to_csv('100m_breaststroke.csv', header=True, index=False)