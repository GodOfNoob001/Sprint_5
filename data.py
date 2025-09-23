import random


def random_valid_mail():
    return f"alexdmiterko30{random.randint(100, 9999)}@ya.ru"


def random_invalid_mail():
    return f"alexdmiterko30{random.randint(100, 9999)}"


class Data:
    valid_login = 'alexdmiterko301212@ya.ru'
    valid_password = 'YaPraktikum123'
    valid_name = 'Александр'
    random_valid_mail = f"alexdmiterko30{random.randint(100, 9999)}@ya.ru"
    random_invalid_mail = f"alexdmiterko30{random.randint(100, 9999)}"
    invalid_passwords = ['1', '12', '123', '1234', '12345']
    valid_passwords = ['123456', '123456P', '123456PRAKTIKUM']
    error_text = 'Некорректный пароль'

