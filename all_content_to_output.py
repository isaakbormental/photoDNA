
'''

что вообще надо? взять base64 , выдать национальности с процентами



что сейчас пишу? взять весь контент и выгрузить важные фичи в pandas csv

'''

#Эта программа берёт все файлы из паки контент и делает json в аутпут
import os,glob
import pandas
import requests
import base64
import json
from collections import defaultdict


def str_not_number(the_str):
    try:
        (float(the_str))
        return False
    except:
        return True


root=os.getcwd()
os.chdir(os.getcwd()+"/content")

j=0
#iterator for rows


number_of_features=41
index_list=[]
for file in glob.glob("*.png"):
    for i in range(number_of_features):
        index_list.append(file[:-4])

df = pandas.DataFrame(columns=['feature', 'value', 'confidence', 'meaning'], index=index_list)




for file in glob.glob("*.png"):
    #print(type(file))
    with open(os.getcwd() +'/' +file, "rb") as image_file:
        encoded_string = image_file.read()
    parameters_post = {
        "api_key": "d45fd466-51e2-4701-8da8-04351c872236",
        "file_base64": base64.b64encode(encoded_string).decode('ascii'),
        "detection_flags": "basicpoints,propoints,classifiers,content",
        "recognize_targets": [
            "all@mynamespace"
        ],
        "original_filename": "sample.png"
    }
    zapros = requests.post('http://www.betafaceapi.com/api/v2/media', json=parameters_post,
                           headers={'Content-type': 'application/json'})

    data = zapros.json()

    user_meaningful_features = defaultdict(list)
    k=0
    for item in (data['media']['faces'][0]['tags']):
        if (str_not_number(item['value'])):
            #user_meaningful_features[item['name']] = [item['value'], item['confidence']]
            df.iloc[j*number_of_features+k].loc['feature']=(item['name'])
            df.iloc[j*number_of_features+k].loc['value']=(item['value'])
            df.iloc[j*number_of_features+k].loc['confidence']=(item['confidence'])
            df.iloc[j * number_of_features + k].loc['meaning'] = 1
            k+=1
    print(file)
    j+=1

    #print(data['media']['faces'][0]['tags'])

os.chdir(root)
df.to_csv('national_features.csv')





'''

os.chdir(root)
os.chdir(os.getcwd()+"/output")
for file in glob.glob("*.json"):
    print(file)


'''



