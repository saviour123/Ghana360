import sys
import json
import requests
import settings


from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
from tweepy.streaming import StreamListener


auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
api = API(auth, wait_on_rate_limit=True,
          wait_on_rate_limit_notify=True)

news_outlet = ['383173078',
               '363577315', '104872280', '2530363285', '322626161', '3131105764', '2463511302']


class Listener(StreamListener):
    def __init__(self):
        super(Listener, self).__init__()

    def on_status(self, status):
        sendMessage(status)
        # print(status.text, file=self.output_file)

    def on_error(
            self, status_code):
        print(status_code)


def sendMessage(message):
    user_id = dict(message._json)['user']['id_str']

    # tweet_url = "https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}".format()
    if not "RT" in message.text and user_id in news_outlet:
        response = requests.post(
            url='https://api.telegram.org/bot{}/sendMessage?chat_id=@ghana360&text={}'.format(
                settings.BOT_TOKEN, message.text)
        )
        resp = response.json
        print(resp)
        print(response)
        return response.json


def main():
    # '742143', '265902729',
    listener = Listener()
    stream = Stream(auth=api.auth, listener=listener)

    try:
        print('Start streaming.')
        stream.filter(news_outlet, )
    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        print('Done.')
        stream.disconnect()


# app = main()

if __name__ == "__main__":
    main()
