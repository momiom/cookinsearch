from bs4 import BeautifulSoup 
import requests
import logging

class SearchCookin:
	def __init__(input_word):
		if __name__ != "__main__":
			# Flaskのロガーを取得
			self.logger = logging.getLogger('flask.app')
		# 検索ワードを設定
		self.input_word = input_word
	
	def request_cookin():
		# 検索用url作成
		base_url = 'https://cookien.com/?s={}'
		request_url = base_url.format(self.input_word)
		self.logger.info('Request URL: {}'.format(request_url))
		
		# リクエストして成功したらbs4に渡す
		response = requests.get(request_url)
		body = response.text
		if response.status_code != requests.codes.ok:
			self.logger.warn('Failed to request.')
			response.raise_for_status()
		
		self.soup = BeautifulSoup(body, 'lxml')
		
if __name__ == "__main__":
	s = SearchCookin('鶏肉')
	s.request_cokkin()
