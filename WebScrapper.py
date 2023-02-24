import requests
import bs4

books_list = []
for i in range(1, 51):
    url = 'http://books.toscrape.com/catalogue/page-{}.html'.format(i)
    print(url)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    curr_page_list = soup.select('.product_pod')
    for book in curr_page_list:
        if [] != book.select('.star-rating.Two'):
            books_list.append(book.select('a')[1]['title'])

print(books_list)
print(len(books_list))
