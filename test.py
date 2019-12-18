import pymysql.cursors
import sys
import operator

a=0;
b=0;
Sum=0;
count=0;
count1=0;#입력 카운트

sql1 = 'select * from Newbie.Content'#사용자 입력 선택
sql2 = "insert into Newbie.Content(DATE, NAME, NOTE, C_NUM, P_TIME, USE_N)values(%s, %s, %s, %s, %s, %s)"#사용자 입력
sql3 = "insert into Newbie.Parking_Buy(BUY_NUM)values(%s)"#사용 수량 입력

sql4 = 'select USE_N from Newbie.Content' #사용수량 컬럼 불러오기
sql5 = 'select BUY_NUM from Newbie.Parking_Buy' #구매수량
sql6 = 'select RESIDUE from Newbie.Residue' #잔여수량

sql7 = "insert into Newbie.Residue(RESIDUE)values(%s)"  #잔여수량 입력

def select():   #내용확인
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8mb4')
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql1)
            rows1 = cursor.fetchall()
            #iprint("NO\t날짜\t   작성자    내역   차량번호   주차시간  사용수량")
            for i in rows1:
                print(i)
            conn.commit()
    finally:
        conn.close()

def Content(input_date, input_name, input_note, input_c_num, input_p_time, input_use_n): #사용자 입력
    global count1
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8mb4') 
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql2, (input_date, input_name, input_note, input_c_num, input_p_time, input_use_n))
            count1=count1+1
            conn.commit()
    finally:
        conn.close()

def Parking_Buy(input_buy_num): #주차권 구매 수량
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8mb4')
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql3, (input_buy_num)) 
            conn.commit()
    finally:
        conn.close()

def test(): #사용수량 컬럼 불러오기
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8mb4')
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql1) #사용자 입력 확인
            rows1 = cursor.fetchall()

            cursor.execute(sql4) #사용수량
            rows2=cursor.fetchall()

            cursor.execute(sql5)#구매수량
            rows3=cursor.fetchall()

            cursor.execute(sql6)#잔여수량확인
            rows4=cursor.fetchall()
            
            global count#지역 변수에서 사용하기 위해global 선언
            
            print(rows2)
            print(count)
            if(rows4 == ()):   #잔여수량이 비어있을 경우
                print("if")
                #sql6번을 가져와서 sql7번에 입력
                a = rows2[0]#사용수량
                b = rows3[0]#구매수량
                for i in range(len(a)):
                    Sum = int(b[0]) - int(a[0])#구매수량 - 사용수량
                cursor.execute(sql7, (Sum))#잔여수량 입력
                rows5=cursor.fetchall()

                cursor.execute(sql6)#잔여수량확인
                rows7=cursor.fetchall()
                count=count+1;#처음이 아니라는 입력값을 count 증가시킴
                for i in rows1:
                    print(i, end=' ')
                    for j in rows7:
                        print(j)
            
            elif(rows2 == ()):
                for i in rows1:
                    print(i, end=' ')
                    for j in rows4:
                        print(j)

            elif(count < count1 ):#사용자가 입력값이공백일 때까지
                print("elif")
                a = rows2[count]#사용수량
                b = rows4[count-1]#잔여수량    
                print(b)
                #print("2"+b[count])
                #print("3"+b[count-1])
                for i in range(len(a)):
                    Sum = int(b) - int(a[count])
                cursor.execute(sql7, (Sum))#잔여수량 입력
                rows6=cursor.fetchall()
                count=count+1#출력 후 count 증가
                for i in rows1:
                    print(i, end=' ')
                    for j in rows6:
                        print(j)
            else:
                print("else")
                for i in rows1:
                    print(i, end=' ')
                    for j in rows4:
                        print(j)


            conn.commit()
    finally:
        conn.close()

while True:
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8mb4')
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql5)
            residue = cursor.fetchall()
            if residue == ():#주차권이 없을 경우
                Parking = False
            else:   #주차권이 있을 경우
                Parking = True
            conn.commit()                                 
    finally:
        conn.close()

    print("1. 내용입력 2. 확인 3. 구매수량 4. 종료 5.test") #시작 메뉴
    num_menu = int(input("번호를 입력해 주세요 : "))
    print("\n")

    #print(Parking)     #구매수량체크
    if(num_menu == 1):  #입력
        if(Parking == False):
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
        test()

    elif(num_menu == 3): #구매수량
        input_buy_num = int(input("구매수량 입력해 주세요 : "))
        Parking_Buy(input_buy_num)

    elif(num_menu == 4): #종료
        sys.exit()

    elif(num_menu == 5):
        test()

    print("\n")
