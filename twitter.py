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
        

    def __init__(self, config=os.getenv('HOME') + '/etc/twibot.ini'):
            threading.Thread.__init__(self)
    	self.config = config
    	self.api = self.conf2api()
