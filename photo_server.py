from flask import Flask
from flask import request
from photoDNA.beface_adapter import send_photo_for_analysis
app = Flask(__name__)


@app.route("/check")
def hello():
    return "Hello World!"

@app.route('/photo', methods=['POST'])
def photo():
    print(request.is_json)
    content = request.get_json()
    print(content)
    encoded_image = content['data']
    #send_photo_for_analysis(encoded_image)
    return send_photo_for_analysis(encoded_image)

if __name__ == "__main__":
    app.run()