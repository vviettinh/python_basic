import re


def is_valid_name(name):
    # Khai báo biểu thức chính quy để kiểm tra định dạng tên người Việt
    pattern = r'^[a-zA-ZÀ-Ỹà-ỹ]+([\s][a-zA-ZÀ-Ỹà-ỹ]+)*$'
    # So khớp biểu thức chính quy với chuỗi tên đầu vào
    match = re.match(pattern, name)
    # Kiểm tra kết quả so khớp để xác định tên hợp lệ hay không
    if match:
        return True
    else:
        return False


def is_valid_phone_number(phone_number):
    # Khai báo biểu thức chính quy để kiểm tra định dạng số điện thoại
    pattern = r'^\+?\d{1,3}[-\.\s]?\d{3,4}[-\.\s]?\d{4}$'
    # So khớp biểu thức chính quy với chuỗi số điện thoại đầu vào
    match = re.match(pattern, phone_number)
    # Kiểm tra kết quả so khớp để xác định số điện thoại hợp lệ hay không
    if match:
        return True
    else:
        return False


def is_valid_email(email):
    # Khai báo biểu thức chính quy để kiểm tra định dạng email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # So khớp biểu thức chính quy với chuỗi email đầu vào
    match = re.match(pattern, email)
    # Kiểm tra kết quả so khớp để xác định email hợp lệ hay không
    if match:
        return True
    else:
        return False
