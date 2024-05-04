class InvalidOperation(Exception):
    TEXT_EXCEPTION = '''Не удалось определить тип операции. 
    Ознакомиться с доступными типами можно через запрос "/help"'''


class InvalidKeys(Exception):
    TEXT_EXCEPTION = 'Не удалось определить ключи словаря. Ознакомиться с доступными ключами можно через запрос "/help '

class InvalidType(Exception):
    TEXT_EXCEPTION = 'Неверный тип данных. Ознакомиться с доступными значениями можно через запрос "/help'
