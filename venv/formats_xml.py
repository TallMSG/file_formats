import json
from pprint import pprint

with open('files/newsafr.json', encoding="utf-8") as datafile:
  json_data = json.load(datafile)


dict1 = {}
for k, v in json_data.items():
  dict1 = v

dict2 = {}
for k, v in dict1.items():
  dict2 = dict1["channel"]

list3 = []
for k, v in dict2.items():
  list3 = dict2["items"]

newslist = []
for i in list3:
  newscontent = i["description"]
  wordlist = newscontent.split()
  newslist.append(wordlist)

jointnewslist = []
for item in newslist:
  for subitem in item:
    jointnewslist.append(subitem)


longwordslist =[]
for item in jointnewslist:
  wordlength = len(item)
  if wordlength > 6:
    longwordslist.append(item)

import collections

word_counter = collections.Counter(longwordslist).most_common(10)

sorted_dict = dict(word_counter)

print(f'Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов:')
for k, v in sorted_dict.items():
    print(f'Слово "{k}" встречается {v} раз')



