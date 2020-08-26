try:
    number_input = int(input("정수 입력>"))

    print("원의 반지름:", number_input)
    print("원의 둘레:", 2*3.14*number_input)
    print("원의 넓이:", 3.14 * number_input * number_input)

except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:",exception)
