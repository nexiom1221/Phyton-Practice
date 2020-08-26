print("프로그램이 시작되었습니다")

while True:
    try:
        print("try 구문이 실행되었습니다")
        break
        print("try 구문의 break 키워드")
    except:
        print("except 구문이 실행되었습니다")
    
    finally:
        print("finally 구문이 실행되었습니다")
    print("while 반복문 마지막 줄")

print("프로그램 종료")