import re


def is_valid_name(name):
    # Kiểm tra xem tên có rỗng hay không
    if not name:
        return False
    # Kiểm tra từng ký tự trong tên
    for char in name:
        if not char.isalpha() and char != ' ':
            return False
    # Nếu tên đạt đủ các điều kiện trên thì trả về True
    return True


def is_valid_phone_number(phone_number):
    # Kiểm tra độ dài của số điện thoại
    if len(phone_number) != 10:
        return False
    # Kiểm tra từng ký tự trong số điện thoại
    for char in phone_number:
        if not char.isdigit():
            return False
    # Nếu số điện thoại đạt đủ các điều kiện trên thì trả về True
    return True


def is_valid_email(email):
    if email is not None and len(email) > 1 and '@' in email and email[0] != '@' and email[-1] != '@':
        return True
    return False
