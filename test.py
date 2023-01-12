import wikipedia as wp
import wikipediaapi

try:
    p = wp.page('cameron van der burgh')
    content = str(p)
    pageTitle = content[16:len(content) - 2]
except wp.DisambiguationError:
    p = wp.page('cameron van der burgh (swimmer')
    content = str(p)
    pageTitle = content[16:len(content) - 2]
except wp.PageError:
    pageTitle = ''
    pass

if pageTitle != '':
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(pageTitle.replace(' ', '_'))
    url = page_py.fullurl

    print("Page - Exists: %s" % page_py.exists())

    print(page_py.fullurl)
else:
    print('bruh')