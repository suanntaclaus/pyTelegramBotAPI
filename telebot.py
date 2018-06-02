
#APITOKEN = '<616484809:AAFyFLE0JHrxHOEsHXaa-gvGXYk7Tg19HxQ>'
#https://api.telegram.org/bot616484809:AAFyFLE0JHrxHOEsHXaa-gvGXYk7Tg19HxQ/getUpdates
#https://api.telegram.org/bot616484809:AAFyFLE0JHrxHOEsHXaa-gvGXYk7Tg19HxQ/sendMessage?chat_id=236704084&text=TestReply

#{"ok":true,"result":[{"update_id":959942309,
#"message":{"message_id":15,"from":{"id":236704084,"is_bot":false,"first_name":"Su-ann","username":"suanntaclaus","language_code":"en-GB"},"chat":{"id":236704084,"first_name":"Su-ann","username":"suanntaclaus","type":"private"},"date":1527910904,"text":"/start","entities":[{"offset":0,"length":6,"type":"bot_command"}]}},{"update_id":959942310,
#"message":{"message_id":16,"from":{"id":236704084,"is_bot":false,"first_name":"Su-ann","username":"suanntaclaus","language_code":"en-GB"},"chat":{"id":236704084,"first_name":"Su-ann","username":"suanntaclaus","type":"private"},"date":1527910905,"text":"hello"}}]}
import urllib
import json 
import requests
import time

TOKEN = "616484809:AAFyFLE0JHrxHOEsHXaa-gvGXYk7Tg19HxQ"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["message"]
            chat = update["message"]["chat"]["id"]
            send_message(text, chat)
        except Exception as e:
            print(e)

def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()