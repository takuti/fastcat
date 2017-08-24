import os
import re
import bz2

try:  # python2
    from urllib import urlretrieve, unquote
except ImportError:  # python3
    from urllib.request import urlretrieve
    from urllib.parse import unquote

import redis

ntriple_pattern = re.compile('^<(.+)> <(.+)> <(.+)> \.\n$')


class FastCatBase(object):

    def __init__(self, db=None):
        if db is None:
            db = redis.Redis()
        self.db = db


class FastCatLoader(FastCatBase):

    def __init__(self, lang='en', db=None):
        super(FastCatLoader, self).__init__(db=db)

        if lang == 'en':
            self.skos_file = 'skos.nt.bz2'
            self.src_url = 'http://downloads.dbpedia.org/3.9/en/skos_categories_en.nt.bz2'
            self.category_regexp = r'^http://dbpedia.org/resource/Category:(.+)$'
        elif lang == 'ja':
            self.skos_file = 'skos_ja.ttl.bz2'
            self.src_url = 'http://ja.dbpedia.org/dumps/20160407/jawiki-20160407-skos-categories.ttl.bz2'
            self.category_regexp = r'^http://ja.dbpedia.org/resource/Category:(.+)$'
        else:
            raise ValueError('`lang` must be either "en" or "ja": ' + lang)

    def load(self):
        if self.db.get('loaded-%s' % self.skos_file):
            return

        if not os.path.isfile(self.skos_file):
            self.download()

        print('loading %s' % self.skos_file)

        cnt = 0

        for line in bz2.BZ2File(self.skos_file):
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

            cnt += 1
            if cnt % 1000 == 0:
                print('Loaded %d-th pair: %s -> %s' % (cnt, broader, narrower))

        self.db.set('loaded-%s' % self.skos_file, '1')

    def download(self):
        print('downloading wikipedia skos file from dbpedia')
        urlretrieve(self.src_url, self.skos_file)

    def _name(self, url):
        m = re.search(self.category_regexp, url)
        return unquote(m.group(1).replace('_', ' '))


class FastCat(FastCatBase):

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
