# ベースイメージ
FROM python:3.6

# workdirの指定
WORKDIR /var/www

# 依存Pythonライブラリ一覧コピー
COPY requirements.txt ./
COPY uwsgi.ini ./

# 依存Pythonライブラリインストール
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /var/www/src
#COPY src/ ./
CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
