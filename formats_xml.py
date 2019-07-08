import xml.etree.ElementTree as ET

tree = ET.parse('files/newsafr.xml')
root = tree.getroot()

titles = []
for child in root:
  for subchild in child:
    if subchild.tag == 'item':
      for endchild in subchild:
        if endchild.tag == 'description':
          text = endchild.text
          words = text.split()
          titles.append(words)

jointnewslist = []
for item in titles:
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




