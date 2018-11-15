#!/usr/bin/python3.5
import base64
import io
import uuid
from datetime import datetime, timedelta
from copy import deepcopy
from PIL import Image
from flask import Flask, make_response, request, json

from app import app
import app.emotion_gender_processor as eg_processor

_DEBUG = False


@app.route('/emotion_classificator/1.0', methods=['POST'])
def classify_emotion():
    if _DEBUG:
        img = Image.open('./app/t1.jpg', mode='r')
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        start_time = datetime.now()

        prediction_result = eg_processor.emotion_classificator(img_byte_arr)

        delta = datetime.now() - start_time

        print('delta for emotion {0}'.format(delta.total_seconds() * 1000.0))
    else:
        if (not is_valid_request(request)):
            return json.jsonify(get_json_response(msg='Invalid request'))

        img_b64, _ = get_request_data(request)
        img_body = get_image_body(img_b64)

        if (img_body is None):
            return json.jsonify(get_json_response(msg='Image not found'))

        start_time = datetime.now()

        prediction_result = eg_processor.emotion_classificator(img_body)

        delta = datetime.now() - start_time

        if (prediction_result == []):
            return json.jsonify(get_json_response())

    # print(delta.total_seconds() * 1000.0)
    print(prediction_result)
    return json.jsonify(get_json_response(prediction_result))


@app.route('/gender_classificator/1.0', methods=['POST'])
def classify_gender():
    if (not is_valid_request(request)):
        return json.jsonify(get_json_response(msg='Invalid request'))

    img_b64, _ = get_request_data(request)
    img_body = get_image_body(img_b64)

    if (img_body is None):
        return json.jsonify(get_json_response(msg='Image not found'))

    start_time = datetime.now()

    prediction_result = eg_processor.gender_classificator(img_body)

    delta = datetime.now() - start_time

    if (prediction_result == []):
        return json.jsonify(get_json_response())

    print(delta.total_seconds() * 1000.0)
    print(prediction_result)
    return json.jsonify(get_json_response(prediction_result))


@app.route('/age_classificator/1.0', methods=['POST'])
def classify_age():
    if (not is_valid_request(request)):
        return json.jsonify(get_json_response(msg='Invalid request'))

    img_b64, _ = get_request_data(request)
    img_body = get_image_body(img_b64)

    if (img_body is None):
        return json.jsonify(get_json_response(msg='Image not found'))

    start_time = datetime.now()

    prediction_result = eg_processor.age_classificator(img_body)

    delta = datetime.now() - start_time

    if (prediction_result == []):
        return json.jsonify(get_json_response())

    print(delta.total_seconds() * 1000.0)
    print(prediction_result)
    return json.jsonify(get_json_response(prediction_result))


def is_valid_request(request):
    return 'image' in request.json


def get_request_data(request):
    r = request.json
    image = r['image'] if 'image' in r else ''
    min_accuracy = r['minAccuracy'] if 'minAccuracy' in r else 60
    return image, min_accuracy


def get_image_body(img_b64):
    if 'data:image' in img_b64:
        img_encoded = img_b64.split(',')[1]
        return base64.decodebytes(img_encoded.encode('utf-8'))
    else:
        return None


def get_json_response(result=None, msg=None):
    json = {
        'success': False
    }

    if msg is not None:
        json['message'] = msg
        return json

    json['data'] = []

    if result is None:
        return json

    for item in result:
        d = {}
        if 'face_bound' in item:
            d['faceRectangle'] = {
                'left': item['face_bound'][0],
                'top': item['face_bound'][1],
                'width': item['face_bound'][2],
                'heigth': item['face_bound'][3]
            }
        if 'emotion' in item:
            d['emotionInfo'] = {
                'emotion': item['emotion'].split(':')[0],
                'confident': item['emotion'].split(':')[1]
            }
        if 'gender' in item:
            d['genderInfo'] = {
                'gender': item['gender'].split(':')[0],
                'confident': item['gender'].split(':')[1]
            }
        if 'age' in item:
            d['age'] = item['age']
        json['data'].append(deepcopy(d))

    json['success'] = True
    return json

# if __name__ == '__main__':
#     # eg_processor.load_models()
#     app.run(port='8080', debug=True)
