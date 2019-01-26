from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/check")
def hello():
    return "Hello World!"

@app.route('/photo', methods=['POST'])
def photo():
    print(request.is_json)
    content = request.get_json()
    print(type(content))
    encoded_image = content['data']
    return 'JSON posted'

def extract_photo_from_json():
    return

if __name__ == "__main__":
    app.run()