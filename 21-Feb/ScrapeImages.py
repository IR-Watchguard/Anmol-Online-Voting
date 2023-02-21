import requests
import bs4
import re


def take_input():
    '''Takes A Valid URL From The User'''
    url = ''
    expression = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
    while True:
        url = input('Please Enter Website URL : ')
        if re.findall(expression, url):
            break
        else:
            print('Please Copy The URL From The Website')

    return url


def fetch_images(url):
    '''Returns a list of source to the images'''
    tags = ['img', 'svg']
    print(url)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    fetched_list = []
    for tag in tags:
        page_img = soup.select(tag)
        if page_img:
            fetched_list.extend(page_img)

    src_list = []
    for item in fetched_list:
        if item.get('src', False):
            src_list.append(item['src'])ut
        else:
            src_list.append(item)

    return src_list


url = take_input()
l = fetch_images(url)
for src in l:
    print(src)
