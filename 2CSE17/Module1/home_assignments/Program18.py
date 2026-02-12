def factorial_digits(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return [int(d) for d in str(fact)]
print(factorial_digits(5))  
print(factorial_digits(10))  
print(factorial_digits(1))
