#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ling\u1e85ars'
SITENAME = u'Ling\u1e85ars'
SITEURL = u'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDERS_AS_CATEGORY = True
MAIN_MENU = True

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/Lingwars'),
          ('twitter', 'https://twitter.com/lingwars'),
          ('The team', SITEURL + '/authors.html'),
          )

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 50

PLUGIN_PATHS = ['plugins']
PLUGINS = ['autopages']

THEME = 'theme/notmyidea'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
