

import boto3
import json
import os


#https://docs.aws.amazon.com/rekognition/latest/dg/celebrities-procedure-image.html
import base64

if __name__ == "__main__":
    photo = 'lady_gaga.jpg'


    client = boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.recognize_celebrities(Image={'Bytes': image.read()})


    print(response)
    print('Detected faces for ' + photo)
    for celebrity in response['CelebrityFaces']:
        print('Name: ' + celebrity['Name'])
        print('Id: ' + celebrity['Id'])
        print('Position:')
        print('   Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
        print('   Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
        print('Info')
        for url in celebrity['Urls']:
            print('   ' + url)
'''
{'UnrecognizedFaces': [], 'ResponseMetadata': {'RetryAttempts': 0, 'RequestId': '488b8081-219b-11e9-94df-4b1b6038287e', 'HTTPHeaders': {'content-length': '848', 'content-type': 'application/x-amz-json-1.1', 'x-amzn-requestid': '488b8081-219b-11e9-94df-4b1b6038287e', 'date': 'Sat, 26 Jan 2019 18:50:43 GMT', 'connection': 'keep-alive'}, 'HTTPStatusCode': 200}, 'CelebrityFaces': [{'MatchConfidence': 100.0, 'Id': '4Fn1Te4k', 'Name': 'Lady Gaga', 'Face': {'Landmarks': [{'Type': 'eyeLeft', 'Y': 0.29353976249694824, 'X': 0.43712693452835083}, {'Type': 'eyeRight', 'Y': 0.286601722240448, 'X': 0.5805856585502625}, {'Type': 'nose', 'Y': 0.369806706905365, 'X': 0.5184049606323242}, {'Type': 'mouthLeft', 'Y': 0.4467722475528717, 'X': 0.46059727668762207}, {'Type': 'mouthRight', 'Y': 0.44681984186172485, 'X': 0.5675793290138245}], 'Confidence': 99.99964141845703, 'BoundingBox': {'Width': 0.44857141375541687, 'Height': 0.44999998807907104, 'Top': 0.10428571701049805, 'Left': 0.28285714983940125}, 'Pose': {'Yaw': 6.803795337677002, 'Pitch': 1.7343127727508545, 'Roll': -3.6946663856506348}, 'Quality': {'Sharpness': 98.57371520996094, 'Brightness': 94.35513305664062}}, 'Urls': ['www.imdb.com/name/nm3078932']}], 'OrientationCorrection': 'ROTATE_0'}
Detected faces for lady_gaga.jpg
Name: Lady Gaga
Id: 4Fn1Te4k
Position:
   Left: 0.45
   Top: 0.10
Info
   www.imdb.com/name/nm3078932

'''