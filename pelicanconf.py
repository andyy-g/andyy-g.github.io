#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'APT42'
SITENAME = 'APT42'
#SITESUBTITLE = u'My Awesome Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

NEST_CSS_MINIFY = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#       ('Python.org', 'https://www.python.org/'),
#       ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#       ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#        ('Another social link', '#'),)

NEST_SITEMAP_MENU = (('À propos', '/a-propos'),
                    ('Contact', '/contact'),
                    ('Statuts', '/statuts'),
                    ('Charte', '/charte'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Themes
THEME = "nest"


NEST_HEADER_IMAGES = "background.jpg"
NEST_HEADER_LOGO = "extra/logo.svg"

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/logo.svg': {'path': 'logo.svg'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
    }


MENUITEMS = [('Statuts','/statuts', '#5f00ff'), ('Charte', '/charte', '#fb04fc'), ('À propos', '/a-propos', '#16c664'), ('Contact', '/contact', '#faed27')]

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

