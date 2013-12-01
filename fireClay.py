#! /usr/bin/python
# from firebase import firebase

# firebase = firebase.FirebaseApplication('https://zeronews.firebaseio.com', None)
# result = firebase.get('/articles', None)
# print result
# print result[0]['topics'][0]

articleURLs = set()

# sys.exit()

import sys
import feedparser
import socket
import json
import urllib2
import urllib
import nltk
import re, htmlentitydefs
def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)


timeout = 120
socket.setdefaulttimeout(timeout)

feed_url = "http://feeds.washingtonpost.com/rss/politics"
feeds = ['http://feeds.washingtonpost.com/rss/politics',
        'http://feeds.washingtonpost.com/rss/lifestyle/food',
        'http://feeds.washingtonpost.com/rss/entertainment/music',
        'http://feeds.washingtonpost.com/rss/entertainment/tv',
        'http://feeds.washingtonpost.com/rss/entertainment/celebrities',
        'http://feeds.washingtonpost.com/rss/entertainment/books',
        'http://feeds.washingtonpost.com/rss/lifestyle/travel',
        'http://feeds.washingtonpost.com/rss/lifestyle/style',
        'http://feeds.washingtonpost.com/rss/lifestyle/advice',
        'http://feeds.washingtonpost.com/rss/business',
        'http://feeds.washingtonpost.com/rss/world',
        'http://feeds.washingtonpost.com/rss/sports',
        'http://www.npr.org/rss/rss.php?id=1014',
        'http://www.npr.org/rss/rss.php?id=1003',
        'http://feeds.washingtonpost.com/rss/homepage',
        'http://www.nytimes.com/services/xml/rss/nyt/National.xml?pagewanted=all',
        'http://www.npr.org/rss/rss.php?id=1009',
        'http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml?edition=int',
        'http://www.nytimes.com/services/xml/rss/nyt/International.xml?pagewanted=all',
        'http://www.npr.org/rss/rss.php?id=3',
        'http://feeds.bbci.co.uk/news/business/rss.xml?edition=int',
        'http://feeds.wired.com/wired/index',
        'http://www.pcworld.com/index.rss',
        'http://www.sciencemag.org/rss/current.xml',
        'http://www.npr.org/rss/rss.php?id=1025',
        'http://feeds.bbci.co.uk/news/health/rss.xml?edition=int',
        'http://www.washingtonpost.com/wp-dyn/rss/sports/index.xml',
        'http://feeds.theguardian.com/theguardian/football/rss',
        'http://www.npr.org/rss/rss.php?id=1055',
        'http://i.rottentomatoes.com/syndication/rss/top_movies.xml',
        'http://i.rottentomatoes.com/syndication/rss/in_theaters.xml',
        'http://www.nytimes.com/services/xml/rss/nyt/MovieNews.xml?pagewanted=all',
        'http://www.sciencemag.org/rss/twis.xml',
        'http://feeds.gawker.com/kotaku/vip',
        'http://feeds.gawker.com/gizmodo/vip',
        'http://feeds.gawker.com/lifehacker/vip']

articles = []
count = 0

def addArticle(url):
  try:
    testURl = 'http://readability.com/api/content/v1/parser?url=' + urllib.quote(url) + '&token=41595283b49e7c2c6be11082bb1a0696501be7ff'
    response = json.loads(urllib2.urlopen(testURl).read())
    text = unescape(str(nltk.clean_html(response['content'])))

    articles.append({'title':title, 'url':url, 'text':text, 'wordCount':response['word_count'], 'author':response['author'], 'domain':response['domain'], 'date':response['date_published']})
  except:
    pass

for feed_url in feeds:
  count += 1
  print count, 'of', len(feeds)
  d = feedparser.parse(feed_url)
  for s in d.entries:
    title = unicode(s.title).encode("utf-8")
    url = unicode(s.link).encode("utf-8")
    if url in articleURLs:
      continue
    articleURLs.add(url)
    addArticle(url)

fOutput = open('exportedArticles.json', 'w')
fOutput.write(json.dumps({'articles':articles}))
fOutput.close()
print len(articles), "articles exported"
