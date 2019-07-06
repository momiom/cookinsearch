from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, Base,
    CarouselTemplate, CarouselColumn, TemplateSendMessage,
    URIAction, PostbackAction, MessageAction
)
import logging
import yaml
import json
from collections import OrderedDict

fmt = "%(levelname)s - %(asctime)s - %(pathname)s in %(funcName)s [line:%(lineno)d] : %(message)s"
logging.basicConfig(filename='/var/logs/python.log', level=logging.DEBUG, format=fmt)

app = Flask(__name__)

line_bot_api = LineBotApi(
    'bB/emTb7qCaeqWMUZB8QFNaDKfjX/WaqGXzhefUbR/ekqj31/yRneAY/HJn06iBiOR1mqlhuda9A1343d4ZBDGjuv6QsLPczGtMV5iSzFE249IEWX2q280JPZd1pxNkfuNqdl6tHZzp35QuX6ailHgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('323db4ca5a11c147b072e2b4faa3d3d5')


@app.route("/")
def index():
    app.logger.info('call index')
    return '<h1>index</h1>'


@app.route("/callback", methods=['POST'])
def callback():
    app.logger.debug('Debug call /call back')

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.error("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    # msg = 'れちゃん「{}」'.format(event.message.text)

    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=msg))
    
    with open('line/flex_message.json') as f:
        data = json.dump(f)
    carousel_template = Base.new_from_json_dict(data)
    
#     carousel_template = CarouselTemplate(columns=[
#         CarouselColumn(text='hoge1', title='fuga1', actions=[
#             URIAction(label='Go to line.me', uri='https://line.me'),
#             PostbackAction(label='ping', data='ping')
#         ]),
#         CarouselColumn(text='hoge2', title='fuga2', actions=[
#             PostbackAction(label='ping with text', data='ping', text='ping'),
#             MessageAction(label='Translate Rice', text='米')
#         ]),
#     ])
    template_message = TemplateSendMessage(
        alt_text='Carousel alt text', template=carousel_template)
    line_bot_api.reply_message(event.reply_token, template_message)


if __name__ == "__main__":
    app.run()
