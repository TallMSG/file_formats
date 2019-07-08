import json
from pprint import pprint

newslist = []
with open('files/newsafr.json', encoding="utf-8") as datafile:
  json_data = json.load(datafile)
  articles_qty = len(json_data['rss']['channel']['items'])

  for article in range(0, articles_qty):
    text = json_data['rss']['channel']['items'][article]['description'].split(' ')
    newslist.append(text)


jointnewslist = []
for item in newslist:
  for subitem in item:
    jointnewslist.append(subitem)

longwordslist =[]
for item in jointnewslist:
  low_reg_words = item.lower()
  wordlength = len(item)
  if wordlength > 6:
        longwordslist.append(low_reg_words)


import collections

word_counter = collections.Counter(longwordslist).most_common(10)

sorted_dict = dict(word_counter)

print(f'Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов:')
for k, v in sorted_dict.items():
    print(f'Слово "{k}" встречается {v} раз')



