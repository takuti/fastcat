# coding: utf-8

from __future__ import unicode_literals
import unittest

from fastcat import FastCatLoader, FastCat


class FastcatEnglishTests(unittest.TestCase):

    def setUp(self):
        FastCatLoader(lang='en').load()
        self.f = FastCat()

    def test_invalid_lang(self):
        with self.assertRaises(ValueError):
            FastCatLoader(lang='cn')

    def test_narrower(self):
        res = self.f.narrower('Functional programming')
        print(res)
        self.assertTrue('Functional languages' in res)

    def test_broader(self):
        res = self.f.broader('Computer programming')
        print(res)
        self.assertTrue('Computing' in res)


class FastcatJapaneseTests(unittest.TestCase):

    def setUp(self):
        FastCatLoader(lang='ja').load()
        self.f = FastCat()

    def test_narrower(self):
        res = self.f.narrower('関数型プログラミング')
        print(res)
        self.assertTrue('関数型言語' in res)

    def test_broader(self):
        res = self.f.broader('プログラミング')
        print(res)
        self.assertTrue('コンピュータ' in res)
