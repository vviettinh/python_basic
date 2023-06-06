from utils.file_utils import read_file_text


def get_list_readers():
    """
    Lấy danh sách độc giả từ file text và đưa vào list
    :return: list of readers
    """
    data = read_file_text()
    readers = []
    if len(data):
        lines = data.strip().split('\n')
        for line in lines:
            id, name, phone_number, email = line.split('\t')
            reader = {
                "id": id,
                "name": name,
                "phone_number": phone_number,
                "email": email
            }
            readers.append(reader)
    return readers


def readers_to_texts(readers):
    """
     chuyển các reader thành text
    :param readers: danh sách độc giả
    :return:
    """
    texts = []
    for reader in readers:
        text = to_text(reader)
        texts.append(text)
    return texts


def delete_reader(readers, text, type):
    """
    xóa độc giả theo text theo loại id/ phone number / email
    :param readers: list of reader
    :param text:  thông tin của độc giả cần xóa
    :param type: loại theo id / phone number / email
    :return:
    """
    for reader in readers:
        if reader[type] == text:
            readers.remove(reader)
            return readers
    return None


def replace_reader(readers, reader_old, reader_new):
    """
    thay thế độc giả cần thay đổi
    :param readers: danh sách độc giả
    :param reader_old: độc giả cần thay đổi
    :param reader_new:  độc giả mới
    :return:
    """
    index_reader = readers.index(reader_old)
    readers[index_reader] = reader_new
    return readers


def find_reader(readers, text, type):
    """
       Tìm kiếm độc giả theo email
       :param readers: danh sách độc giả
       :param text: thông tin của độc giả
       :param type: id/email/phone_number
       :return:
           độc giả cần tìm theo email
   """
    res = []
    for reader in readers:
        if reader[type] == text:
            res.append(reader)
    return res


def to_text(reader):
    return f"{reader['id']}\t{reader['name']}\t{reader['phone_number']}\t{reader['email']}"
