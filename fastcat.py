#!/usr/bin/env python

import os
import re
import bz2

try:  # python2
    from urllib import urlretrieve, unquote
except ImportError:  # python3
    from urllib.request import urlretrieve
    from urllib.parse import unquote

import redis

skos_file = 'skos.nt.bz2'
ntriple_pattern = re.compile('^<(.+)> <(.+)> <(.+)> \.\n$')


class FastCat(object):

    def __init__(self, db=None):
        if db is None:
            db = redis.Redis()
        self.db = db

    def broader(self, cat):
        """Pass in a Wikipedia category and get back a list of broader Wikipedia
        categories.
        """
        return list(map(lambda res: res.decode('utf-8'), self.db.smembers('b:%s' % cat)))

    def narrower(self, cat):
        """Pass in a Wikipedia category and get back a list of narrower Wikipedia
        categories.
        """
        return list(map(lambda res: res.decode('utf-8'), self.db.smembers('n:%s' % cat)))

    def load(self):
        if self.db.get('loaded-skos'):
            return

        if not os.path.isfile(skos_file):
            self.download()

        print('loading %s' % skos_file)
        for line in bz2.BZ2File(skos_file):
            m = ntriple_pattern.match(line.decode('utf-8'))

            if not m:
                continue

            s, p, o = m.groups()
            if p != 'http://www.w3.org/2004/02/skos/core#broader':
                continue

            narrower = self._name(s)
            broader = self._name(o)
            self.db.sadd('b:%s' % narrower, broader)
            self.db.sadd('n:%s' % broader, narrower)
            print('added %s -> %s' % (broader, narrower))

        self.db.set('loaded-skos', '1')

    def download(self):
        print('downloading wikipedia skos file from dbpedia')
        url = 'http://downloads.dbpedia.org/3.9/en/skos_categories_en.nt.bz2'
        urlretrieve(url, skos_file)

    def _name(self, url):
        m = re.search('^http://dbpedia.org/resource/Category:(.+)$', url)
        return unquote(m.group(1).replace('_', ' '))
