from flask import Flask, request
from controller import controller

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hi,you can do it'


@app.route('/help', methods=["GET"])
def help():
    return controller.help()


@app.route("/calculate", methods=["POST"])
def mayby():
    data = request.json

    return str(controller.calculate(data))


@app.route("/text_redactor", methods=["POST"])
def text_red():
    data = request.json
    return str(controller.text_redactor(data))


@app.route("/parser", methods=["POST"])
def pars():
    data = request.json
    return str(controller.parser(data))


if __name__ == "__main__":
    app.run(debug=True)