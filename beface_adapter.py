import base64
import requests
import json


def send_photo_for_analysis(photo_string):
    parameters_post = {
        "api_key": "d45fd466-51e2-4701-8da8-04351c872236",
        "file_base64": photo_string,
        "detection_flags": "basicpoints,propoints,classifiers,content",
        "recognize_targets": [
            "all@mynamespace"
        ],
        "original_filename": "sample.png"
    }
    zapros = requests.post('http://www.betafaceapi.com/api/v2/media',
                           json=parameters_post,
                           headers={'Content-type': 'application/json'})
    print('--------------')
    print(zapros.json())
    return str(zapros.json())
    #return json.dumps(zapros.json())
