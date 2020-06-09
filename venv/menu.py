# coding=utf-8
import pick_menu
import rest_info
import my_rest

def show_menu():
    print("1. 메뉴 골라주기")
    print("2. 식당 정보")
    print("3. 단골 가게")
    print("4. 종료")

def pick_num():
    while True:
        show_menu()
        input_num = input("번호를 입력하세요 : ")
        if input_num == '1':
            pick_menu.pick_menu()
        elif input_num == '2':
            rest_info.pick_menu()
        elif input_num == '3':
            my_rest.show_my_rest()
        elif input_num == '4':
            print("프로그램이 종료되었습니다.")
            break
        else:
            print("1부터 4까지 숫자를 선택해주세요.")
        print()

if __name__ == '__main__':
    pick_num()