import time

number = 0

target_tick =time.time() + 5

while time.time() < target_tick:
    number += 1

print("5초동안 {}번 반복됨".format(number))


i = 0 

while True:
    print("{}번째 반복문".format(i))
    i = i + 1

    input_text = input("> 종료하시겠습니까?(y): ")
    if input_text in ['y','Y']:
        print("반복종료")
        break

numbers = [5,15,25,35,45]

for number in numbers:
    if number <20:
        continue
    print(number)

