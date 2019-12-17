import pymysql.cursors
import sys

turn=0;

sql1 = 'select * from Newbie.Content'
sql2 = "insert into Newbie.Content(DATE, NAME, NOTE, C_NUM, P_TIME, USE_N)values(%s, %s, %s, %s, %s, %s)"
sql3 = "insert into Newbie.Residue(RUSIDUE)values(%s)"
def select():
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8mb4')
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql1)
            rows = cursor.fetchall()
            for i in rows:
                print(i)
            conn.commit()
    finally:
            conn.close()

def Content(input_date, input_name, input_note, input_c_num, input_p_time, input_use_n):
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8mb4') 
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql2, (input_date, input_name, input_note, input_c_num, input_p_time, input_use_n))
            conn.commit()
    finally:
        conn.close()

def Rusidue(input_rusidue):
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8mb4')
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql3, (input_rusidue)) 
            conn.commit()
    finally:
        conn.close()

while True:
    print("1. 내용입력 2. 확인 3. 구매수량 4. 종료") #시작 메뉴
    print("\n") 
    num_menu = int(input("번호를 입력해 주세요 : "))
    print("\n")

    if(num_menu == 1):  #입력
        print(turn)
        if(turn <= 0):
            print("구매수량을 먼저 입력해 주세요.")
        else:
            input_date=0
            input_name=0
            input_note=0
            input_c_num=0
            input_p_time=0
            input_use_n=0

            input_date = str(input("날짜 : "))
            input_name = str(input("작성자 : "))
            input_note = str(input("내역 : "))
            input_c_num = str(input("차량번호 : "))
            input_p_time = str(input("주차시간 : "))
            input_use_n = int(input("사용수량 : "))
            Content(input_date, input_name, input_note, input_c_num, input_p_time, input_use_n)

    elif(num_menu == 2): #확인
        select()

    elif(num_menu == 3): #구매수량
        turn+=1
        input_rusidue = int(input("구매수량 입력해 주세요 : "))
        Rusidue(input_rusidue)

    elif(num_menu == 4): #종료
        sys.exit()

    print("\n")
