import json
import tweepy
import datetime


def hello(event, context):
    # Twitter API credentials
    consumer_key = '3oLPZrOiOLSPnRibb6mwXhE9J'
    consumer_secret = 'yfNePnFZ6B0e37hkPEEzCwkuFhk3r99CdK9uHKbtKDpdmQZDYE'
    access_token = '2151165253-8GnYZlSGBGHJGBNdnvppiIURoIKetk5wkH00Mkl'
    access_token_secret = 'Q7PmebKSKUTOxPb1losWH15m8mdd49wSsa4Wvgrf2eonG'

    # Authenticate with Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)


# Get current time
    now = datetime.datetime.now()

# Search for tweets containing "Bitcoin news" in the last 24 hours
    tweets = tweepy.Cursor(api.search_tweets, q="Bitcoin news", lang="en", since=int((now-datetime.timedelta(days=1)).timestamp())).items(100)

# Create a dictionary to store tweets and their like count
    tweet_data = {}
    for tweet in tweets:
        tweet_data[tweet.text] = tweet.favorite_count

# Sort tweets by likes count in descending order
    sorted_tweets = sorted(tweet_data.items(), key=lambda x: x[1], reverse=True)

# Get the top 10 most popular tweets
    top_tweets = sorted_tweets[:10]

    return (json.dumps(top_tweets, indent=4))
