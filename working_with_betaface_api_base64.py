
import requests
import json

'''
https://imgbb.com/

bbc code full linked

[url=https://imgbb.com/][img]https://i.ibb.co/9wSn6cr/afhganistan.png[/img][/url]
[url=https://imgbb.com/][img]https://i.ibb.co/nm4gL5x/argentina.png[/img][/url]
[url=https://imgbb.com/][img]https://i.ibb.co/J5B4Xqh/austria.png[/img][/url]
[url=https://imgbb.com/][img]https://i.ibb.co/fdTmM2R/burma.png[/img][/url]
[url=https://imgbb.com/][img]https://i.ibb.co/cr3nyyz/germany.png[/img][/url]
[url=https://imgbb.com/][img]https://i.ibb.co/ZNdBYXC/greece.png[/img][/url]
[url=https://imgbb.com/][img]https://i.ibb.co/2vFbXTZ/india.png[/img][/url]
[url=https://imgbb.com/][img]https://i.ibb.co/B45HPgL/iran.png[/img][/url]

'''
import os
import base64

with open("lesha.jpg", "rb") as image_file:
  encoded_string = image_file.read()
print(base64.b64encode(encoded_string).decode('ascii'))
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
with open('lesha.json', 'w') as outfile:
  json.dumps(data, outfile)


print(data)































'''


parameters_post = {
  "api_key": "d45fd466-51e2-4701-8da8-04351c872236",
  "file_uri": "http://betafaceapi.com/api_examples/sample.png",
  "detection_flags": "basicpoints,propoints,classifiers,content",
  "recognize_targets": [
    "all@mynamespace"
  ],
  "original_filename": "sample.png"
}

zapros=requests.post('http://www.betafaceapi.com/api/v2/media', json=parameters_post, headers={'Content-type': 'application/json'})

data=zapros.json()
print(data)




'''