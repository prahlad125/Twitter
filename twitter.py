from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "1021084648036696064-oJefY8xYP98tjMwOJoSns77ZHI4uEZ"
access_token_secret = "TdasWgiRNc2T8EU4fOazSYD8sBgXXP2rYJWgJJto2PPEb"
consumer_key = "q3FOODWHNI4rvADGDxo6zr6mE"
consumer_secret = "Fg3y4pZKpFCWbqt7qY03BE4vZkWjQF8zSp5iv3ZPvDhdD2SMwm"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
