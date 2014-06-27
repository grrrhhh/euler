"""
sum of the digits in the number 100!
"""


def factorial(n):
    factorial_result = 1
    while n > 1:
        factorial_result *= n
        n -= 1

    return factorial_result

def sum_of_digits(x):
    return sum(map(int,str(x)))

print sum_of_digits(factorial(100))


"""
Ans - 648
"""