# weather = input("비,미세먼지,맑음 택")
# if weather == '비' or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else:
#     print('준비물 필요 없어요')


temp = int(input('기온은 어때요?'))
if 30 <= temp:
    print("덥다 나가지말자")
elif 10 <= temp and temp <30:
    print("나가자")
elif 0 <= temp < 10:
    print("외투를 챙기자")
else:
    print("춥다 나가지말자")