import settings
import requests
import json


def sendMessage(message):
    if not "RT" in message:
        json.loads(message._json)
        response = requests.post(
            url='https://api.telegram.org/bot{}/sendMessage?chat_id=@ghana360&text={}'.format(
                settings.BOT_TOKEN, message)
        )
        return response.json
