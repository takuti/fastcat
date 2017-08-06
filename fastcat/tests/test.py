# coding: utf-8

from __future__ import unicode_literals
import unittest

import fastcat


class FastcatEnglishTests(unittest.TestCase):

    def test_narrower(self):
        loader_en = fastcat.FastCatLoader()
        loader_en.load()

        f = fastcat.FastCat()
        self.assertTrue('Functional languages' in f.narrower('Functional programming'))

    def test_broader(self):
        loader_en = fastcat.FastCatLoader()
        loader_en.load()

        f = fastcat.FastCat()
        self.assertTrue('Computing' in f.broader('Computer programming'))


class FastcatJapaneseTests(unittest.TestCase):

    def test_narrower(self):
        loader_ja = fastcat.FastCatLoaderJapanese()
        loader_ja.load()

        f = fastcat.FastCat()
        self.assertTrue('関数型言語' in f.narrower('関数型プログラミング'))

    def test_broader(self):
        loader_ja = fastcat.FastCatLoaderJapanese()
        loader_ja.load()

        f = fastcat.FastCat()
        self.assertTrue('コンピュータ' in f.broader('プログラミング'))
