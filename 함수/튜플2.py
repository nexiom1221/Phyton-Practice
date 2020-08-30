def test():
    return(10, 20)
    
a,b = test()

print("a:",a)
print("b:",b)
print()

a, b = b, a

print("#교환 후 값")
print("a:",a)
print("b:",b)