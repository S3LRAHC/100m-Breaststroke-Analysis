from playwright.sync_api import sync_playwright
import pandas as pd

# read csv
df = pd.read_csv('100m_breaststroke.csv')

# getting swimmer names
names = df.loc[:, 'full_name_computed']

# getting all first and last names to search on fina website
firstNames = []
lastNames = []
for i in range(len(names)):
    name = names.iloc[i]
    commaIndex = name.rfind(',')
    lastNames.append(name[:commaIndex])
    firstNames.append(name[commaIndex + 2:])

firstNames = [x.casefold() for x in firstNames]
lastNames = [x.casefold() for x in lastNames]

# ============== scraping height from fina website =================

# URL
URL = "https://www.fina.org/athletes?gender=&discipline=&nationality=&name="

# XPATHS
ATHLETE_SEARCH = "//input[@id='athlete-search']"
SEARCH_ENTER = "//button[@type='submit']"
ATHLETE_PAGE = "//div[@class='athlete-table__name']"
ATHLETE_PROFILE = "//a[@title='Profile']"
ATHLETE_HEIGHT = "//*[@id='main-content']/section[1]/div[1]/div[1]/div[2]/span[2]"

# getting list of athlete height
heightList = []
for i in range(len(names)):
    firstName = firstNames[i]
    lastName = lastNames[i]
    athleteHeight = ''

    # scraping height data
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL)

        # search athlete
        page.fill(ATHLETE_SEARCH, "{} {}".format(firstName, lastName))
        page.keyboard.press('Enter')

        # go to athlete page
        page.click(ATHLETE_PAGE)

        # go to athlete profile
        page.click(ATHLETE_PROFILE)

        # get athlete height
        athleteHeight = page.text_content(ATHLETE_HEIGHT)
        athleteHeight = athleteHeight.strip()
        try:
            athleteHeight = int(athleteHeight)
        except ValueError:
            pass
        
    heightList.append(athleteHeight)
    print(heightList)

# appending to csv
height_df = pd.DataFrame({'height': heightList})
height_df.to_csv('100m_breaststroke', mode='a', index=False, header=False)
