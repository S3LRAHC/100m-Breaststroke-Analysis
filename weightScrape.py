import urllib3
import requests
import wikipediaapi 
import wikipedia as wp
import pandas as pd
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# # =================== GETTING NAMES FROM CSV =====================

# # read csv
# df = pd.read_csv('100m_breaststroke.csv')

# # getting swimmer names
# names = df.loc[:, 'full_name_computed']

# # getting all first and last names to search on fina website
# firstNames = []
# lastNames = []
# for i in range(len(names)):
#     name = names.iloc[i]
#     commaIndex = name.rfind(',')
#     lastNames.append(name[:commaIndex])
#     firstNames.append(name[commaIndex + 2:])

# firstNames = [x.casefold() for x in firstNames]
# lastNames = [x.casefold() for x in lastNames]

# # ============ GETTING URLS FROM WIKIPEDIA =================
# urlList = []
# for i in range(len(names)):
#     firstName = firstNames[i]
#     lastName = lastNames[i]
#     try:
#         p = wp.page('{} {}'.format(firstName, lastName))
#         content = str(p)
#         pageTitle = content[16:len(content) - 2]
#     except wp.DisambiguationError:
#         p = wp.page('{} {} (swimmer)'.format(firstName, lastName))
#         content = str(p)
#         pageTitle = content[16:len(content) - 2]
#     except wp.PageError:
#         pageTitle = ''
#         pass
#     if pageTitle != '':
#         wiki_wiki = wikipediaapi.Wikipedia('en')
#         page_py = wiki_wiki.page(pageTitle.replace(' ', '_'))
#         url = page_py.fullurl
#         urlList.append(url)
#     else:
#         urlList.append('')

# ================ extracting weight info ================
urlList = ["https://en.wikipedia.org/wiki/Michael_Phelps"]
weightList = []
extractedWeight = []

for i in range(len(urlList)):    
    url = urlList[i]
    try:
        session = requests.Session()
        html = session.get(url, verify=False).content
        soup = BeautifulSoup(html, "lxml")

        table = soup.find("table",{"class":"infobox vcard"})
        info = table.findAll('tr')

        weightInfo = ' '
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
        extractedWeight.append(weightInfo)

    except:
        url = url + "_(swimmer)"
        session = requests.Session()
        html = session.get(url, verify=False).content
        soup = BeautifulSoup(html, "lxml")

        table = soup.find("table",{"class":"infobox vcard"})
        info = table.findAll('tr')

        weightInfo = ''
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
        extractedWeight.append(weightInfo)

print(extractedWeight)