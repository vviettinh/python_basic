from utils.re_utils import is_valid_name, is_valid_phone_number, is_valid_email
from utils.string_utils import name_normalize


def input_info_reader():
    """
    Nhập tên, sdt, email của độc giả
    :return:
    """
    name = input_name_reader()
    phone_number = input_phone_number_reader()

    email = input_email_reader()

    return name, phone_number, email


def input_name_reader():
    """
        Nhập tên  của độc giả
        :return:
        """
    name = input("Nhập họ và tên của độc giả: ")
    name = name_normalize(name)
    while not is_valid_name(name):
        name = input("""
        Bạn đang nhập sai định dạng của tên người,
        Ví dụ đúng: "Nguyễn Văn A", "Nguyen Van A", "nguyen van a", "john Doe"
        Xin mời bạn nhập lại tên của độc giả: 
                        """)
        name = name_normalize(name)
    return name


def input_phone_number_reader():
    """
        Nhập sdt của độc giả
        :return:
        """
    phone_number = input("Nhập số điện thoại của độc giả: ").strip()

    while not is_valid_phone_number(phone_number):
        phone_number = input("""
    Bạn đang nhập sai định dạng của số điện thoại,
    Ví dụ đúng: '0987654321', '+84987654321', '123-456-7890'
    Ví dụ sai: '0123456789'
    , Xin mời bạn nhập lại số điện thoại của độc giả: 
                                """)
    return phone_number


def input_email_reader():
    """
        Nhập email của độc giả
        :return:
    """
    email = input("Nhập email của độc giả: ").strip()
    while not is_valid_email(email):
        email = input("""
    Bạn đang nhập sai định dạng của email,
    Ví dụ đúng: 'abc@example.com', 'abc.def@example.com', 'abc123@example.com'
    Ví dụ sai: 'abc@example', 'abc@.com'
    , Xin mời bạn nhập lại email của độc giả: 
                    """)
    return email


def input_id_reader():
    id = input("Nhập id của độc giả: ").strip()
    return id
