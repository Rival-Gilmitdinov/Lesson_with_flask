from my_exceptions import InvalidSign, InvalidKeys, InvalidType


class Validator:
    def validate_type(self, data, t_data):
        """Метод по проверке типа переданных данных
        Arg:
            data: переданные значения
            t_data: тип данных, который проверяется
        Raise:
            Ошибка, в случае, если типы данных не совпадают"""
        if not isinstance(data, t_data):
            raise TypeError('Неверный тип данных')

    def validate_sign(self, sign):
        """Метод по проверки правильности введенного знака
        Arg:
            sign: Знак, который ввел пользователь
        Raise:
            ошибка, если пользователь ввел неккорекный знак"""
        if sign not in ('+', '-', '/', '*'):
            raise InvalidSign

    def validate_keys(self, data):
        """Метод по проверке введенных ключей
        Arg:
            data: переданные данные
        Raise:
             ошибка, если пользователь ввел неккорекный ключ """
        if "figure1" not in data.keys() or "figure2" not in data.keys() or "sign" not in data.keys():
            raise InvalidKeys


    def validate_type_value(self, data):
        """Метод по проверки правильности типов данных
         Arg:
            data: переданные данные
        Raise:
             ошибка, если пользователь ввел неккорекный тип"""
        if type(data['figure1']) != int or type(data['figure2']) != int or type(data['sign']) != str:
            raise InvalidType

    def validate_text_keys(self, data):
        """Метод по проверке введенных ключей в текстовый редактор
        Arg:
            data: переданные данные
        Raise:
             ошибка, если пользователь ввел неккорекный ключ """
        if 'operation' not in data.keys() or 'text' not in data.keys():
            raise InvalidKeys

    def validate_text_type(self, data):
        """Метод по проверки правильности типов данных в текстовом редакторе
            Arg:
                data: переданные данные
            Raise:
                ошибка, если пользователь ввел неккорекный тип"""
        if type(data['text']) != str or type(data['operation']) != str:
            raise InvalidType


validator = Validator()