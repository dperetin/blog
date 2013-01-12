# -*- coding: utf-8 -*-
AUTHOR = u'Dejan Peretin'
SITENAME = u"dejanperetin.com"
SITEURL = 'http://dejanperetin.com'
TIMEZONE = "Europe/Paris"

#GITHUB_URL = 'http://github.com/dperetin/'
DISQUS_SITENAME = "dperetin"
GOOGLE_ANALYTICS = "UA-32705935-1"

PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True

DEFAULT_PAGINATION = 4

#FEED_RSS = 'feeds/all.rss.xml'
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS = (('Linux za sve', 'http://www.linuxzasve.com'),
         ('Pelican', "http://pelican.notmyidea.org/en/latest/"),
        )

SOCIAL = (('Twitter', 'http://twitter.com/dperetin'),
          ('GitHub', 'http://github.com/dperetin'),
          ('Stack Overlow', 'http://stackoverflow.com/users/1803990/dperetin'))

# static paths will be copied under the same name
STATIC_PATHS = ["slike", ]

THEME = "tuxlite_tbs"

DISPLAY_PAGES_ON_MENU = True

DEFAULT_CATEGORY = 'Ostalo'

DEFAULT_LANG = 'en'

LOCALE = {'hr_HR'}

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
