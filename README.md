# Flask + line-bot-sdk
## 構成
```
.
|-- README.md
|-- app
|   |-- Dockerfile
|   |-- logs
|   |   |-- python.log
|   |   `-- uwsgi.log
|   |-- requirements.txt
|   |-- src
|   |   |-- bs4scrach.py
|   |   |-- items.py
|   |   |-- line
|   |   |   |-- flex_message.json
|   |   |   `-- memo.txt
|   |   |-- run.py
|   |   `-- scrapers.py
|   `-- uwsgi.ini
|-- docker-compose.yml
`-- nginx
    |-- Dockerfile
    |-- logs
    |   |-- access.log
    |   `-- error.log
    `-- nginx.conf
```
