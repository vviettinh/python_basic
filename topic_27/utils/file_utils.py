PATH_FILE = './data/reader.txt'


def read_file_text():
    """
        đọc file
        :return: dự liệu trong file text
        """
    with open(PATH_FILE, 'r') as f:
        data = f.read()
    return data


def write_texts(texts):
    """
        Lưu text vào file
        :param text: thông tin của các độc giả
        :return:
        """
    if texts:
        with open(PATH_FILE, 'w') as f:
            for text in texts:
                f.write(text + "\n")
    else:
        with open(PATH_FILE, 'w') as f:
            f.write("")


def write_text(text):
    """
    Lưu text vào file
    :param text: thông tin của 1 độc giả
    :return:
    """
    with open(PATH_FILE, 'a+') as f:
        f.write(text + "\n")
