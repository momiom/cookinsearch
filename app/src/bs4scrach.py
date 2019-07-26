from bs4 import BeautifulSoup
import requests
import re
from items import CookinItem


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
        sb = BeautifulSoup(body, 'html.parser')
        return sb
    else:
        response.raise_for_status()


def scrape(bs):
    """
    :type bs: BeautifulSoup
    """
    post_items = []

    post_articles = bs.find_all('article', id=re.compile(r'post-[0-9]{1,5}'))

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
        cooking_methods = post.find('div', class_='cooking_method')
        if cooking_methods is not None:
            cooking_methods = cooking_methods.find_all('span', recursive=False)
            cooking_methods = [method.get_text().strip() for method in cooking_methods]
        else:
            cooking_methods = []
        post_items.append(CookinItem({
            'url': url.strip(),
            'title': title.strip(),
            'img': img.strip(),
            'tags': tags,
            'cooking_methods': cooking_methods
        }))

    return post_items[:10]


if __name__ == "__main__":
    import json
    soup = request('豚肉')
    posts = scrape(soup)
    print(len(posts))
    # with open('./posts.json', 'w', encoding='utf-8') as f:
    #     json.dump(posts, f, indent=4, ensure_ascii=False)
