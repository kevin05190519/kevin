#coding:utf-8

import time
import pickle
import random
import requests,datetime,json
from linebot import LineBotApi
from linebot.models import TextSendMessage
from json import JSONEncoder

class RequestManager:

    CONST_API_SLACK_HOOK = 'https://hooks.slack.com/services/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'


    def slackAttachmentsWithFieldsMessager(self, channel, pretext, title, text, title_link, attach_link, botname,bold_text=None, field_content=None, thumb_url=None, footer_icon=None, icon_emoji=None):

        payload = {"channel": channel,
                   "attachments": [
                    {
                        "fallback": "",
                        "color": "#ffaa00",
                        "pretext": pretext,
                        "author_name": "",
                        "author_link": "",
                        "author_icon": "",
                        "title": title,
                        "title_link": title_link,
                        "text": text,
                        "fields": [
                            {
                                "title": bold_text,
                                "value": field_content,
                                "short": False
                            }
                        ],
                        "image_url": attach_link,
                        "thumb_url": thumb_url,
                        "footer": "eat launch Bot",
                        "footer_icon": "https://img.au-market.com/mapi/pc_icon/39767/3976700000002/100211_116788.png",
                        "ts": ''
                    }
                    ],
                   "username": botname,
                   "icon_emoji": icon_emoji,
                   "link_names": 1}

        req = requests.post(self.CONST_API_SLACK_HOOK, data=json.dumps(payload, cls=PythonObjectEncoder))
        print req.text
class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (list, dict, str, unicode, int, float, bool, type(None))):
            return JSONEncoder.default(self, obj)
        return {'_python_object': pickle.dumps(obj)}
"""if str((time.strftime("%d/%m/%Y"))) == '06/10/2017':
    print str((time.strftime("%d/%m/%Y")))
else :
    print 'no'"""


def send_message():
    launch=['義大利麵','北大荒','花蓮扁食','中信','吃沒吃過的','原味','八方雲集','蜥蜴咖哩','肉圓＋麵線','subway',
            'pizza hut','KFC','炒烏龍','牛肉麵','粥','涼麵']
    random_number=random.randint(0, len(launch)-1)
    data = {
        'score': 0,
        'title': 'Todays launch ',
        'date': time.strftime("%d/%m/%Y"),
        'comment': '',
        'pretext': 'UtaPass intern eat launch !',
        'text': '',
        'content': launch[random_number],
        'thumb_url': 'https://img.au-market.com/mapi/pc_icon/39767/3976700000002/100211_116788.png',
        'footer': 'launch',
        'footer_icon': 'https://img.au-market.com/mapi/pc_icon/39767/3976700000002/100211_116788.png',
    }

    # send to utapass channel

    RequestManager().slackAttachmentsWithFieldsMessager("#kevin_iosreview_test", data['pretext'], "", data['text'],
                                                        "", "", "launch time ", data['title'], data['content'],
                                                        data['thumb_url'], data['footer_icon'])
if __name__ == "__main__":
    send_message()