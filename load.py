#!/usr/bin/env python

"""
a little script to download the category data and load it
"""

import fastcat

loader_en = fastcat.FastCatLoader()
loader_en.load()

loader_ja = fastcat.FastCatLoaderJapanese()
loader_ja.load()
