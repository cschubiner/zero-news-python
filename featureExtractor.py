#! /usr/bin/python
from firebase import firebase

firebase = firebase.FirebaseApplication('https://zeronews.firebaseio.com', None)
result = firebase.get('/articles', None)

politicsWords = set(['afghanistan', 'africa', 'america', 'american', 'army', 'asia', 'barack', 'bush', 'campaign', 'candidate', 'china', 'clinton', 'congress', 'conservative', 'constitution', 'corruption', 'courts', 'crime', 'culture', 'democrat', 'democrats', 'economics', 'economy', 'election', 'elections', 'energy', 'environment', 'europe', 'featured', 'funny', 'george', 'government', 'governor', 'health care', 'house', 'humor', 'immigration', 'india', 'iran', 'iraq', 'islam', 'israel', 'john', 'kerry', 'law', 'liberal', 'libya', 'mccain', 'media', 'military', 'new', 'obama', 'pakistan', 'palin', 'political', 'politics', 'poll', 'polling', 'polls', 'president', 'religion', 'rep', 'republican', 'republicans', 'russia', 'science', 'security', 'senate', 'senator', 'states', 'taxes', 'technology', 'terrorism', 'united', 'us', 'usa', 'war', 'washington', 'world'])
sportsWords = set(['49ers', 'afl', 'american', 'football', 'athletics', 'auto', 'racing', 'badminton', 'baseball', 'basketball', 'basketball', 'm', 'basketball', 'w', 'bowling', 'boxing', 'boys', 'basketball', 'boys', 'soccer', 'cheerleading', 'crew', 'cricket', 'cross', 'country', 'curling', 'cycling', 'darts', 'derek', 'jeter', 'equestrian', 'fencing', 'field', 'hockey', 'fishing', 'football', 'basketball', 'girls', 'soccer', 'golf', 'gymnastics', 'handball', 'hockey', 'horse', 'racing', 'ice', 'hockey', 'indoor', 'track', 'lacrosse', 'lakers', 'league', 'martial', 'arts', 'men', 'mens', 'mens', 'basketball', 'mens', 'golf', 'mens', 'soccer', 'mens', 'sports', 'mens', 'tennis', 'michael', 'jordan', 'miscellaneous', 'mma', 'motor', 'sports', 'motorsport', 'motorsports', 'nascar', 'nba', 'netball', 'nfl', 'olympics', 'other', 'sports', 'poker', 'racing', 'sox', 'rifle', 'rowing', 'rugby', 'rugby', 'union', 'running', 'sailing', 'sf', 'skateboarding', 'skiing', 'snooker', 'soccer', 'softball', 'squash', 'surfing', 'swimming', 'swimming', 'diving', 'table', 'tennis', 'tennis', 'track', 'track', 'field', 'triathlon', 'volleyball', 'water', 'polo', 'winter', 'sports', 'women', 'womens', 'womens', 'basketball', 'womens', 'golf', 'womens', 'soccer', 'womens', 'sports', 'womens', 'tennis', 'wrestling', 'yankees'])

politicsArticles = 0
for article in result:
  articleText = article['text'].encode('utf-8')
  numPoliticsWords = 0
  numSportsWords = 0
  for word in articleText.split():
    if word in politicsWords:
      numPoliticsWords += 1
    if word in sportsWords:
      numSportsWords += 1

  if float(numPoliticsWords)/article['wordCount'] > .01:
    politicsArticles += 1
  print numPoliticsWords, numSportsWords
print politicsArticles
