list_input = ["52","273", "555", "스파이","236"]

list_number = []

for item in list_input:
    try:
        float(item)
        list_number.append(item)
    except:
        pass

print("{} 내부에 있는 숫자는".format(list_input))
print("{} 입니다.".format(list_number))

try:
    number_input = int(input("정수 입력>"))

except:
    print("정수를 입력하지 않았습니다.")

else:
    print("원의 반지름:", number_input)
    print("원의 둘레:", 2*3.14*number_input)
    print("원의 넓이:", 3.14 * number_input * number_input)

finally:
    print("어떻게든 끝났습니다.")