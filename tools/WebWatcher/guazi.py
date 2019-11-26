# =============================================================================
# Author: falseuser
# Created Time: 2019-09-19 13:29:35
# Last modified: 2019-09-23 12:03:48
# Description: watcher_1.py
# =============================================================================
import js2py
import requests
from html.parser import HTMLParser
from log import SimpleLogger


logger = SimpleLogger("cars")


class ScriptParser(HTMLParser):
    """解析HTML中的script内容"""

    def __init__(self):
        super().__init__()
        self.is_script = False
        self.scripts = []

    def handle_starttag(self, tag, attrs):
        if tag == "script":
            self.is_script = True

    def handle_endtag(self, tag):
        if tag == "script":
            self.is_script = False

    def handle_data(self, data):
        if self.is_script:
            self.scripts.append(data)


class CarsParser(HTMLParser):
    """解析HTML中的Cars信息"""

    def __init__(self):
        super().__init__()
        self.cars = []
        self.prefix = "https://www.guazi.com"

    def handle_starttag(self, tag, attrs):
        a_class = ('class', 'car-a')
        if tag == "a" and a_class in attrs:
            car_attrs = dict(attrs)
            title = car_attrs['title']
            href = self.prefix + car_attrs['href'].split('#')[0]
            car = (title, href)
            self.cars.append(car)


def get_antipas(text):
    parser = ScriptParser()
    parser.feed(text)
    script = parser.scripts[0].strip()
    parser.close()
    script_splitted = script.split(";")
    script = ";".join(script_splitted[:-4])
    context = js2py.EvalJs()
    context.execute(script)
    return context.value


def get_from_www(url):
    user_agent = (
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/76.0.3809.132 Safari/537.36"
    )
    headers = {
        "User-Agent": user_agent,
    }
    r1 = requests.get(url, headers=headers)  # Get antipas
    if r1.status_code == 203:
        r1.encoding = "UTF-8"
        antipas = get_antipas(r1.text)
        cookies = {"antipas": antipas}
        r2 = requests.get(url, headers=headers, cookies=cookies)
        if r2.status_code == 200:
            r2.encoding = "UTF-8"
            return r2.text
        else:
            msg = "Get content from {0} failed".format(url)
            raise Exception(msg)
    else:
        msg = "Get antipas from {0} failed".format(url)
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
