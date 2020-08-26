n = 10 
a = range(0, int(n/2))

print(list(a))

for i in range(5):
    print(str(i+1) + "= 반복 변수")

array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    print("{} 번쨰 반복 {}".format(i+1, array[i]))

for i in range(4, 0-1 , -1):
    print(i)
print()
for i in reversed(range(5)):
    print(i)

i =0 
while i< 10:
    print("{}번쨰 반복".format(i))
    i += 1

list_test = [1,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4,5,6,8,7,9,100]
value = 2

while value in list_test:
    list_test.remove(value)

print(list_test)