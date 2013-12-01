from flask import Flask
import os
import requests
from firebase import firebase
import feedparser
import json
from pprint import pprint
import numpy

firebase = firebase.FirebaseApplication('https://zeronews.firebaseio.com', None)

app = Flask(__name__)

@app.route("/test")
def test():

    liked = open('liked.json')
    print "got pass liked"
    liked_json = json.load(liked)

    disliked = open('disliked.json')
    disliked_json = json.load(disliked)

    # result = firebase.put('users', 'colby/articles/liked', liked_json)
    # result = firebase.put('users', 'colby/articles/disliked', disliked_json)

    return "HELLO"

@app.route("/colbyjson")
def colbyjson():
    result = firebase.get("/users/colby/artibles/liked")

@app.route("/")
def hello():
    result = firebase.get("/articles", None)
    # print result
    return "Hello, world!"

@app.route("/topfive")
def topfive():
    d = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
    articles = list()
    for i in range(10):
        article = dict()
        article['id'] = i
        article['title'] = d.entries[i].title
        article['url'] = d.entries[i].link
        articles.append(article)
    return json.JSONEncoder().encode(articles)

@app.route("/firebase1")
def firebase1():
    result = firebase.get('/articles', None)

    # print result
    r = requests.get(r'http://www.reddit.com/user/spilcm/comments/.json')
    print r
    print r.text
    print r.status_code
    return result

if __name__ == "__main__":
    app.run()

