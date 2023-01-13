from playwright.sync_api import sync_playwright
import pandas as pd

df = pd.read_csv('100m_breaststroke.csv')
countries_df = df['team_short_name'].unique()
capitals = {'South Africa': 'Cape Town', 'Singapore': 'Singapore'}

print(countries_df)

# URL
URL = "https://www.google.com/"

# XPATHS
SEARCHBOX = "//input[@class='gLFyf']"
ANSWER = "//a[@class='FLP8od']"
ANSWER2 = "//div[@class='IZ6rdc']"

# scraping capital city data
for i in range(len(countries_df)):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL)

        if countries_df[i] not in ['South Africa', 'Club', 'Singapore']:
            page.fill(SEARCHBOX, "{} capital city".format(countries_df[i]))
            page.keyboard.press('Enter')
        else:
            continue
        try:
            capitals[countries_df[i]] = page.text_content(ANSWER, timeout=5000)
        except:
            capitals[countries_df[i]] = page.text_content(ANSWER2)
    print(capitals)
