import requests
import bs4
import re


class Validate:
    expression = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'

    def check_valid(self, url):
        if re.match(self.expression, url):
            return True
        else:
            return False


class Input:

    url = ''

    def __init__(self):
        self.validate_url = Validate()

    def take_input(self):
        while True:
            self.url = input('Please Enter Website URL : ')
            if self.validate_url.check_valid(self.url):
                return self.url
            else:
                print('Please Copy A Valid Link')


class Scrape:

    def make_soup(self, url):
        res = requests.get(url)
        print(res.history)
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        return soup


class ImageScrapper(Scrape):
    def __init__(self):
        self.scrapehelper = Scrape()
        self.fetched_list = []
        self.src_list = []

    def scrape_images(self, url, tags):
        self.soup = self.scrapehelper.make_soup(url)
        for tag in tags:
            page_img = self.soup.find_all(tag)
            if page_img:
                self.fetched_list.extend(page_img)
        return self.fetched_list

    def fetch_src(self, fetched_list):
        for item in fetched_list:
            if item.get('src', False):
                self.src_list.append(item['src'])
            else:
                self.src_list.append(item)

        return self.src_list


class Printer:
    def print_results(self, res_list):
        for res in res_list:
            print(res)


class WebScrapper:

    def __init__(self):
        self.input_taker = Input()
        self.scrape_images = ImageScrapper()
        self.printer = Printer()

    def return_input(self):
        return self.input_taker.take_input()

    def return_image_list(self, url, tags):
        return self.scrape_images.scrape_images(url, tags)

    def return_src_list(self, fetched_list):
        return self.scrape_images.fetch_src(fetched_list)

    def print_results(self, res_list):
        self.printer.print_results(res_list)


if __name__ == "__main__":
    scrape = WebScrapper()
    user_url = scrape.return_input()
    page_images = scrape.return_image_list(user_url, ['img', 'svg'])
    page_images_src = scrape.return_src_list(page_images)
    scrape.print_results(page_images_src)
