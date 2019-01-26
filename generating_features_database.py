'''

Get list of features on the screen looking nicely

'''

import json
from pprint import pprint

with open('output/burma.json') as f:
    data = json.load(f)

#pprint(data)


pprint(data['media']['faces'][0]['tags'])

'''
Функция совпадений:
совпало по значение - прибавляем confidence
отнимаем конфиденс умноженный на число
чем больше цифра, тем больше результат для народа

'''
