#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Peter Drew'
SITENAME = 'Peter Drew'
SITEURL = ''

THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'simplex'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = None

# (
#     ('Pelican', 'http://getpelican.com/'),
#     ('Python.org', 'http://python.org/'),
#     ('Jinja2', 'http://jinja.pocoo.org/'),
# )

# Social widget
SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/in/pjdrew/'),
    ('GitHub', 'https://github.com/pjdrew'),
    ('Instagram', 'https://www.instagram.com/thepjd/'),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican-plugins/']
PLUGINS = ['i18n_subsites']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
