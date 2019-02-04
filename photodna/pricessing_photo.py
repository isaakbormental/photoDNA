import json
import requests
import pandas as pd
from collections import defaultdict
import statistics
from collections import OrderedDict
import os

# os.chdir('D:\Education\Hackathones\photohack\pravoslavnaya_papka\photoDNA\photodna')
os.chdir('/var/www/html/backend/photoDNA/photodna')

def process(encoded_image):
    df_males = pd.read_csv('national_features_males.csv')
    df_females = pd.read_csv('national_features_females.csv')

    do = False
    the_mask = [0, 0, 0.575, 0.475, 0.625, 0.45, 0.35, 0.475, 1, 0.95, 0.75, 0.75, 0, 0.625, 0.95, 0.75, 0.475, 0, 0, 0,
                0.45, 0.5, 0.2, 0.975, 0.15, 0.55, 1, 0.95, 1, 0, 0.925, 1, 0.525, 0.55, 0.675, 0.85, 0.85, 0, 0, 0.275,
                0, 0, 0, 0.25]

    our_dict, gender, age, facial = get_cost_dictionary(encoded_image, df_males, df_females, the_mask, do)

    if (gender is None and age is None and facial is None):
        return '{"faces":0}'

    age = int(age)
    if (age > 40):
        age -= 10
    else:
        if (age > 30):
            age -= 5

    sorted_arr = [(k, our_dict[k]) for k in sorted(our_dict, key=our_dict.get, reverse=True)]
    final_result = get_nationality(sorted_arr)
    the_data = write_json(final_result, age, gender, facial)
    return json.dumps(the_data, indent=4)
    # with open('data.json', 'w') as outfile:
    #     json.dump(the_data, outfile, indent=4)


def str_not_number(the_str):
    try:
        (float(the_str))
        return False
    except:
        return True


def get_similarity(a,b):

    if a.iloc[0]==b:
        return 1
    return -1


def write_json(the_construction, age,gender,facial):

    intermediate_dict=OrderedDict(the_construction)

    gayness=10*(list(intermediate_dict.values())[0]%10)
    second_digit=(list(intermediate_dict.values())[1])%10>4

    gayness+=second_digit
    gayness=int(10*(gayness*gayness/100/100)%10)

    if (second_digit):
        gayness+=10

    if((list(intermediate_dict.values())[1])%10==6):
        gayness=100-gayness

    new_construct=[{'name':list(intermediate_dict.keys())[0],'confidence':list(intermediate_dict.values())[0]},{'name':list(intermediate_dict.keys())[1],'confidence':list(intermediate_dict.values())[1]},{'name':list(intermediate_dict.keys())[2],'confidence':list(intermediate_dict.values())[2]}]
    #{'nose': [100.0, 'Polish'], 'lips': [100.0, 'Italian'], 'eyes': [100.0, 'Mongolian']}

    facial_new=[{list(facial.keys())[0]:{'confidence':list(facial.values())[0][0],'nation':list(facial.values())[0][1]}},{list(facial.keys())[1]:{'confidence':list(facial.values())[1][0],'nation':list(facial.values())[1][1]}},{list(facial.keys())[2]:{'confidence':list(facial.values())[2][0],'nation':list(facial.values())[2][1]}}]
    new_dict={'nationality':new_construct,'gender':gender,'age':age,'straight':100-gayness,'gay':gayness,'facial features':facial_new}
    return new_dict


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


def get_cost_dictionary(the_64,df_males,df_females,the_mask, do):
    the_dict = defaultdict(float)


    # with open(the_64, "rb") as image_file:
    #     encoded_string = image_file.read()

    parameters_post = {
        "api_key": "d45fd466-51e2-4701-8da8-04351c872236",
        "file_base64":the_64,
        "detection_flags": "basicpoints,propoints,classifiers,content",
        "recognize_targets": [
            "all@mynamespace"
        ],
        "original_filename": "sample.png"
    }

    zapros = requests.post('http://www.betafaceapi.com/api/v2/media', json=parameters_post,
                           headers={'Content-type': 'application/json'})


    data = zapros.json()
    if (data['media']['faces'] is None):
        return '{"faces":0}', None, None, None
    # with open('request.json', 'w') as outfile:
    #     json.dump(data,outfile,indent=4)

    the_gender, the_age =data['media']['faces'][0]['tags'][18]['value'],data['media']['faces'][0]['tags'][1]['value']

    if(the_gender=='male'):
        df=df_males
    else:
        df=df_females

    c_l = list(df['countries'])
    for item in c_l:
        if item in the_dict:
            pass
        else:
            the_dict[item] = 0

    facial_fetures={'eyes':[0,''],'nose':[0,''],'lips':[0,'']}
    if(do):
        for item in (data['media']['faces'][0]['tags']):
            if (str_not_number(item['value'])):

                for dict_item in the_dict:
                    df_country = df.loc[df.iloc[:, 0] == dict_item, :]
                    df_country_feature = df_country.loc[df_country['feature'].isin([item['name']])]


                    the_dict[dict_item] += get_similarity(df_country_feature['value'], item['value']) * (item['confidence'] + df_country_feature['confidence'].iloc[0]) / 2


    else:
        l=0
        for item in (data['media']['faces'][0]['tags']):
            if (str_not_number(item['value'])):
                i_n=0
                for dict_item in the_dict:
                    df_country = df.loc[df.iloc[:, 0] == dict_item, :]
                    df_country_feature = df_country.loc[df_country['feature'].isin([item['name']])]
                    the_similarity =get_similarity(df_country_feature['value'], item['value']) * (item['confidence'] + df_country_feature['confidence'].iloc[0]) / 2
                    #the_similarity =get_similarity(df_country_feature['value'], item['value'])


                    the_dict[dict_item] += the_mask[l]*the_similarity
                    if(i_n==8):
                        the_similarity = 100*get_similarity(df_country_feature['value'], item['value']) * (1-
                                    abs((item['confidence'] - df_country_feature['confidence'].iloc[0])))

                        if(facial_fetures['lips'][0]<the_similarity):
                            facial_fetures['lips'][0]=the_similarity
                            facial_fetures['lips'][1] = dict_item

                    if (i_n == 9):
                        the_similarity = 100*get_similarity(df_country_feature['value'], item['value']) * (1-
                                    abs((item['confidence'] - df_country_feature['confidence'].iloc[0])))

                        if (facial_fetures['nose'][0] < the_similarity):
                            facial_fetures['nose'][0] = the_similarity
                            facial_fetures['nose'][1] = dict_item


                    if (i_n == 26):
                        the_similarity = 100*get_similarity(df_country_feature['value'], item['value']) * (1-
                                    abs((item['confidence'] - df_country_feature['confidence'].iloc[0])))

                        if (facial_fetures['eyes'][0] < the_similarity):
                            facial_fetures['eyes'][0] = the_similarity
                            facial_fetures['eyes'][1] = dict_item



                    i_n+=1

            l+=1
    return the_dict,the_gender,the_age,facial_fetures

