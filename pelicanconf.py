#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mohit Sharma'
SITENAME = u'Urban Observatory'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme
THEME = "theme/html5/"

# Blogroll
LINKS = (('What is Urban Observatory', 'http://cusp.nyu.edu/press-release/nyu-cusp-unveils-first-kind-urban-observatory-downtown-brooklyn/'),
         ('WSJ2050', 'http://www.wsj.com/articles/as-world-crowds-in-cities-become-digital-laboratories-1449850244'),
         ('NYTimes', 'http://www.nytimes.com/2013/02/24/technology/nyu-center-develops-a-science-of-cities.html'),
         ('UO Feeds and Timelapses', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# For html5-dopetrope
COPYRIGHT = "2016 CUSP"
ABOUT_LINK = "http://cusp.nyu.edu"
ABOUT_IMAGE = "images/cusp-logo.png"
SHOW_COPYRIGHT = True

MAIL = ["masoud.ghandehari@nyu.edu", "greg.dobler@nyu.edu", "mohit.sharma@nyu.edu"]
