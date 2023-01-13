import pandas as pd

df = pd.read_csv('100m_breaststroke.csv')

capitals = {
    'South Africa': 'Cape Town', 'Singapore': 'Singapore', 'Club': '-', 'Great Britain': 'London', 
    'Netherlands': 'Amsterdam', 'United States of America': 'Washington, D.C.', 'Italy': 'Rome', 
    'Belarus': 'Minsk', 'Australia': 'Canberra', "People's Republic of China": 'Beijing', 
    'France': 'Paris', 'Ukraine': 'Kyiv', 'Norway': 'Oslo', 'Japan': 'Tokyo', 
    'Russian Federation': 'Moscow', 'Turkey': 'Ankara', 'Germany': 'Berlin', 
    'Lithuania': 'Vilnius', 'Brazil': 'Brasília', 'Kazakhstan': 'Astana', 'Denmark': 
    'Copenhagen', 'Serbia': 'Belgrade', 'Hungary': 'Budapest', 'Austria': 'Vienna', 
    'Republic of Korea': 'Seoul', 'Slovenia': 'Ljubljana', 'Ireland': 'Dublin', 
    'New Zealand': 'Wellington', 'Canada': 'Ottawa', 'Kyrgyzstan': 'Bishkek', 
    'Colombia': 'Bogotá', 'Finland': 'Helsinki', 'Greece': 'Athens', 'Sweden': 'Stockholm', 
    'Poland': 'Warsaw', 'Switzerland': 'Bern', 'Bulgaria': 'Sofia', 'Iceland': 'Reykjavík', 
    'Israel': 'Jerusalem', 'Slovakia': 'Bratislava', 'Spain': 'Madrid', 'Estonia': 'Tallinn', 
    'Venezuela': 'Caracas'}

for i in range(len(df['team_short_name'])):
    df.loc[i, 'capital_city'] = capitals[df.loc[i, 'team_short_name']]

df.to_csv('100m_breaststroke.csv', header=True, index=False)