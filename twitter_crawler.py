import tweepy
import json
import time

def authenticate():
    consumer_key = "29VGxORitZLxsC4cJhW8"
    consumer_secret = "7buX5RjxJMmH0XMjzSrIOaxEaCAXvxuv7U0bX1tqCZf7"
    access_token = "712145112-fevxRZkiWwEsx2VQVzG94TUowkg5aCybFwy"
    access_token_secret = "7v2SF5bkS8cJi1zuHRfAfVbeQEZrTbDvzdEuaYM"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return  api

def main():
    api = authenticate()

    user_id = 3763761
    all_tweets = api.user_timeline(id = user_id, count = 200)
    oldest = all_tweets[-1].id - 1

    while True:
        try:
            tweets = api.user_timeline(id = user_id, count = 200, max_id = oldest )
            oldest = tweets[-1].id - 1
            all_tweets.extend(tweets)
        except IndexError:
            break
        except tweepy.error.RateLimitError:
            time.sleep(60*15)

    with open("tweets.json", "w") as f:
        for tweet in all_tweets:
            json.dump(tweet._json,f)
            f.write('\n')


if __name__ == "__main__":
    main()
