"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def p5(val):

    result = val
    while True:
        for factor in range(val, 1, -1):
            if result % factor == 0:
                if factor == 2:
                    print result
                    return
            else:
                break

        result += 20


p5(20)
"""
232792560
"""
