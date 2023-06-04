from model.reader_utils import get_list_readers, readers_to_texts, find_reader, replace_reader
from utils.file_utils import write_text, write_texts
from utils.input_utils import input_info_reader, input_name_reader, input_phone_number_reader, input_email_reader, \
    input_id_reader


def add_info_reader():
    """
        thêm độc giả mới
    :return:
    """
    # nhập thông tin của độc giả
    name, phone_number, email = input_info_reader()
    # Lấy danh sách tất cả các độc giả ở trong dữ liệu (file text)
    readers = get_list_readers()
    # Kiểm tra xem email tồn tại chưa
    reader_by_email = find_reader(readers, email, "email")
    # Nếu email tồn tại trong dữ liệu thì yêu cầu nhập lại email
    while len(reader_by_email) > 0:
        print("Email của bạn đã bị trùng với độc giả khác")
        email = input_email_reader()
        reader_by_email = find_reader(readers, email, "email")
    # Kiểm tra xem số điện thoại tồn tại chưa
    reader_by_phone_number = find_reader(readers, phone_number, "phone_number")
    # Nếu số điện thoại tồn tại trong dữ liệu thì yêu cầu nhập lại số điện thoại
    while len(reader_by_phone_number) > 0:
        print("Số điện thoại của bạn đã bị trùng với độc giả khác\n Xin mời bạn nhập lại số điện thoại")
        phone_number = input_phone_number_reader()
        reader_by_phone_number = find_reader(readers, phone_number, "phone_number")
    # tạo object reader(độc giả)

    id = int(readers[-1]['id']) + 1 if len(readers) > 0 else 0
    text_reader = f"{id}\t{name}\t{phone_number}\t{email}"
    # Lưu dữ liệu vào file text
    write_text(text_reader)
    print("\t\t\t\t\t\t****\n\t\t\tĐã thêm độc giả mới thành công")


def delete_info_reader():
    """
    Xóa thông tin của độc giả theo:
        1: theo sdt ( xóa 1 độc giả vì sdt không thể 2 ngừoi chung)
        2: theo email ( xóa độc giả vì email không thể 2 người chung)
        3: theo id ( xóa độc giả vì email không thể 2 người chung)
    :return:
        thông báo thành công hoặc không tìm thấy độc giả như yêu cầu để xóa
    """
    print("""*** Hãy chọn cách xóa ***
    2.1 Xóa độc giả theo số điện thoại
    2.2 Xóa độc giả theo email
    2.3 Xóa độc giả theo id 
    Ví dụ nhập: 2.1
           ****       
    """)
    dict_option = {
        "2.1": ["số điện thoại", "phone_number"],
        "2.2": ["email"],
        "2.3": ["id"]
    }
    # Lấy danh sách tất cả các độc giả ở trong dữ liệu (file text)
    readers = get_list_readers()
    text = None
    option = None
    # Chọn xem xóa theo số điện thoại hay theo email
    while text is None:
        option = input("Nhập sự lựa chọn của bạn:").strip()
        match option:
            case "2.1":
                # nhập số điện thoại
                text = input_phone_number_reader()
            case "2.2":
                # nhập email
                text = input_email_reader()
            case "2.3":
                # nhập id
                text = input_id_reader()
            case _:
                print("Bạn đã nhập sai, xin mời bạn nhập lại:")
    # tìm kiếm độc giả theo input vừa nhập và theo option chọn ban đầu
    readers_found = find_reader(readers, text, type=dict_option[option][-1])

    # kiểm tra reader có tồn tại không
    if len(readers_found) > 0:
        # Xóa độc giả vừa tìm được
        readers.remove(readers_found[-1])
        # chuyển thành một danh sách text
        reader_texts = readers_to_texts(readers)
        # Lưu dữ liệu vào file text
        write_texts(reader_texts)
        print("Xóa thành công!!!")
    else:
        print(f"Không tìm thấy độc giả có {dict_option[option][0]} là {text}")


def display_readers():
    """
         Hiện thị thông tin của tất cả độc
    """
    # Lấy danh sách tất cả các độc giả ở trong dữ liệu (file text)
    readers = get_list_readers()
    # Duyệt vòng for để hiện thị thông tin của độc giả
    if readers:
        for reader in readers:
            print(reader.to_text() + "\n")
    else:
        print("\n ***Không có độc giả nào trong danh sách***")


def update_info_reader():
    print("""*** Hãy chọn cách cập nhật ***
    3.1 cập nhật độc giả theo số điện thoại
    3.2 cập nhật độc giả theo email
    3.3 cập nhật độc giả theo id
    Ví dụ nhập: 3.1
           ****       
    """)
    dict_option = {
        "3.1": ["số điện thoại", "phone_number"],
        "3.2": ["email"],
        "3.3": ["id"]
    }
    # Lấy danh sách tất cả các độc giả ở trong dữ liệu (file text)
    readers = get_list_readers()
    option = None
    reader_new = None
    # Lựa chọn option đến khi nào nhập đúng là 3.1 or 3.2
    while reader_new is None:
        option = input("Nhập lựa chọn của bạn:").strip()
        print("*************")
        # kiểm tra option trong danh sách không
        if option in dict_option.keys():
            # nhập thông tin của độc giải
            id = None
            if option == "3.3":
                id = input_id_reader()
            name, phone_number, email = input_info_reader()
            reader_new = {
                "name": name,
                "phone_number": phone_number,
                "email": email
            }
            if id is not None:
                reader_new['id'] = id
        else:
            print("Bạn đã nhập sai, xin mời bạn nhập lại:")

        # Tìm kiếm độc giả theo yêu cầu
        reader_old = find_reader(readers, reader_new[dict_option[option][-1]], dict_option[option][-1])

    # kiểm tra độc giả có tồn tại không, không thì hiện thị ra thông cáo không tìm thấy
    if len(reader_old) > 0:
        # thay thế độc giả cũ thành độc giả mới
        reader_new['id'] = reader_old[-1]['id']  # lấy id của độc giả cũ
        readers = replace_reader(readers, reader_old[-1], reader_new)
        # Chuyển thành text rồi lưu vào file text
        reader_texts = readers_to_texts(readers)
        write_texts(reader_texts)
        print("Cập nhật thành công thành công!!!")
    else:
        print(f"Không tìm thấy độc giả có {dict_option[option][0]} là {reader_new[dict_option[option][-1]]}")


def find_info_reader():
    print("""*** Hãy chọn cách xóa ***
    4.1 Tìm kiếm độc giả theo tên
    4.2 Tìm kiếm độc giả theo số điện thoại
    4.3 Tìm kiếm độc giả theo email
    4.4 Tìm kiếm độc giả theo id 
    Ví dụ nhập: 4.1
           ****       
    """)
    dict_option = {
        "4.1": ["tên", "name"],
        "4.2": ["số điện thoại", "phone_number"],
        "4.3": ["email"],
        "4.4": ["id"]
    }
    readers = get_list_readers()
    text = None
    option = None
    # chọn option
    while text is None:
        option = input("Nhập lựa chọn của bạn:").strip()
        match option:
            case "4.1":
                # nhập tên độc giả cần tìm kiếm
                text = input_name_reader()
            case "4.2":
                # nhập số điện thoại độc giả cần tìm kiếm
                text = input_phone_number_reader()
            case "4.3":
                # nhập email độc giả cần tìm kiếm
                text = input_email_reader()
            case "4.4":
                text = input_id_reader()
            case _:
                print("Bạn đã nhập sai, xin mời bạn nhập lại:")
    # Tìm kiếm đọc giả theo mục lựa chọn

    readers_found = find_reader(readers, text, dict_option[option][-1])

    if readers_found:  # kiểm tra xem độc giả tổn tại hay không ( nếu reader = None hoặc = [] => False, nếu khác 2 trường hợp khác thì trả về True
        readers_text = readers_to_texts(readers_found)
        for text in readers_text:
            print(text)

    else:
        print(f"\nKhông tìm thấy độc giả có {dict_option[option][0]} là {text}")


def display_menu():
    print("""
        ---------Chương trình quản lí đọc giả---------

        ********************Menu********************
        0. Thoát khỏi chương trình
        1. Nhập thông tin độc giả
        2. Xóa thông tin độc giả 
        3. Cập nhật thông tin độc giả
        4. Tìm kiếm thông tin độc giả
        5. Hiển thị danh sách độc giả
        6. Hiện thị lại menu
        *******************************************

        """)
