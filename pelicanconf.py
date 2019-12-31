#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import re


#
# Custom settings
#
ENV = os.getenv('PYTHON_ENV', 'development')
NOINDEX = ENV == 'development'

DESCRIPTION_MAX_LENGTH = 300
INDEX_TITLE = '記事一覧'
INDEX_DESCRIPTION = 'チャットツール向け絵文字の無料生成サービス『絵文字ジェネレーター』の開発者ブログです。サービスのアップデート情報の告知や、技術情報の発信を行っています。絵文字の生成アルゴリズムや、利用技術 (Python, aiohttp, JavaScript, TypeScript, Vue, C++, Skia, etc...) に興味がある方は、ぜひご覧ください。'
PAGER_SUFFIX = 'ページ目'
SITE_SUBTITLE = 'チャット向け絵文字生成サービス'


#
# Basic settings
#
def do_inject_style(value):
    css_path = 'theme/dist/style.css'
    with open(css_path, 'r', encoding = 'utf-8') as fp:
        return fp.read()

def do_squash(value):
    return re.sub(r'\s+', ' ', value)

USE_FOLDER_AS_CATEGORY = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DELETE_OUTPUT_DIRECTORY = True
JINJA_FILTERS = {
    'inject_style': do_inject_style,
    'squash': do_squash,
}
PATH = 'content'
PLUGINS = ['minify', 'neighbors', 'sitemap', 'summary']
PLUGIN_PATHS = ['plugins']
SITENAME = '絵文字ジェネレーター 開発者ブログ'

if ENV == 'production':
    SITEURL = 'https://blog.emoji-gen.ninja'
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
FEED_ATOM = None
FEED_ALL_ATOM = 'feeds/atom.xml'
FEED_ALL_RSS = 'feeds/rss.xml'
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
