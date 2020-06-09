# coding=utf-8
import pymysql

def show_my_rest():
    conn = pymysql.connect(host='localhost', user='root',
                           password='*****', db='restaurant',
                           unix_socket="/tmp/mysql.sock")

    while True:
        print("1. 단골가게 보기\n2. 단골가게 등록하기\n3. 삭제하기\n4. 돌아가기")
        inputNum = input("번호를 입력하세요 : ")
        if inputNum == '1':
            curs = conn.cursor(pymysql.cursors.DictCursor)
            sql = """
                SELECT *
                FROM my_rest
            """
            curs.execute(sql)
            row = curs.fetchone()
            i = 1
            if row is None:
                print("등록된 단골가게가 없습니다. 등록해주세요!")
            else:
                print("등록하신 단골가게 리스트입니다!")
                print("================================")
                while row:
                    print(str(i) + "번\n가게 이름 : " + row['name'] + "\n가게 전화번호 : " + row['phone'] + "\n가게 위치 : " + row['place'])
                    print("================================")
                    i = i + 1
                    row = curs.fetchone()
            curs.close()

        elif inputNum == '2':
            print("등록하실 단골가게의 정보를 입력해주세요!")
            name = input("가게 이름 : ")
            phone= input("가게 전화번호 : ")
            place = input("가게 위치 : ")
            curs = conn.cursor()
            sql = """INSERT INTO my_rest (name, phone, place) values (%s, %s, %s)"""
            a = (name, phone, place)
            curs.execute(sql, a)
            conn.commit()
            curs.close()

        elif inputNum == '3':
            name = input("삭제하고 싶은 단골가게의 이름을 입력해주세요! ")
            sql = """
                DELETE FROM my_rest where name=%s;
            """
            curs = conn.cursor()
            curs.execute(sql, name)
            conn.commit()
            curs.close()

        elif inputNum == '4':
            break

        else:
            print("1부터 4까지 번호를 선택해주세요.")
        print()

if __name__ == '__main__':
    show_my_rest()