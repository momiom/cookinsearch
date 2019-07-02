from bs4 import BeautifulSoup
import requests
import logging


class Scraper:
    def __init__(self, input_word):
        if __name__ != "__main__":
            # Flaskのロガーを取得
            self.logger = logging.getLogger('flask.app')
        # 検索ワードを設定
        self.input_word = input_word


class CookinScraper(Scraper):
    def request(self):
        # 検索用url作成
        base_url = 'https://cookien.com/?s={}'
        request_url = base_url.format(self.input_word)
        self.logger.info('Request URL: {}'.format(request_url))

        # リクエストして成功したらbs4に渡す
        response = requests.get(request_url)
        body = response.text
        if response.status_code == requests.codes.ok:
            self.soup = BeautifulSoup(body, 'lxml')
        else:
            self.logger.warn('Failed to request.')
            response.raise_for_status()


class ShirogohanScraper(Scraper):
    def request(self):


if __name__ == "__main__":
    s = CookinScraper('鶏肉')
    s.request_cokkin()
