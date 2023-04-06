import json


docs_contents = []
docs_titles = []
docs_urls = []

def read():
    f = open('IR_data_news_12k.json', encoding='utf8')
    data = json.load(f)
    for i in data:
        docs_titles.append(data[i]["title"])
        docs_contents.append(data[i]["content"])
        docs_urls.append(data[i]["url"])
    f.close()