from my_exceptions import InvalidSign, InvalidKeys, InvalidType


class Validator:
    def validate_type(self, data, t_data):
        if not isinstance(data, t_data):
            raise TypeError('Неверный тип данных')

    def validate_sign(self, sign):
        if sign not in ('+', '-', '/', '*'):
            raise InvalidSign

    def validate_keys(self, data):
        if "figure1" not in data.keys() or "figure2" not in data.keys() or "sign" not in data.keys():
            raise InvalidKeys


    def validate_type_value(self, data):
        if type(data['figure1']) != int or type(data['figure2']) != int or type(data['sign']) != str:
            raise InvalidType

    def validate_text_keys(self, data):
        if 'operation' not in data.keys() or 'text' not in data.keys():
            raise InvalidKeys

    def validate_text_type(self, data):
        if type(data['text']) != str or type(data['operation']) != str:
            raise InvalidType


validator = Validator()