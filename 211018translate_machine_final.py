from bs4 import BeautifulSoup  #뷰티풀숲
import time #시간
from openpyxl import Workbook #엑셀
from selenium import webdriver #셀레니움 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import codecs
import os #필요없는 코드

driver = webdriver.Chrome(r'C:\Users\admin\crawlingtwitter\chromedriver')

# driver.implicitly_wait(3)

timestamp = time.time()
It = time.localtime(timestamp)

# wb = Workbook()
# ws = wb.active
# ws.append(["연번", "id", "날짜", "url", "content"])

translate_input = input("번역대상이 저장되어 있는 파일명을 입력하세요(ex\ paper.txt):")
translate_output = r"C:/Users/admin/translating_machine/" + str(It.tm_year) + str(It.tm_mon) + str(It.tm_mday) + str(It.tm_hour) + str(It.tm_min)+ str(translate_input)
# search_result = str(It.tm_year) + str(It.tm_mon) + str(It.tm_mday) + str(It.tm_hour) + str(It.tm_min) + str(search_csv)

translate_input_path = r"C:/Users/admin/translating_machine/" + translate_input

f = codecs.open(translate_input, 'r', "utf-8")

f2 = codecs.open(translate_output, 'w', "utf-8")

text_to_input = ""

count = 0

result = "" 

url = "https://papago.naver.com/" #파파고 주소

lines = f.readlines() #list로 돌려줌 

pure_text = ""

for i in lines :
    pure_text += i

# 문단 전체가 하나의 글로 통합

pure_text_list = []

pure_text_list = pure_text.split('.') #문장 단위 분해

print(pure_text_list)

for line in pure_text_list : #line하나가 번역기에 다안들어 갈수도 있는 문제

    if line == '' : pass
    else : 
        count += 1 #문장 갯수 세기
                
        text_to_input += line #문장을 text_to_input에 집어넣는다.

        text_to_intput = '.'    

        print("====================" + str(count) + "====================")
        print(line)

        if (count % 10 == 0 or count == len(pure_text_list) ) : #문장이 10개가 되거나 count가 pure_text_list에 일치하는 경우

            text_to_input = text_to_input.replace('\r', '')

            text_to_input = text_to_input.replace('\n', ' ')

            print("====================================================text_to_input :" + text_to_input)

            driver.get(url)

            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "txtSource")))
            
            # time.sleep(3)

            driver.find_element_by_id("txtSource").send_keys(text_to_input)
            #txtSource

            try : 
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#txtTarget > span"))) #번역된 글이 뜰때까지 기다린다
            except :
                pass

            time.sleep(5)

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            # print(soup)

            # result = soup.select_all("#txtTarget > span:nth-child(1)")

            result = soup.select("#txtTarget > span")


            for i in result : 
                print(i.text)
                f2.write(str(i.text))


            result = ""

            # except : 
            #     pass

            text_to_input = "" 




driver.close()

f.close()

f2.close()


 