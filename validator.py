from my_exceptions import InvalidOperation, InvalidKeys, InvalidType


class Validator:
    def validate_type(self, data, t_data):
        """Метод по проверке типа переданных данных
        Arg:
            data: переданные значения
            t_data: тип данных, который проверяется
        Raise:
            Ошибка, в случае, если типы данных не совпадают"""
        if not isinstance(data, t_data):
            raise InvalidType

    def validate_operation(self, operation, list_operation):
        """Метод по проверки правильности введенного знака
        Arg:
            sign: Знак, который ввел пользователь
        Raise:
            ошибка, если пользователь ввел неккорекный знак"""
        if operation not in list_operation:
            raise InvalidOperation

    def validate_keys(self, data, keys_list):
        """Метод по проверке введенных ключей
        Arg:
            data: переданные данные
        Raise:
             ошибка, если пользователь ввел неккорекный ключ """
        for key in keys_list:
            if key not in data.keys():
                raise InvalidKeys

    def validation_calculate(self, data):
        try:
            self.validate_type(data, dict)
        except InvalidType as error:
            return error.TEXT_EXCEPTION
        try:
            self.validate_keys(data, ['figure1', 'figure2', 'sign'])
        except InvalidKeys as error:
            return error.TEXT_EXCEPTION
        try:
            self.validate_operation(data['sign'], ('+', '-', '*', '/'))
        except InvalidOperation as error:
            return error.TEXT_EXCEPTION
        try:
            self.validate_type(data['figure1'], (float, int))
            self.validate_type(data['figure1'], (float, int))
            self.validate_type(data["sign"], str)
        except InvalidType as error:
            return error.TEXT_EXCEPTION

    def validation_text(self, data, type_request):
        try:
            self.validate_type(data, dict)
        except InvalidType as error:
            return error.TEXT_EXCEPTION
        try:
            self.validate_keys(data, ['operation', 'text'])
        except InvalidKeys as error:
            return error.TEXT_EXCEPTION
        try:
            if type_request == 'text_redactor':
                self.validate_operation(data['operation'], ('upper', 'lower', 'reverse', 'strip'))
            elif type_request == 'parser':
                self.validate_operation(data['operation'], ('number', 'email'))
        except InvalidOperation as error:
            return error.TEXT_EXCEPTION
        try:
            self.validate_type(data['operation'], str)
            self.validate_type(data['text'], str)
        except InvalidType as error:
            return error.TEXT_EXCEPTION


validator = Validator()