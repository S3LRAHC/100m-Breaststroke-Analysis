import pandas as pd

# city timezones from scraper
capitalTimeZones = {'Cape Town': '2', 'Singapore': '8', 'London': '0', 'Amsterdam': '1', 
'Washington, D.C.': '-5', 'Rome': '1', 'Minsk': '3', 'Canberra': '11', 'Beijing': '8', 
'Paris': '1', 'Kyiv': '2', 'Oslo': '1', 'Tokyo': '9', 'Moscow': '3', 'Ankara': '3', 
'Berlin': '1', 'Vilnius': '2', 'Brasília': '-3', 'Astana': '7', 'Copenhagen': '1', 
'Belgrade': '1', 'Budapest': '1', 'Vienna': '1', 'Seoul': '9', 'Ljubljana': '1', 
'Dublin': '0', 'Wellington': '13', 'Ottawa': '-5', 'Bishkek': '6', 'Bogotá': '-5', 
'Helsinki': '2', 'Athens': '2', 'Stockholm': '1', 'Warsaw': '1', 'Bern': '1', 
'Sofia': '2', 'Reykjavík': '0', 'Jerusalem': '2', 'Bratislava': 
'1', 'Madrid': '1', 'Tallinn': '2', 'Caracas': '-4', '-': '-'}
meetTimeZones = {'Gwangju': '9', 'Tokyo': '9', 'Omaha': '-6', 'Rome': '1', 
'Marseille': '1', 'Greensboro': '-5', 'London': '0', 'Budapest': '1', 'Donetsk': '3', 
'Shanghai': '8', 'Monaco': '1', 
'Barcelona': '1', 'Kazan': '3', 'Istanbul': '3', 'Rio de Janeiro': '-3', 'Heidelberg': '1', 
'Irvine': '-8', 'Copenhagen': '1', 'Debrecen': '1', 'Saint Raphael': '2', 'Berlin': '1', 
'Moscow': '3', 'Napoli': '1', 'Sheffield': '0', 'Rotterdam': '1', 'Nagaoka': '9', 
'Tianjin': '8', 'Shizuoka': '9', 'Jeju': '9', 'Zrenjanin': '1', 'Qingdao': '8', 'Dublin': '0', 
'Birmingham': '0', 'Xian': '1', 'Clovis': '-8', 'Tashkent': '5', 'Beijing': '8', 'Belgrade': '1', 
'Graz': '1', 'Adelaide': 0, 'Toronto': '-5', 'Indianapolis': '-5', 'Alimos': '2', 
'Westmont': '-8', 'Palo Alto': '-8', 'Montreal': '-5', 'Qingdae': '8', 'Ganzhou': '8', 
'Federal Way': '-8', 'Eindhoven': '1', 'Gimcheon': '9', 'Szczecin': '1', 'Gold Coast': '10', 
'Piraeus': '2', 'Glasgow': '0', 'Tochigi': '9', 'Austin': '-6', 'Limoges': '1', 
'Mission Viejo': '-8', 'Taipei City': '8', 'Linköping': '1', 'Stockholm': '1', 
'Port Elizabeth': '2', 'Pescara': '1', 'Sydney': '11', 'Santo Domingo': '-4', 'Chartres': '1'}

# read csv
df = pd.read_csv('100m_breaststroke.csv')

# add timezones and their time difference to dataframe
for i in range(len(df)):
    capital = df.loc[i, 'capital_city']
    meetCity = df.loc[i, 'meet_city']

    try:
        df.loc[i, 'capital_timezone'] = capitalTimeZones[capital]
        df.loc[i, 'meet_timezone'] = meetTimeZones[meetCity]
        df.loc[i, 'time_difference_hours'] = int(meetTimeZones[meetCity]) - int(capitalTimeZones[capital])
    except ValueError:
        continue

df.to_csv('100m_breaststroke.csv', index=False, header=True)