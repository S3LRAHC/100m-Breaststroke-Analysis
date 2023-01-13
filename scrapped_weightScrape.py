import urllib3
import requests
import wikipediaapi 
import wikipedia as wp
import pandas as pd
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# =================== GETTING NAMES FROM CSV =====================

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

# ============ GETTING URLS FROM WIKIPEDIA =================
url = ''
for i in range(len(names)):
    firstName = firstNames[i]
    lastName = lastNames[i]
    print(firstName + ' ' + lastName)
    try:
        p = wp.page('{} {}'.format(firstName, lastName))
        content = str(p)
        pageTitle = content[16:len(content) - 2]

    except wp.DisambiguationError as e:
        disambiguations = e.options
        # finding disambiguation with swimmer in it
        i = 0
        for i in range(len(disambiguations)):
            if "swimmer" in disambiguations[i]:
                p = wp.page(disambiguations[i])
                break
            else:
                i += 1
        content = str(p)
        pageTitle = content[16:len(content) - 2]

    except wp.PageError:
        pageTitle = ''
        pass
    if pageTitle != '':
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page(pageTitle.replace(' ', '_'))
        url = page_py.fullurl

    if url != '':
        # ================ extracting weight info ================
        # scraping table
        session = requests.Session()
        html = session.get(url, verify=False).content
        soup = BeautifulSoup(html, "lxml")
        table = soup.find("table",{"class":"infobox vcard"})
        info = table.findAll('tr')

        # finding weight info
        weightInfo = '-'
        for row in info:
            content = []
            if row.find('th'):
                content += [row.find('th').text]
            if row.find('a'):
                content += [row.find('a').text]
            if row.find('td'):
                content += [row.find('td').text]
            if 'Weight' in content:
                weightInfo = content

        # ============== cleaning data if weight is found ===============
        weight = 0
        # finding weight entry in list
        if weightInfo != '-':
            i = 0
            for i in range(len(weightInfo)):
                if 'kg' not in weightInfo[i]:
                    i += 1
                else:
                    break
            print(weightInfo)

            # removing spaces and \xa0 characters
            if ' ' in weightInfo[i]:
                weightInfo[i] = weightInfo[i].replace(' ', '')
            if r'\xa0' in weightInfo[i]:
                weightInfo[i] = weightInfo[i].replace(r'\xa0', '')
            text = weightInfo[i]

            print(text)

            # determining weight from string
            kgIndex = text.rfind('kg')
            weight = int(text[kgIndex - 2] + text[kgIndex - 1])

            # if not entire weight is being captured
            if len(str(weight)) == 1:
                weight = int(text[kgIndex - 3] + text[kgIndex - 2])

        # adding weight value to csv
        print(weight)
        df.loc[i, 'weight'] = weight
        df.to_csv('100m_breaststroke.csv', index=False)
