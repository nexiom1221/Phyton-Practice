def fibonacci(n):
    if n == 1:
        return 1

    elif n == 2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("fibnacci(1):",fibonacci(1))
print("fibnacci(2):",fibonacci(2))
print("fibnacci(3):",fibonacci(3))
print("fibnacci(4):",fibonacci(4))
print("fibnacci(5):",fibonacci(5))
print("fibnacci(6):",fibonacci(6))


# 주의 오래 걸림
print("fibnacci(1):",fibonacci(50))