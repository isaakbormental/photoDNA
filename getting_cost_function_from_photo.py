import json
import glob,os
import requests
from collections import defaultdict
import base64

'''
Функция: совпадение - прибавляем конфиденс
стринга

'''



'''
root=os.getcwd()
os.chdir(os.getcwd()+"/output")
for file in glob.glob("*.json"):
    print(file)
os.chdir(root)



'''
important_features=[]

def str_not_number(the_str):
    try:
        (float(the_str))
        return False
    except:
        return True

def get_similarity(a,b):
    if a==b:
        return 1
    return -1


def get_nationality(picture_path):

    pass

#picture path jpg на диске; nationality_path - json файл с диска

def get_cost_value(picture_path,nationality_path):
    with open(picture_path, "rb") as image_file:
        encoded_string = image_file.read()


    parameters_post = {
        "api_key": "d45fd466-51e2-4701-8da8-04351c872236",
        "file_base64":base64.b64encode(encoded_string).decode('ascii'),
        "detection_flags": "basicpoints,propoints,classifiers,content",
        "recognize_targets": [
            "all@mynamespace"
        ],
        "original_filename": "sample.png"
    }

    zapros = requests.post('http://www.betafaceapi.com/api/v2/media', json=parameters_post,
                           headers={'Content-type': 'application/json'})

    data = zapros.json()


    with open('output/' + 'user.json', 'w') as outfile:
        json.dump(data, outfile)




    with open(nationality_path) as f2:
        nation_data = json.load(f2)

    user_meaningful_features=defaultdict(list)
    for item in (data['media']['faces'][0]['tags']):
        if(str_not_number(item['value'])):
            user_meaningful_features[item['name']]=[item['value'],item['confidence']]

    nation_meaningful_features=defaultdict(list)

    for item in (nation_data['media']['faces'][0]['tags']):
        if (str_not_number(item['value'])):
            nation_meaningful_features[item['name']] = [item['value'], item['confidence']]


    print(user_meaningful_features)

    print('separator')
    cost_function=0

    print(type(get_similarity(user_meaningful_features['bald'][0],nation_meaningful_features['bald'][0])),get_similarity(user_meaningful_features['bald'][0],nation_meaningful_features['bald'][0]))
    print(type(user_meaningful_features['bald'][1]),user_meaningful_features['bald'][1])

    for keys in user_meaningful_features:
        cost_function+=(user_meaningful_features[keys][1]+nation_meaningful_features[keys][1])/2*get_similarity(user_meaningful_features[keys][0],nation_meaningful_features[keys][0])

    #for item in (nation_data['media']['faces'][0]['tags']):
        #print(item)

#{'value': '0.08', 'confidence': 1.0, 'name': 'yaw'}
#{'value': 'yes', 'confidence': 0.22, 'name': 'young'}
#44 фичи всего

    return cost_function



'''

for item in data['media']['faces'][0]['tags']:
    print(item['confidence'],item['name'],item['value'])

'''



print(get_cost_value('balzhina.jpg','output/india.json'))




'''
мне надо 
links=['https://i.ibb.co/9wSn6cr/afhganistan.png','https://i.ibb.co/nm4gL5x/argentina.png','https://i.ibb.co/J5B4Xqh/austria.png','https://i.ibb.co/fdTmM2R/burma.png','https://i.ibb.co/cr3nyyz/germany.png','https://i.ibb.co/ZNdBYXC/greece.png','https://i.ibb.co/2vFbXTZ/india.png','https://i.ibb.co/B45HPgL/iran.png']
countries=['afghanistan','argentina','austria','burma','germany','greece','india','iran']
#создадим словарь countries: links
countries_links=defaultdict(list)
the_iterator=0
for item in countries:
    countries_links[countries]=links[the_iterator]
    the_iterator+=1
    
i=0
for item in links:
  parameters_post = {
    "api_key": "d45fd466-51e2-4701-8da8-04351c872236",
    "file_uri": item,
    "detection_flags": "basicpoints,propoints,classifiers,content",
    "recognize_targets": [
      "all@mynamespace"
    ],
    "original_filename": "sample.png"
  }

  zapros = requests.post('http://www.betafaceapi.com/api/v2/media', json=parameters_post,
                         headers={'Content-type': 'application/json'})

  data = zapros.json()
  with open('output/'+countries[i]+'.json', 'w') as outfile:
    json.dump(data, outfile)
  i+=1
'''










#for item in ''