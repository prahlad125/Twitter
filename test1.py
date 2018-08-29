import tweepy
import sys
from textblob import TextBlob
import nltk
import re
from nltk.tokenize import word_tokenize


access_token = "1021084648036696064-oJefY8xYP98tjMwOJoSns77ZHI4uEZ"
access_token_secret = "TdasWgiRNc2T8EU4fOazSYD8sBgXXP2rYJWgJJto2PPEb"
consumer_key = "q3FOODWHNI4rvADGDxo6zr6mE"
consumer_secret = "Fg3y4pZKpFCWbqt7qY03BE4vZkWjQF8zSp5iv3ZPvDhdD2SMwm"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

screen = sys.argv[1]
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name=screen)

for text in tweets:
    a=text.text
    a=a.encode("utf-8")
    a=a.split()
    print(a)



d={}
filename = 'self.txt'
f= open(filename,"r+")
for i in f:
    l = i.split()
    d[l[0]]=l[1]



print d["wow"]

def read_scores(sent_file):
    with open(sent_file) as f:
        return {line.split('\t')[0]: int(line.split('\t')[1]) for line in f}

'''
if __name__ == '__main__':
    sent_file=sys.argv[1]
    tweet_file = sys.argv[2]
    scores = read_scores(sent_file=sent_file)
    for score in scores:
        print score
'''
