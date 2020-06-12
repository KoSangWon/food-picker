# coding=utf-8
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import requests
import time
import ssl

def rest_info():
    food = input("원하는 메뉴를 입력하세요 : ")
    print("현재 위치를 인식 중이에요!")
    driver = webdriver.Chrome('/Users/kosangwon/Desktop/chromedriver')

    driver.implicitly_wait(5)

    driver.get("https://m.map.naver.com/#")

    search_click = driver.find_element_by_xpath('/html/body/div[2]/header/div[4]/div/div/div/span[1]/input')

    time.sleep(15)#GPS로 현재 위치 인식해야함.
    search_click.click()
    search_input = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/form/div/div[2]/div/span[1]/input')
    search_input.send_keys(food)
    search_input.send_keys('\n')
    time.sleep(3)
    req = driver.page_source

    print("위치 인식이 끝났습니다! 아래에 리스트를 보여드릴게요!")

    soup = BeautifulSoup(req, 'html.parser')
    res = soup.find_all(class_='item_tit _title')
    res2 = soup.find_all(class_='item_address _btnAddress')
    res3 = soup.find_all(class_='item_distance')

    for i in range(0, len(res)):
        print("============================================")
        print(str(i+1) + " 번째")
        print("식당 이름 : "+ res[i].find('strong').text)
        print("주소 : " + make_address(res2[i].text))
        print("거리 : " + res3[i].text)


def rest_info_related_order():
    food = input("원하는 메뉴를 입력하세요 : ")
    print("현재 위치를 인식 중이에요!")
    driver = webdriver.Chrome('/Users/kosangwon/Desktop/chromedriver')

    driver.implicitly_wait(5)

    driver.get("https://m.map.naver.com/#")

    search_click = driver.find_element_by_xpath('/html/body/div[2]/header/div[4]/div/div/div/span[1]/input')

    time.sleep(15)#GPS로 현재 위치 인식해야함.
    search_click.click()
    search_input = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/form/div/div[2]/div/span[1]/input')
    search_input.send_keys(food)
    search_input.send_keys('\n')
    time.sleep(4)
    req = driver.page_source

    print("위치 인식이 끝났습니다! 아래에 리스트를 보여드릴게요!")

    soup = BeautifulSoup(req, 'html.parser')
    res = soup.find_all(class_='item_tit _title')
    res2 = soup.find_all(class_='item_address _btnAddress')
    res3 = soup.find_all(class_='item_distance')

    for i in range(0, len(res)):
        print("============================================")
        print(str(i+1) + " 번째")
        print("식당 이름 : "+ res[i].find('strong').text)
        print("주소 : " + make_address(res2[i].text))
        print("거리 : " + res3[i].text)




def rest_info_distance_order():
    food = input("원하는 메뉴를 입력하세요 : ")
    print("현재 위치를 인식 중이에요!")
    driver = webdriver.Chrome('/Users/kosangwon/Desktop/chromedriver')

    driver.implicitly_wait(5)

    driver.get("https://m.map.naver.com/#")

    search_click = driver.find_element_by_xpath('/html/body/div[2]/header/div[4]/div/div/div/span[1]/input')

    time.sleep(15)#GPS로 현재 위치 인식해야함.
    search_click.click()
    search_input = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/form/div/div[2]/div/span[1]/input')
    search_input.send_keys(food)
    search_input.send_keys('\n')
    search_click_2 = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/label[2]')
    search_click_2.click()
    driver.find_element_by_xpath('/html/body/div[4]/div[2]/ul/li[1]/div[1]/a[2]/div/strong')
    time.sleep(1)
    req = driver.page_source

    print("위치 인식이 끝났습니다! 아래에 리스트를 보여드릴게요!")

    soup = BeautifulSoup(req, 'html.parser')
    res = soup.find_all(class_='item_tit _title')
    res2 = soup.find_all(class_='item_address _btnAddress')
    res3 = soup.find_all(class_='item_distance')

    for i in range(0, len(res)):
        print("============================================")
        print(str(i+1) + " 번째")
        print("식당 이름 : "+ res[i].find('strong').text)
        print("주소 : " + make_address(res2[i].text))
        print("거리 : " + res3[i].text)



def make_address(address):
    address = address[4:].strip()
    return address

def show_menu():
    print()
    print("보고자 하는 순서를 선택하신 후 메뉴를 입력해주세요!")
    print("1. 관련도순")
    print("2. 거리순")
    print("3. 돌아가기")

def pick_menu():
    while True:
        show_menu()
        input_num = input("번호를 입력하세요 : ")
        if input_num == '1':
            rest_info_related_order()
        elif input_num == '2':
            rest_info_distance_order()
        elif input_num == '3':
            break
        else:
            print("1부터 3까지 번호를 선택해주세요.")
        print()


if __name__ == '__main__':
    pick_menu()