import tweepy
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import json

access_token = "1021084648036696064-oJefY8xYP98tjMwOJoSns77ZHI4uEZ"
access_token_secret = "TdasWgiRNc2T8EU4fOazSYD8sBgXXP2rYJWgJJto2PPEb"
consumer_key = "q3FOODWHNI4rvADGDxo6zr6mE"
consumer_secret = "Fg3y4pZKpFCWbqt7qY03BE4vZkWjQF8zSp5iv3ZPvDhdD2SMwm"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = tweepy.API(auth)


account_list = []
if (len(sys.argv) > 1):
  account_list = sys.argv[1:]
else:
  print("Please provide a list of usernames at the command line.")
  sys.exit(0)

if len(account_list) > 0:
  for target in account_list:
    print("Getting data for " + target)
    item = auth_api.get_user(target)
    print("name: " + item.name)
    print("screen_name: " + item.screen_name)
    print("description: " + item.description)
    print("statuses_count: " + str(item.statuses_count))
    print("friends_count: " + str(item.friends_count))
    print("followers_count: " + str(item.followers_count))
    tweets = item.statuses_count
    account_created_date = item.created_at
    delta = datetime.utcnow() - account_created_date
    account_age_days = delta.days
    print("Account age (in days): " + str(account_age_days))
    if account_age_days > 0:
      print("Average tweets per day: " + "%.2f"%(float(tweets)/float(account_age_days)))
    hashtags = []
    mentions = []
    tweet_count = 0
    end_date = datetime.utcnow() - timedelta(days=30)

    tweets = []
    fetched_tweets = auth_api.search(target,2)
    for tweet in fetched_tweets:
        parsed_tweet = {}
        parsed_tweet['text'] = tweet.text
        print (parsed_tweet)


    for status in Cursor(auth_api.user_timeline, id=target).items():
      tweet_count += 1
      if hasattr(status, "entities"):
        entities = status.entities
        if "hashtags" in entities:
          for ent in entities["hashtags"]:
            if ent is not None:
              if "text" in ent:
                hashtag = ent["text"]
                if hashtag is not None:
                  hashtags.append(hashtag)
        if "user_mentions" in entities:
          for ent in entities["user_mentions"]:
            if ent is not None:
              if "screen_name" in ent:
                name = ent["screen_name"]
                if name is not None:
                  mentions.append(name)
      if status.created_at < end_date:
        break
    print
    print("Most mentioned Twitter users:")
    for item, count in Counter(mentions).most_common(10):
      print(item + "\t" + str(count))

    print
    print("Most used hashtags:")
    for item, count in Counter(hashtags).most_common(10):
      print(item + "\t" + str(count))

    print
    print "All done. Processed " + str(tweet_count) + " tweets."
    print
