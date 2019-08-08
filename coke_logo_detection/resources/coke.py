from flask_restful import Resource,request
from flask import jsonify
from coke_logo_detection.models.coke import CokeModel
import os
from coke_logo_detection.definitions import IMAGE_PATH


class Coke(Resource):
    def post(self):
        try:
            if os.path.exists(IMAGE_PATH):
                os.remove(IMAGE_PATH)

            file = request.files['image']
            file.save(IMAGE_PATH)
            try:
                coke_detector = CokeModel()
                coke_detector.detect_coke_logo()
                result = coke_detector.json()
                print(result)
                return jsonify(result)
            except Exception as e:
                return {"message": "{}".format(e)}, 400

        except:
            return {"message": "Can't upload image"}, 500

