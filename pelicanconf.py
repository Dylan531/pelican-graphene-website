#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dylan'
SITENAME = u"Dylan's Tech Blog"
SITEURL = 'dylancramer.me'

STATIC_PATHS = []

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
DISQUS_SITENAME = 'dylantechblog'

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),)

MENU_LINKS = (('Home', ''),
          ('About', 'pages/about.html'),
          ('Projects', 'pages/projects.html'),
          ('Archives', 'archives.html'))
MEDIA_LINKS = (('steam', 'http://steamcommunity.com/id/Dylan531'),
          ('git', 'https://gist.github.com/Dylan531'),
          ('twitter', '/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

THEME = '/home/website/pelican-graphene-ui'
DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
