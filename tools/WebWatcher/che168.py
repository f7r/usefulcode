# =============================================================================
# Author: falseuser
# Created Time: 2019-09-21 10:55:15
# Last modified: 2019-09-23 12:03:38
# Description: watcher_2.py
# =============================================================================
import requests
from html.parser import HTMLParser
from log import SimpleLogger

logger = SimpleLogger("cars")


class CarsParser(HTMLParser):
    """解析HTML中的Cars信息"""

    def __init__(self):
        super().__init__()
        self.is_car = False
        self.is_title = False
        self.href = ""
        self.cars = []
        self.prefix = "https://www.che168.com"

    def handle_starttag(self, tag, attrs):
        li_class = ('class', 'cards-li list-photo-li')
        a_class = ('class', 'carinfo')
        if tag == "li" and li_class in attrs:
            self.is_car = True
            self.car_title = dict(attrs)['carname']
        if tag == "a" and self.is_car and a_class in attrs:
            car_attrs = dict(attrs)
            href = self.prefix + car_attrs['href'].split('?')[0]
            car = (self.car_title, href)
            self.cars.append(car)

    def handle_endtag(self, tag):
        if tag == "li" and self.is_car:
            self.is_car = False
            self.carname = ""


def get_from_www(url):
    user_agent = (
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/76.0.3809.132 Safari/537.36"
    )
    headers = {"User-Agent": user_agent}
    r1 = requests.get(url, headers=headers)
    if r1.status_code == 200:
        r1.encoding = "gb2312"
        return r1.text
    else:
        msg = "Get content from {0} failed".format(url)
        raise Exception(msg)


def get_cars(url):
    try:
        text = get_from_www(url)
        parser = CarsParser()
        parser.feed(text)
        cars = parser.cars
        parser.close()
        msg = "Get {0} results from {1}".format(len(cars), url)
        logger.info(msg)
        debug_msg = "From {0} Get cars: {1}".format(url, cars)
        logger.debug(debug_msg)
        return cars
    except Exception as e:
        logger.exception(e)
        return []
