from bs4 import BeautifulSoup
import requests


def request(input_word):
    # 検索用url作成
    base_url = 'https://cookien.com/?s={}'
    request_url = base_url.format(input_word)
    print(request_url)

    # リクエストして成功したらbs4に渡す
    response = requests.get(request_url)
    print(response.status_code)
    body = response.text
    if response.status_code == requests.codes.ok:
        soup = BeautifulSoup(body, 'html.parser')
        return soup
    else:
        response.raise_for_status()


if __name__ == "__main__":
    soup = request('鶏肉')
    print(soup)
