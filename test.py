import tweepy
import sys
from textblob import TextBlob
import nltk
import re


access_token = "1021084648036696064-oJefY8xYP98tjMwOJoSns77ZHI4uEZ"
access_token_secret = "TdasWgiRNc2T8EU4fOazSYD8sBgXXP2rYJWgJJto2PPEb"
consumer_key = "q3FOODWHNI4rvADGDxo6zr6mE"
consumer_secret = "Fg3y4pZKpFCWbqt7qY03BE4vZkWjQF8zSp5iv3ZPvDhdD2SMwm"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
screen = sys.argv[1]

tweets = api.user_timeline(screen_name=screen)
'''
d={}
filename = 'self.txt'
f= open(filename,"r+")
for i in f:
    l = i.split()
    d[l[0]]=int(l[-1])
print d['wow']
sum = 0'''
for text in tweets:
    a=text.text
    print a
    analysis = TextBlob(a)
    print
    print (analysis.sentiment)
    if analysis.sentiment.polarity > 0:
        print 'positive'
    elif analysis.sentiment.polarity == 0:
        print 'neutral'
    else:
        print 'negative'
    print
    a=a.encode("utf-8")
    a=a.split()
    '''for i in a:
        if i in d:
            sum += d[i]'''


'''
for text in tweets:
    tokens = nltk.word_tokenize(text.text)
    print tokens[0]
'''


def read_scores(sent_file):
    with open(sent_file) as f:
        return {line.split('\t')[0]: int(line.split('\t')[1]) for line in f}
