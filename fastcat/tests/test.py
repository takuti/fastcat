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
        self.assertTrue('Functional languages' in self.f.narrower('Functional programming'))

    def test_broader(self):
        self.assertTrue('Computing' in self.f.broader('Computer programming'))


class FastcatJapaneseTests(unittest.TestCase):

    def setUp(self):
        FastCatLoader(lang='ja').load()
        self.f = FastCat()

    def test_narrower(self):
        self.assertTrue('関数型言語' in self.f.narrower('関数型プログラミング'))

    def test_broader(self):
        self.assertTrue('コンピュータ' in self.f.broader('プログラミング'))
