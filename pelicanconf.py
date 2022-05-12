#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Benjamin Schwan'
SITENAME = 'bnjmnschwn'
SITEURL = 'http://localhost:8000'
THEME = 'velovivre3/'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['more_categories', 'tipue_search']
STATIC_PATHS = ['images', 'files']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']
DISQUS_SITENAME = 'velovivre'

# define URLs for articles and place to save 
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

# define URLs for pages and place to save 
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# define URLs for categories and place to save
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

# define URLs for tags and place to save
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# period archives
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

LOAD_CONTENT_CACHE = False

FILENAME_METADATA = '(?P<title>.*)'
DESCRIPTION = 'Ein Blog. Ursprünglich mal nur Radsport - mittlerweile breit gefächert'
PATH = '../Content'
OUTPUT_RETENTION = ['.git']
# OUTPUT_PATH = '../Website'

TWITTER_USERNAME = 'bnjmnschwn'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('xcodata.com', 'https://www.xcodata.com'),
	('unterlenker.com', 'https://www.unterlenker.com/'),
	('cyclingsunday.com', 'https://www.cyclingsunday.com'),
	('169k.net', 'https://www.169k.net'),
	('draussendrang.de', 'https://www.draussendrang.de'),
	('goodtimesroll.cc', 'https://www.goodtimesroll.cc'),
	('shutuplegs.de', 'https://www.shutuplegs.de'),
	('jacominasenkel.de', 'https://www.jacominasenkel.de'),
	('radelmaedchen.de', 'https://radelmaedchen.de/'),
	('pedalkultur.blog','https://pedalkultur.blog/'))

# Social widget
SOCIAL = (('instagram', 'https://instagram.com/bnjmnschwn'),
          ('twitter', 'https://twitter.com/bnjmnschwn'),
          ('strava', 'https://www.strava.com/athletes/1292066'),
          ('linkedin', 'https://www.linkedin.com/in/benjamin-schwan/'),
          ('github', 'https://www.github.com/bnjmnschwn'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True