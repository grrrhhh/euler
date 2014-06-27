"""
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
def fibonaci(n = 10):
    x, y = 1, 2
    while x <= n:
        yield x
        x, y = y, x + y

def p2(n = 4000000):
    print sum(x for x in fibonaci(n) if x % 2 == 0)

p2()
