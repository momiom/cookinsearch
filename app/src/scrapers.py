from abc import ABCMeta, abstractmethod
from bs4 import BeautifulSoup
import requests
import logging


class Scraper(metaclass=ABCMeta):
    def __init__(self, input_word):
        if __name__ != "__main__":
            # Flaskのロガーを取得
            self.logger = logging.getLogger('flask.app')
        # 検索ワードを設定
        self.input_word = input_word
        self.base_url = ''

    @abstractmethod
    def get_items():
        pass

    @abstractmethod
    def request(self):
        pass


class CookinScraper(Scraper):
    def get_items():

        return cokkin_items

    def request(self):
        # 検索用url作成
        base_url = 'https://cookien.com/?s={}'
        self.request_url = base_url.format(self.input_word)
        self.logger.info('Request URL: {}'.format(self.request_url))

        # リクエストして成功したらbs4に渡す
        response = requests.get(self.request_url)
        body = response.text
        if response.status_code == requests.codes.ok:
            self.soup = BeautifulSoup(body, 'lxml')
        else:
            self.logger.warn('Failed to request.')
            response.raise_for_status()


class ShirogohanScraper(Scraper):
    def request(self):
        pass


if __name__ == "__main__":
    s = CookinScraper('鶏肉')
    s.request_cokkin()
