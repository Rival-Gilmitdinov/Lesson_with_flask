from flask import Flask, request
from controller import controller

app = Flask(__name__)

@app.route('/')
def hello():
    """Функция создает сервер с возвращенными значениями"""
    return 'Hi,you can do it'


@app.route('/help', methods=["GET"])
def help():
    """Функция создает сервер со справкой для дальнейшей работы"""
    return controller.help()


@app.route("/calculate", methods=["POST"])
def mayby():
    """Функция создает сервер, выполняющего функция калькулятора
    Return:
        вычисленные данные в формате str"""
    data = request.json
    return str(controller.calculate(data))


@app.route("/text_redactor", methods=["POST"])
def text_red():
    """Функция создает сервер, выполняющего функция текстового редактора
    Return:
        отредактированные данные в формате str"""
    data = request.json
    return str(controller.text_redactor(data))


@app.route("/parser", methods=["POST"])
def pars():
    """Функция создает сервер, выполняющего функцию парсинга текста
    Return:
        извлеченные данные в формате str"""
    data = request.json
    return str(controller.parser(data))


if __name__ == "__main__":
    app.run(debug=True)