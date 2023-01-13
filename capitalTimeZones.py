from playwright.sync_api import sync_playwright, expect
import pandas as pd

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

timeZones = {}

# URL
MAIN_URL = "https://time.is/"

# XPATHS
TEXT = "//*[@id='time_zone']/div[1]/ul/li[1]"

for key, value in capitals.items():
    newUrl = MAIN_URL + value
    if ' ' in value:
        newValue = value.replace(' ', '_')
    timeZone = 0
    content = ''

    if value != '-':
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(newUrl)
            content = page.text_content(TEXT)

        minusIndex = content.rfind('-')
        plusIndex = content.rfind('+')

        if plusIndex > -1:
            if '+' == content[-2]:
                timeZone = content[-1]
            elif '+' == content[-3]:
                timeZone = content[-2] + content[-1]

        elif minusIndex > -1:
            if '-' == content[-2]:
                timeZone = '-' + content[-1]
            elif '-' == content[-3]:
                timeZone = '-' + content[-2] + content[-1]

        timeZones[value] = timeZone
        print(timeZones)

    else:
        continue
