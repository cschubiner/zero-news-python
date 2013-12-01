#! /usr/bin/python
from firebase import firebase
import json
import topicWordMap

firebase = firebase.FirebaseApplication('https://zeronews.firebaseio.com', None)

articleList = firebase.get('/articles', None)

topics = ['politics', 'sports', 'world', 'science', 'health', 'technology', 'business', 'gaming']
wordMap = topicWordMap.getwordmap()
for articleIndex, article in enumerate(articleList[:2]):
  articleWordList = article['text'].encode('utf-8').split()
  features = list()
  for topic in topics:
    wordCount = 0
    topicWords = wordMap[topic]
    for word in articleWordList:
      if len(word) >= 4 and word.lower() in topicWords:
        wordCount += 1
    for i in range(len(articleWordList)-1):
      # Find pairs of words
      wordPair = articleWordList[i] + ' ' + articleWordList[i+1]
      if wordPair.lower() in topicWords:
        wordCount += 2

    features.append(float(wordCount) * 1000.0/float(article['wordCount']) / float(len(topicWords)))
  result = firebase.put('articles', str(articleIndex) + '/features', features)
  print features
