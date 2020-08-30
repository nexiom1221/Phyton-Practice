import random

english = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

with open("info.txt", "w") as file:
    for i in range(1000):
        
        name = random.choice(english) + random.choice(english)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        file.write("{}, {}, {}\n".format(name,weight,height))