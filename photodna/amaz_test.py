import boto3

s3 = boto3.client('s3')

with open('imaga.jpg', 'rb') as data:
    response = s3.upload_fileobj(data, 'storage.ws.pho.to', 'photohack/stckrs/image-test-server.png')


print(response)
