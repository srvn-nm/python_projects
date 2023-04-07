from __future__ import unicode_literals
import json
from hazm import *


docs_contents = []
docs_titles = []
docs_urls = []
positionalIndex = {}
docs_ranks = {}
phrase = []
stopWords_list = ["با", "و", "در", "ولی", "اما", "نیز", "اگر", "که", "مگر", "از", "بر", "تا", "بی", "الا", "غیر", ".",
                ",", "،", ".", "/", "را", "مانند", "جزو", ":", "به", "؛"]

def read():
    f = open('../../IR_data_news_12k.json', encoding='utf8')
    data = json.load(f)
    for i in data:
        docs_titles.append(data[i]["title"])
        docs_contents.append(data[i]["content"])
        docs_urls.append(data[i]["url"])
    f.close()
    
def normalize(data, i):
    normalizer = Normalizer()
    data = normalizer.normalize(data)
    tokenizedData = word_tokenize(data)
    stemmer = Stemmer()
    for j in range(len(tokenizedData)):
        tokenizedData[j] = stemmer.stem(tokenizedData[j])
    for i in tokenizedData:
        if i in stopWords_list:
            tokenizedData.remove(i)
            print(data)
    index(tokenizedData, i)
    
def index(tokenizedData, i):
    for j in range(len(tokenizedData)):
        data = tokenizedData[j]
        if data in positionalIndex:
            positionalIndex[data][0] = positionalIndex[data][0] + 1
            if i in positionalIndex[data][1]:
                positionalIndex[data][1][i].append(j)
            else:
                positionalIndex[data][1][i] = [j]
        else:
            positionalIndex[data] = []
            positionalIndex[data].append(1)
            positionalIndex[data].append({})
            positionalIndex[data][1][i] = [j]


read()
normalize()