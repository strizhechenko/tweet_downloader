from twitter import TwiBot
import json, os


def tweets_save(tweets):
    open(TwiBot.cache, 'w').write(json.dumps(tweets, indent=4))


def tweets_fetch_all():
    me = TwiBot(config).api.me()
    all_tweets = list()
    max_id = None
    for page in range(0, 16):  # 16 * 200 = 3200, twitter limit
        tweets, max_id = download(me, max_id)
        all_tweets.extend(tweets)
    return all_tweets


def tweets_fetch(me, max_id):
    tweets = me.timeline(count=200, max_id=max_id)
    tweets_to_text = lambda tweet: tweet.text
    return map(tweets_to_text, tweets), tweets.max_id


if __name__ == '__main__':
    tweets_save(tweets_fetch_all())
