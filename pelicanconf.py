#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Layla Tadjpour'
SITENAME = 'Layla Tadjpour'
SITEURL = ''
THEME = 'Flex'
PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('fast.ai',"http://www.fast.ai/"),
        )



# Feeds 
FEEDS =  (('All posts', 'feeds/all.atom.xml'),
          ('Category', 'feeds/category'),
          )


# Social widget
SOCIAL = (
         ('github', 'https://github.com/layla-tadjpour'),
         ('twitter', 'https://twitter.com/laylatadjpour'),
         ('linkedin', 'https://www.linkedin.com/in/layla-tadjpour-6144602/'),
         )


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DISPLAY_PAGES_ON_MENU = True
STATIC_PATHS = ['images']