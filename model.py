import json


class Model:
    def open(self, file):
        with open(file, 'r') as file:
            return json.loads(file.read())

    def help(self):
        with open('help.text', encoding='utf-8', mode='r') as file:
            return file.read()


model = Model()