from __future__ import absolute_import, print_function

from tweepy import OAuthHandler, Stream, StreamListener
import json

consumer_key	    = os.getenv('CONSUMER_KEY')
consumer_secret 	= os.getenv('CONSUMER_SECRET')
access_token 		= os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        
        data = json.loads(data)
        print(data, data['text'])
        # save this to file?
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(languages=["ml"],track=['malayalam'])

