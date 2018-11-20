#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import json
import os
import re
from unidecode import unidecode


#
# Custom settings
#
ENV = os.getenv('PYTHON_ENV', 'development')
NOINDEX = True # ENV == 'development'
SITE_SUBTITLE = 'チャット向け絵文字生成サービス'
INDEX_TITLE = '記事一覧'


#
# Basic settings
#
def do_hashed_assets(name):
    json_path = 'theme/assets.json'
    with open(json_path, 'r') as fp:
        assets = json.load(fp)
        asset_path = assets['main'].get(name)
        if asset_path:
            return asset_path.replace('static/', '')

def do_squash(value):
    return re.sub(r'\s+', ' ', value)

USE_FOLDER_AS_CATEGORY = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DELETE_OUTPUT_DIRECTORY = True
JINJA_FILTERS = {
    'hashed_assets': do_hashed_assets,
    'squash': do_squash,
}
PATH = 'content'
PLUGINS = ['minify', 'sitemap']
PLUGIN_PATHS = ['vendor/plugins']
SITENAME = '絵文字ジェネレーター 開発者ブログ'

if ENV == 'production':
    SITEURL = 'https://emoji-gen.ninja/blog'
else:
    SITEURL = '/blog'


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
# Themes
#
THEME = 'theme'


#
# Plugins
#
MINIFY = {
    'reduce_boolean_attributes': True,
    'remove_comments': True,
}
SITEMAP = { 'format': 'xml' }
