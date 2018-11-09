#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

import os
from unidecode import unidecode


#
# Basic settings
#
USE_FOLDER_AS_CATEGORY = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DELETE_OUTPUT_DIRECTORY = True
PATH = 'content'
PLUGINS = ['sitemap']
PLUGIN_PATHS = ['vendor/plugins']
SITENAME = 'blog'

if os.getenv('PYTHON_ENV') == 'production':
    SITEURL = 'https://emoji-gen.ninja/blog'
else:
    SITEURL = ''


#
# URL settings
#
ARTICLE_URL = 'posts/{date:%Y%m%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y%m%d}/{slug}.html'
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''


#
# Time and Date
#
TIMEZONE = 'Asia/Tokyo'
DEFAULT_DATE_FORMAT = '%Y/%m/%d'


#
# Metadata
#
AUTHOR = '絵文字ジェネレーター'


#
# Feed settings
#
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


#
# Pagination
#
DEFAULT_PAGINATION = 10


#
# Translations
#
DEFAULT_LANG = 'ja'


#
# Plugins
#
SITEMAP = { 'format': 'xml' }
