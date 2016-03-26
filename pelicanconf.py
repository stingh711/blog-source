#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'Sting'
SITENAME = u'Pure Blogging'
SITEURL = 'http://stingh711.github.io'
SITETITLE = "Pure Blogging"
SITESUBTITLE = "Sting's note about programming and life"
SITEDESCRIPTION = ''
ROBOTS = 'index, follow'
MAIN_MENU = True

MENUITEMS = (('Archives', '/archives.html'),)

PATH = 'content'
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['asciidoc_reader']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = 'Flex'
#THEME = 'pelican-octopress-theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ASCIIDOC_OPTIONS = ["-a source-highlighter=pygments"]
ASCIIDOC_BACKEND = 'html5'

# Blogroll
SOCIAL = (('Tumblr', 'http://pure-blogging.tumblr.com'),
        ('Lofter', 'http://stinghu.lofter.com'),
        )

# Social widget
SOCIAL = (('Weibo', 'http://weibo.com/1676924302/profile?topnav=1&wvr=6'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images']

QUOTE_CONTENT = '"Replace fear of unknown with curiosity"'
QUOTE_FOOTER = 'Anonymous'
