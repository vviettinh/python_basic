from utils.func_main import add_info_reader, delete_info_reader, display_readers, \
    update_info_reader, find_info_reader, display_menu

def main():
    display_menu()
    while True:
        option_number = input(
            "\t\t\t\t\t\t****\t\t\t\t\t\t\nXin mời nhập số tương ứng với lựa chọn của bạn (0-6):").strip()
        match option_number:
            case '1':
                # add information reader
                add_info_reader()
            case '2':
                # delete information reader
                delete_info_reader()
            case '3':
                # update information reader
                update_info_reader()
            case '4':
                # find information reader
                find_info_reader()
            case '5':
                # display readers
                display_readers()
            case '6':
                # display hiện thị lại menu
                display_menu()
            case '0':
                # exit
                print("--- Bạn đã thoát thành công ---")
                exit()
            case _:
                print("\nYêu cầu của bạn chưa có trong menu")
                print("\n Xin hãy nhập lại")


if __name__ == "__main__":
    main()
