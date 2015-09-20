#!/usr/bin/python

# coding: utf-8
import os
import tweepy
import threading
import sys
from ConfigParser import ConfigParser


class TwiBot(threading.Thread):

    def conf2api(self):
        with open(self.config) as f:
            c = ConfigParser()
    	    c.readfp(f)
        conf = dict(c.items('twitter'))
        auth = tweepy.OAuthHandler(
            conf['consumer_key'], conf['consumer_secret'])
        auth.set_access_token(conf['access_token'], conf[
                              'access_token_secret'])
        return tweepy.API(auth)

    def tweet(self, tweet):
        if len(tweet) <= 140 and len(tweet) > 0:
            try:
                self.api.update_status(tweet)
                return True
            except tweepy.TweepError:
                print 'Duplicate'
        return False

    def __init__(self, config=os.getenv('HOME') + '/etc/twibot.ini'):
            threading.Thread.__init__(self)
    	self.config = config
    	self.api = self.conf2api()


if __name__ == '__main__':
    if os.path.isfile(sys.argv[1]):
        TwiBot(sys.argv[1]).tweet(" ".join(sys.argv[2:]))
    else:
        TwiBot().tweet(" ".join(sys.argv[1:]))
