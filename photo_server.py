from flask import Flask
from flask import request
from flask_cors import CORS
from beface_adapter import send_photo_for_analysis
app = Flask(__name__)
CORS(app)

@app.route("/check")
def hello():
    return "Hello World!"

@app.route('/photo', methods=['POST'])
def photo():
    print(request.is_json)
    content = request.get_json()
    print(content)
    print()
    print(content['img'].split(',', 1)[1])
    encoded_image = content['img'].split(',', 1)[1]
    #send_photo_for_analysis(encoded_image)
    return send_photo_for_analysis(encoded_image)

if __name__ == "__main__":
    app.run()