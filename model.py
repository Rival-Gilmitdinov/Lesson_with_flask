import json


class Model:
    def help(self):
        """Метод для открытия текстового файла со справкой
        Return:
            текст файла"""
        with open('help.text', encoding='utf-8', mode='r') as file:
            return file.read()


model = Model()