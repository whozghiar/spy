from flask import Flask, jsonify
from app.composants.screenshot import take_screenshot
from app.composants.webcam import take_webcam_photo
from app.composants.system import get_system_info

app = Flask(__name__)


@app.route('/screenshot', methods=['GET'])
def screenshot():
    base64_image, filename = take_screenshot()
    return jsonify({"filename": filename, "image": base64_image})


@app.route('/webcam', methods=['GET'])
def webcam():
    base64_image, filename = take_webcam_photo()
    return jsonify({"filename": filename, "image": base64_image})


@app.route('/systeminfo', methods=['GET'])
def systeminfo():
    system_info = get_system_info()
    return jsonify(system_info)
