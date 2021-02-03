from datetime import datetime
from random import randint, seed

from flask import Flask, jsonify, request

seed(datetime.now())
SECRET_NUM = randint(0, 1024)

app = Flask(__name__)


@app.route("/hello-world", methods=["GET"])
def hello_world():
    return_string = "Hello World!"
    if request.args:
        print(request.args)
        try:
            upper_case = request.args["upper"].lower()
        except KeyError:
            return "wrong parameter", 400
        if upper_case == "true":
            return_string = "HELLO WORLD!"
        elif upper_case == "false":
            return_string = "hello world!"
        else:
            return jsonify({"error": "True or False only"}), 400
    return jsonify({"response": return_string}), 200


@app.route("/get-secret", methods=["GET"])
def get_secret():
    return jsonify({"number": SECRET_NUM}), 200


@app.route("/check-secret", methods=["POST"])
def check_secret():
    # enough for demo- number should be changed after successful check
    global SECRET_NUM
    r = request.get_json()
    try:
        to_check = r["secret"]
    except KeyError:
        return jsonify({"error": "no number passed"}), 400

    if isinstance(to_check, int):
        if to_check == SECRET_NUM:
            SECRET_NUM = randint(0, 1024)
            return jsonify({"check": "OK"}), 200
        else:
            return jsonify({"check": "FAILED"}), 400
    else:
        return jsonify({"error": "value must be an integer"}), 400


@app.route("/double", methods=["POST"])
def double_number():
    r = request.get_json()
    try:
        number = r["number"]
    except (KeyError, TypeError):
        return jsonify({"error": "no number passed"}), 400

    try:
        double = int(number)*2
    except ValueError:
        return jsonify({"error": "a number was not passed"}), 400

    return jsonify({"double": double}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
