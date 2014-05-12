"""
    Find the sum of all the multiples of 3 or 5 below 1000.
"""
def p1(n = 1000):
    return sum(set(range(0,n,3) + range(0,n,5)))

print p1()

"""
Other Solutions:
    sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
    sum(filter(lambda n: n % 3 == 0 or n % 5 == 0, range(0, 1000)))

"""