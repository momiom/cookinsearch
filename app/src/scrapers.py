import re
from abc import ABCMeta, abstractmethod, ABC
from bs4 import BeautifulSoup
import requests
import logging
from . import items


class Scraper(metaclass=ABCMeta):
    def __init__(self, input_word):
        if __name__ != "__main__":
            # Flaskのロガーを取得
            self.logger = logging.getLogger('flask.app')
        # 検索ワードを設定
        self.input_word = input_word
        self.request_url = ''
        self._base_url = ''
        self._soup = None

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def request(self):
        pass


class CookinScraper(Scraper):
    def request(self):
        # 検索用url作成
        base_url = 'https://cookien.com/?s={}'
        self.request_url = base_url.format(self.input_word)
        self.logger.info('Request URL: {}'.format(self.request_url))

        # リクエストして成功したらbs4オブジェクトを生成
        response = requests.get(self.request_url)
        body = response.text
        if response.status_code == requests.codes.ok:
            self._soup = BeautifulSoup(body, 'lxml')
        else:
            self.logger.warning('Failed to request.')
            response.raise_for_status()

    def get_items(self):
        post_items = []

        post_articles = self._soup.find_all('article', id=re.compile(r'post-[0-9]{1,5}'))
        for post in post_articles:
            url = post.find('a').get('href')
            title = post.find('h2', class_='entry-title-2').string
            img = post.find('img').get('src')
            tags = post.find('div', class_='content_tag').find_all('span', recursive=False)
            tags = [tag.get_text().strip() for tag in tags]
            # 1つだけの場合「すぐめし」アイコンを探す
            if len(tags) == 1:
                has_sugumeshi = len(post.find_all('div', class_='cat_now')) > 0
                if has_sugumeshi:
                    tags.append('すぐめし')
            cooking_methods = post.find('div', class_='cooking_method').find_all('span', recursive=False)
            cooking_methods = [method.get_text().strip() for method in cooking_methods]
            post_items.append(items.CookinItem({
                'url': url.strip(),
                'title': title.strip(),
                'img': img.strip(),
                'tags': tags,
                'cooking_methods': cooking_methods
            }))
        return post_items


class ShirogohanScraper(Scraper):
    def get_items(self):
        pass

    def request(self):
        pass


if __name__ == "__main__":
    s = CookinScraper('鶏肉')
    s.request_cokkin()
