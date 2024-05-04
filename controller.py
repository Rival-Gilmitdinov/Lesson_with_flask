from model import model
from validator import validator
from my_exceptions import InvalidSign, InvalidKeys, InvalidType
import re


class Controller:
    def help(self):
        return model.help()

    def calculate(self, data):
        try:
            validator.validate_type(data, dict)
        except TypeError:
            return 'Неверный тип данных, передайте данные в словаре, для более ' \
                   'детальной информации обратитесь к запросу "/help"'
        try:
            validator.validate_sign(data['sign'])
        except InvalidSign as error:
            return error.TEXT_EXCEPTION
        try:
            validator.validate_keys(data)
        except InvalidKeys as error:
            return error.TEXT_EXCEPTION
        try:
            validator.validate_type_value(data)
        except InvalidType as error:
            return error.TEXT_EXCEPTION
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
        try:
            validator.validate_type(data, dict)
        except TypeError:
            return 'Неверный тип данных, передайте данные в словаре, для более ' \
                   'детальной информации обратитесь к запросу "/help"'
        try:
            validator.validate_text_keys(data)
        except InvalidKeys as error:
            return error.TEXT_EXCEPTION
        try:
            validator.validate_text_type(data)
        except InvalidType as error:
            return error.TEXT_EXCEPTION
        if data['operation'] == 'upper':
            return data['text'].upper()
        elif data['operation'] == 'lower':
            return data['text'].lower()
        elif data['operation'] == 'strip':
            return data['text'].replace(" ", '')
        elif data['operatinon'] == 'reverse':
            return data['operation'][::-1]
        else:
            raise SyntaxError('operation not found')

    def parser(self, data):
        try:
            validator.validate_type(data, dict)
        except TypeError:
            return 'Неверный тип данных, передайте данные в словаре, для более ' \
                   'детальной информации обратитесь к запросу "/help"'
        try:
            validator.validate_text_keys(data)
        except InvalidKeys as error:
            return error.TEXT_EXCEPTION
        try:
            validator.validate_text_type(data)
        except InvalidType as error:
            return error.TEXT_EXCEPTION

        if data['operation'] == 'number':
            match = re.findall(r"\+?[\d\s\-\\]+", data['text'])
            return match[0]
        elif data['operation'] == 'email':
            match = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', data['text'])
            return match
        else:
            return "Неверная операция"


controller = Controller()
