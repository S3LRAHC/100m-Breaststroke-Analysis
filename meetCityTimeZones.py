from playwright.sync_api import sync_playwright, expect
import pandas as pd

df = pd.read_csv('100m_breaststroke.csv')

timeZones = {}

# URL
MAIN_URL = "https://time.is/"

# XPATHS
TEXT = "//*[@id='time_zone']/div[1]/ul/li[1]"

uniqueCities = df['meet_city'].unique()

for city in uniqueCities:
    newUrl = MAIN_URL + city
    if ' ' in city:
        newValue = city.replace(' ', '_')
    timeZone = 0
    content = ''

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=False)
        page = browser.new_page()
        page.goto(newUrl, timeout=0)
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

    timeZones[city] = timeZone
    print(timeZones)