from model import model
from validator import validator
import re


class Controller:
    def help(self):
        """Метод открывает файл со справкой
        Return:
            возвращает открытый файл"""
        return model.help()

    def calculate(self, data):
        """Метод производит операции по вычислению значений (сложение, вычитание, умножение и деление)
        Arg:
            data : словарь, с данными, которые передал пользователь
        Return:
            посчитанное значение, либо ошибка с ее описанием"""
        value = validator.validation_calculate(data)
        if value:
            return value
        if data["sign"] == '+':
            return data['figure1'] + data['figure2']
        elif data["sign"] == '-':
            return data['figure1'] - data['figure2']
        elif data["sign"] == '*':
            return data['figure1'] * data['figure2']
        elif data["sign"] == '/':
            if data['figure2'] == 0:
                return 'На ноль делить нельзя'
            else:
                return data['figure1'] / data['figure2']

    def text_redactor(self, data):
        """Метод производит операции по редактированию текста
              Arg:
                  data : словарь, с данными, которые передал пользователь
              Return:
                  измененный тест, либо ошибка с ее описанием"""
        value = validator.validation_text(data, 'text_redactor')
        if value:
            return value
        if data['operation'] == 'upper':
            return data['text'].upper()
        elif data['operation'] == 'lower':
            return data['text'].lower()
        elif data['operation'] == 'strip':
            return data['text'].replace(" ", '')
        elif data['operation'] == 'reverse':
            return data['operation'][::-1]

    def parser(self, data):
        """Метод производит операции по парсингу текста (находит номер телефона или email пользователя)
              Arg:
                  data : словарь, с данными, которые передал пользователь
              Return:
                    найденный текст или ошибка с ее описанием"""
        value = validator.validation_text(data, 'parser')
        if value:
            return value
        if data['operation'] == 'number':
            match = re.findall(r"\+?[\d\s\-\\]+", data['text'])
            return match[0]
        elif data['operation'] == 'email':
            match = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', data['text'])
            return match


controller = Controller()
