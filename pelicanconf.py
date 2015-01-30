#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Olga Botvinnik'
SITENAME = u'Science, meet productivity'
SITEURL = ''
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'


TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = '/'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = 'feeds/all-%s.atom.xml'

# Blogroll
LINKS =  (('Pythonic Perambulations', 'http://jakevdp.github.io/'),
          ('Living in an Ivory Basement', 'http://ivory.idyll.org/blog/'),
          ("Jess Hamrick's blog", 'http://www.jesshamrick.com/blog/'),)

# Social widget
SOCIAL = (('github-square', 'http://github.com/olgabot'),
          ('twitter-square', 'http://twitter.com/olgabot'),
          ('linkedin-square', 'http://www.linkedin.com/in/olgabotvinnik/'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "olgabot-pure-single"

COVER_IMG_URL = "https://raw.githubusercontent.com/olgabot/olgabot.github.io-source/master/content/images/ordered_driftwood.jpg"
PROFILE_IMG_URL = "http://raw.githubusercontent.com/olgabot/olgabot.github.io-source/master/content/images/olga_icon_square.jpg"
TAGLINE = "A computational RNA biologist exploring productivity, python, and reproducibility."
DISQUS_SITENAME = "sciencemeetproductivity"

TYPOGRIFY = True

GOOGLE_ANALYTICS = "UA-53680167-1"

MENUITEMS = [('Archive', 'archives.html'), ('About', 'pages/about.html'), ]

# IPython notebook blog posts
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['plugins/ipynb']
PLUGINS = ['ipynb']

IPYNB_STOP_SUMMARY_TAGS = [('div', ('class', 'input')), ('div', ('class', 'output'))]
