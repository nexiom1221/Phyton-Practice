jonghwa = "961221-1234567"

print("성별 : "+ jonghwa[7])
print("년 : "+ jonghwa[0:2])
print("생일 : "+ jonghwa[2:6])

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].islower())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("i", 9)
print(index)
print(python.find("Java"))

print(python.count("n"))