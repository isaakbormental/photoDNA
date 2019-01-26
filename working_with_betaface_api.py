
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


links=['https://i.ibb.co/9wSn6cr/afhganistan.png','https://i.ibb.co/nm4gL5x/argentina.png','https://i.ibb.co/J5B4Xqh/austria.png','https://i.ibb.co/fdTmM2R/burma.png','https://i.ibb.co/cr3nyyz/germany.png','https://i.ibb.co/ZNdBYXC/greece.png','https://i.ibb.co/2vFbXTZ/india.png','https://i.ibb.co/B45HPgL/iran.png']
countries=['afghanistan','argentina','austria','burma','germany','greece','india','iran']
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

  #print(data)































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