
'''
храню кост функции в дикшанари: название страны - значение


'''

import json
import glob,os
import requests
from collections import defaultdict
import base64
import pandas as pd
from collections import defaultdict
import time
import statistics


df=pd.read_csv('national_features.csv')
print(os.getcwd())





#добавлю в словарь все ключи



def str_not_number(the_str):
    try:
        (float(the_str))
        return False
    except:
        return True

def get_similarity(a,b):
    #print(type(a.iloc[0]),type(b))
    #print(a.iloc[0],b)

    if a.iloc[0]==b:
        return 1
    return -1

'''
алгоритм процентовки:
value/макс+0.5*медиана - округлили

вернули 3
'''


def get_nationality(something):
    value_arr=[]

    for item in something:
        value_arr.append(item[1])

    the_median=statistics.median(value_arr)

    new_arr=[]

    new_arr.append((something[0][0],int(100*something[0][1]/(something[0][1]+0.5*the_median))))
    new_arr.append((something[1][0],int(100*something[1][1]/(something[0][1]+the_median))))
    new_arr.append((something[2][0],int(100*something[2][1]/(something[0][1]+2*the_median))))

    return new_arr

#picture path jpg на диске; nationality_path - json файл с диска

def get_cost_dictionary(base_encoded_pic,df):
    the_dict = defaultdict(float)
    c_l = list(df['countries'])
    for item in c_l:
        if item in the_dict:
            pass
        else:
            the_dict[item] = 0


    parameters_post = {
        "api_key": "d45fd466-51e2-4701-8da8-04351c872236",
        "file_base64":base_encoded_pic,
        "detection_flags": "basicpoints,propoints,classifiers,content",
        "recognize_targets": [
            "all@mynamespace"
        ],
        "original_filename": "sample.png"
    }

    zapros = requests.post('http://www.betafaceapi.com/api/v2/media', json=parameters_post,
                           headers={'Content-type': 'application/json'})

    data = zapros.json()


    #item['value'],item['confidence'],item['name']
    for item in (data['media']['faces'][0]['tags']):
        if (str_not_number(item['value'])):
            #здесь мы получили важную фичу человека
            '''
            надо сравнить все его фичи и поменять значения у национальностей
            сначала залочим датафрейм с такими же фичами, потом изменим значения словаря
            
            получим датафрейм Афганистан
            пройдёмся по всем фичам датафрейма и по всем фичам 
            '''

            for dict_item in the_dict:
                df_country=df.loc[df.iloc[:, 0] == dict_item, :]
                df_country_feature=df_country.loc[df_country['feature'].isin([item['name']])]
                the_dict[dict_item]+=get_similarity(df_country_feature['value'],item['value'])*(item['confidence']+df_country_feature['confidence'].iloc[0])/2
                #print(get_similarity(df_country_feature['value'],item['value']))







    return the_dict



our_dict=get_cost_dictionary('lesha.jpg',df)







sorted = [(k, our_dict[k]) for k in sorted(our_dict, key=our_dict.get, reverse=True)]
#print(sorted)
#sorted=something


final_result=get_nationality(sorted)

print(final_result)

'''
массив с объектами
json

'''



with open('data.json', 'w') as outfile:
    print('{', file=outfile)
    print('  "data": [', file=outfile)

    print('    {', file=outfile)
    print('      "nation": ' + '"' + final_result[0][0] + '"' + ',', file=outfile)
    print('      "occuracy": ' + str(final_result[0][1]), file=outfile)
    print('    },', file=outfile)

    print('    {', file=outfile)
    print('      "nation": ' + '"' + final_result[1][0] + '"' + ',', file=outfile)
    print('      "occuracy": ' + str(final_result[1][1]), file=outfile)
    print('    },', file=outfile)

    print('    {', file=outfile)
    print('      "nation": ' + '"' + final_result[2][0] + '"' + ',', file=outfile)
    print('      "occuracy": ' + str(final_result[2][1]), file=outfile)
    print('    }', file=outfile)

    print('  ]', file=outfile)

    print('}', file=outfile)











#final_countries_percantage=get_nationality(sorted)

#print(our_dict['israel'],type(our_dict['israel']))
#print(get_cost_dictionary('balzhina.jpg',df))


'''
ПОНЯТЬ ЧТО ЭТО СЕРВИС
а не просто обработка фото

Ценность ДНК
фотофильтры уводит от полезной инфы

Инфографика

мотив - самовыражение
1. про смещение внимние
2. мониторинг конкурентов, что важно для пользователей

чётко сформулировать, что доносит юзер

в чём мотивация поделиться

3 национальности.
'''

'''
План:

сделать проценты

спросить про план с диаграммой

спросить про план с названиями национальностей
'''