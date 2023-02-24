import requests
import bs4

page = 1
authors = set()
while True:
    base = 'https://quotes.toscrape.com/page/{}/'.format(page)
    res = requests.get(base)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    author_list = soup.select('.author')
    if author_list != []:
        authors.update(author_list)
        page += 1
    else:
        break

''' Printing the unique authors over the website '''
for author in authors:
    print(author.getText())
