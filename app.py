import sys
import settings
import t_bot

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
from tweepy.streaming import StreamListener


auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


class Listener(StreamListener):
    def __init__(self):
        super(Listener, self).__init__()

    def on_status(self, status):
        t_bot.sendMessage(status)
        # print(status.text, file=self.output_file)

    def on_error(self, status_code):
        print(status_code)


if __name__ == "__main__":
    news_outlet = ['383173078',
                   '363577315', '104872280', '2530363285', '322626161']

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
