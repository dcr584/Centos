import pymysql.cursors
import sys

input_ea=0;

#conn = pymysql.connect(host='localhost', user='root', password='123', charset='utf8mb4')
sql1 = 'select * from study.information' #test1 출력
sql2 = "insert into study.information(Date, Note, Count)values(%s, %s, %s)"#test1 입력
sql3 = "insert into study.information(EA)values(%s)"  #티켓 수량 입력
sql4 = 'select * from study.information where Ea OR NULL' #값이 있는 것 만 출력
sql5 = "insert into study.information(Ea)values(%s)"#test1 입력

def select():
    conn = pymysql.connect(host='localhost', user='root', password='123', charset='utf8mb4')
    try:
        with conn.cursor() as cursor:
           # sql1 = 'select * from study_test.test1'
            cursor.execute(sql1)
            rows = cursor.fetchall()
            for i in rows:
                print(i)
            conn.commit()
    finally:
            conn.close()

def insert(input_Date, input_Note, input_Count):
    conn = pymysql.connect(host='localhost', user='root', password='123', charset='utf8mb4')

    try:
        with conn.cursor() as cursor:
            #sql2 = "insert into study_test.test1(Date, Note, Count)values(%s, %s, %s)"
            #if(input_ea <= 0):
            cursor.execute(sql2, (input_Date, input_Note, input_Count))
            #else:
             #   input_ea = input_ea - input_Count
             #   cursor.execute(sql2, (input_Date, input_Note, input_Count, input_ea))
            #cursor.execute(sql5, (input_ea))
            conn.commit()
    finally:
        conn.close()

def EA(input_Ea):
    conn = pymysql.connect(host='localhost', user='root', password='123', charset='utf8mb4')

    try:
        with conn.cursor() as cursor:
            #sql3 = "insert into study_test.EA_table(EA)values(%s)"
            cursor.execute(sql3, (input_Ea)) 
            conn.commit()
    finally:
        conn.close()

while True:
    print("1. 내용입력 2. 확인 3. 구매수량 4. 종료") #시작 메뉴
    print("\n")
    
    num_menu = int(input("번호를 입력해 주세요 : "))
    print("\n")

    if(num_menu == 1):  #입력
        input_date = str(input("날짜 : "))
        input_note = str(input("내역 : "))
        input_count = int(input("사용수량 : "))
        insert(input_date, input_note, input_count)

    elif(num_menu == 2): #확인
        select()

    elif(num_menu == 3): #구매수량
        input_ea = int(input("구매수량 입력해 주세요 : "))
        EA(input_ea)

    elif(num_menu == 4): #종료
        sys.exit()

    print("\n")
