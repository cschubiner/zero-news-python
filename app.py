from flask import Flask
import os
from firebase import firebase
import feedparser
import json

firebase = firebase.FirebaseApplication('https://zeronews.firebaseio.com', None)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world!"

@app.route("/topfive")
def topfive():
    # result = firebase.post('/users', new_user)
    # result = firebase.get('/users/name',None)
    d = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
    articles = list()
    for i in range(5):
        article = dict()
        article['id'] = i
        article['title'] = d.entries[i].title
        article['url'] = d.entries[i].link
        articles.append(article)
    return json.JSONEncoder().encode(articles)

if __name__ == "__main__":
    app.run()

