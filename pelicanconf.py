#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import json
import os
from pathlib import Path
from unidecode import unidecode


#
# Basic settings
#
def hashed_assets(name):
    json_path = str(Path('.').joinpath('theme/dist/assets.json').resolve())
    with open(json_path, 'r') as fp:
        assets = json.load(fp)
        asset_path = assets['main'].get(name)
        if asset_path:
            return asset_path.replace('static/', '')

USE_FOLDER_AS_CATEGORY = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DELETE_OUTPUT_DIRECTORY = True
JINJA_FILTERS = {
    'hashed_assets': hashed_assets,
}
PATH = 'content'
PLUGINS = ['minify', 'sitemap']
PLUGIN_PATHS = ['vendor/plugins']
SITENAME = '絵文字ジェネレーター 開発者ブログ'

if os.getenv('PYTHON_ENV') == 'production':
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
DEFAULT_PAGINATION = 3


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
