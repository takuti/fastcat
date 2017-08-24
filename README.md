fastcat
=======

[![Build Status](https://travis-ci.org/takuti/fastcat.svg?branch=master)](https://travis-ci.org/takuti/fastcat)

**fastcat** is a little Python library for quickly looking up broader/narrower 
relations in Wikipedia categories locally. The idea is that fastcat can be
useful in situations where you need to rapidly lookup category relations,
but don't want to hammer on the [Wikipedia
API](http://en.wikipedia.org/w/api.php). fastcat relies on Redis, and a 
[SKOS](http://downloads.dbpedia.org/3.9/en/skos_categories_en.nt.bz2) 
file that [DBpedia make available](http://wiki.dbpedia.org/services-resources/documentation/datasets) based on the Wikipedia MySQL
[dumps](http://dumps.wikimedia.org/enwiki/latest/).

The original author of fastcat is [Ed Summers](https://github.com/edsu/fastcat), and here [Takuya Kitazawa](https://github.com/takuti/) directly modifies the code on this forked repository. The main difference with the original version is that, Japanese is supported in addition to English, and you can install fastcat via `pip`. Note that the modified version of fastcat only supports Python 3, while the original code was written in Python 2.

## Installation

You first need to setup Redis server on your machine as follows.

On Mac:

```
$ brew install redis
```

On Linux:

```
$ apt-get install redis-server
```

Eventually, installing fastcat itself is straightforward:

```
$ pip install git+https://github.com/takuti/fastcat.git
```

## Usage

First and foremost, you should not forget to launch a local Redis server as:

```
$ redis-server
```

Next, the first time you import fastcat you'll need to populate your Redis database
with the category data from DBpedia. To do that instantiate a `FastCatLoader` object
and call the `load` method. After that you can use it to do lookups.

```python
>>> from fastcat import FastCatLoader, FastCat
>>> f = FastCat()
>>> # English
>>> FastCatLoader(lang='en').load()
...
>>> f.narrower('Functional programming')
['Lambda calculus', 'Functional data structures', 'Dependently typed programming', 'Higher-order functions', 'Implementation of functional programming languages', 'Recursion schemes', 'Combinatory logic', 'Functional languages']
>>> f.broader('Computer programming')
['Computing', 'Software engineering']
>>> # Japanese
>>> FastCatLoader(lang='ja').load()
...
>>> f.narrower( 関数型プログラミング')
['高階関数', '関数型言語']
>>> f.broader('プログラミング')
['コンピュータ', '計算機科学', 'ソフトウェア工学']
```

## License

[Creative Commons Attribution-ShareAlike 3.0](http://creativecommons.org/licenses/by-sa/3.0/)
