# coding: utf-8

from __future__ import unicode_literals
import unittest

import fastcat


class FastcatTests(unittest.TestCase):

    def test_narrower(self):
        f = fastcat.FastCat()
        self.assertTrue('Functional languages' in f.narrower('Functional programming'))
        self.assertTrue('関数型言語' in f.narrower('関数型プログラミング'))

    def test_broader(self):
        f = fastcat.FastCat()
        self.assertTrue('Computing' in f.broader('Computer programming'))
        self.assertTrue('コンピュータ' in f.broader('プログラミング'))


if __name__ == '__main__':
    loader_en = fastcat.FastCatLoader()
    loader_en.load()

    loader_ja = fastcat.FastCatLoaderJapanese()
    loader_ja.load()

    unittest.main()
