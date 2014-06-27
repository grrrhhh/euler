"""
What is the sum of the digits of the number 21000?
"""
def sum_of_digits(x):
    return sum(map(int,str(x)))

num = pow(2, 1000)

print sum_of_digits(num)

"""
Solution - 1366
"""