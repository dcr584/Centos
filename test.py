import pymysql.cursors
import sys

num_1=0;    #사용수량 입력 받을 변수    
num_2=0;    #구매수량 & 잔여수량 변수
answer=0;   #잔여수량 계산 변수
first_count = 0; #처음 실행 카운터
input_count=0;   #입력 카운트
index_count = 0; #잔여수량 index 카운터

sql1 = 'select * from Newbie.Content'#사용자 입력 선택
sql2 = "insert into Newbie.Content(DATE, NAME, NOTE, C_NUM, P_TIME, USE_N)values(%s, %s, %s, %s, %s, %s)"#사용자 입력
sql3 = "insert into Newbie.Parking_Buy(BUY_NUM)values(%s)"#사용 수량 입력
sql4 = 'select USE_N from Newbie.Content' #사용수량 컬럼 불러오기
sql5 = 'select BUY_NUM from Newbie.Parking_Buy' #구매수량
sql6 = 'select RESIDUE from Newbie.Residue' #잔여수량
sql7 = "insert into Newbie.Residue(RESIDUE)values(%s)"  #잔여수량 입력

def Content(input_date, input_name, input_note, input_c_num, input_p_time, input_use_n): #사용자 입력
    global input_count #전역변수 사용
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8mb4') 
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql2, (input_date, input_name, input_note, input_c_num, input_p_time, input_use_n))
            input_count = input_count + 1 #입력 카운트 증가
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

def Residue(): #사용수량 컬럼 불러오기
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
            
            global first_count #지역 변수에서 사용하기 위해global 선언
            
            if(rows2 == ()):#사용수량에 입력이 없을 경우
                #print("1")
                    for i in rows1:
                        print(i, end=' ')
                        for j in rews4:
                            print(j)

            elif(rows4 == ()):   #잔여수량이 비어있을 경우
                #print("2")
                num_1 = rows2[0]#사용수량---데이터 베이스의 tuple 값을 가져와 num_1 대입
                num_2 = rows3[0]#구매수량---데이터 베이스의 tuple 값을 가져와 num_2 대입

                for i in range(len(num_1)):#num_1의 사이즈 만큼
                    Sum = int(num_2[0]) - int(num_1[0])#구매수량 - 사용수량---(('100'),) 이러한 형태를 띄기 때문에 [0]번 인덱스의 값을 넣어준다.
                
                cursor.execute(sql7, (Sum))#잔여수량 입력
                rows5=cursor.fetchall()
        
                cursor.execute(sql6)#잔여수량확인
                rows7=cursor.fetchall()
                
                first_count = first_count + 1;#first_count를 통해 구매수량 및 사용자가 프로그램을 처음 이용하지 않는 다는 것을 카운트한다.

                for i in rows1:#사용자가 입력한 정보
                    print(i, end=' ')#end=' ' 자동 줄바꿈 방지
                    for j in rows7[0]:#구매수량 - 사용수량 한 값을 출력한다.
                       print(j)
                        
            elif(first_count < input_count):#사용자가 입력을 할때마다 input_count가 카운트된다. 입력 카운트보다 작을 때 까지 실행하게 한다.
                #print("3")
                num_1 = rows2[first_count]#사용수량
                num_2 = rows4[first_count-1]#잔여수량
                
                for i in range(len(num_1)):#사용수량 사이즈만큼
                    Sum = int(num_2[0]) - int(num_1[0])#잔여수량 - 사용수량
                cursor.execute(sql7, (Sum))#잔여수량 입력
                rows6=cursor.fetchall()

                cursor.execute(sql6)#잔여수량확인
                rows8=cursor.fetchall()
                first_count = first_count + 1#출력 후 count 증가

                index_count = 0 #잔여수량 index 카운터 변수

                for i in rows1:
                    print(i, end=' ')
                    for j in rows8[index_count]:#잔여수량 tuple에서 0번index부터 하나씩 출력하게 한다.
                        print(j)
                        index_count = index_count + 1 #index 증가
            else:
                #print("4")
                index_count = 0
                cursor.execute(sql6)#잔여수량확인
                rows4=cursor.fetchall()

                for i in rows1:
                    print(i, end=' ')
                    for j in rows4[index_count]:#잔여수량 tuple에서 0번 index부터 하나씩 출력하게 한다.
                        print(j)
                        index_count = index_count + 1 #index 증가
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

    print("1. 내용입력 2. 확인 3. 구매수량 4. 종료") #시작 메뉴
    num_menu = int(input("번호를 입력해 주세요 : "))
    print("\n")

    if(num_menu == 1):  #입력
        if(Parking == False):#구매수량이 없을 경우
            print("구매수량을 먼저 입력해 주세요.")
        else:#구매수량이 있을 경우
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
        Residue()

    elif(num_menu == 3): #구매수량
        input_buy_num = int(input("구매수량 입력해 주세요 : "))
        Parking_Buy(input_buy_num)

    elif(num_menu == 4): #종료
        sys.exit()

    print("\n")
