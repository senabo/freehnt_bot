import requests
import telebot
import time
import re
import os

token_telegram = os.getenv('TELEGRAM_TOKEN')
token = os.getenv('FREEHUNT_TOKEN')
chat_id = os.getenv('CHAT_ID')

bot = telebot.TeleBot(token_telegram)


def get_api(param):
    '''Get data from Freelancehunt'''
    url = f'https://api.freelancehunt.com/v2/{param}'
    payload = {}
    headers = {'Authorization': f'Bearer {token}'}
    r = requests.request("GET", url, headers = headers, data = payload)
    return r.json()


def check_feeds():
    r = get_api('my/feed')
    for i in r['data'][::-1]:
        if i['attributes']['is_new']:
            mes = i['attributes']['message']
            mes = re.split(r'<', mes, maxsplit = 1)
            text = ('\n' + '<' + mes[1])
            try:
                i['links']
                try:
                    bot.send_message(chat_id = chat_id,
                                     text = '🧨🧨🧨🧨 <b>New Project</b>🧨🧨🧨🧨' + text,
                                     parse_mode = 'HTML')
                except: continue
            except:
                try:
                    bot.send_message(chat_id = chat_id,
                                     text = '✉️✉️✉️✉️ <b>New Message</b> ✉️✉️✉️✉️' + text,
                                     parse_mode = 'HTML')
                except: continue
        else:
            continue


def main_bot():
    while True:
        try:
            check_feeds()
            time.sleep(5 * 60)
        except:
            time.sleep(5 * 60)







