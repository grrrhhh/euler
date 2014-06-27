"""
Sum square difference
Sum of Squares - Square of sums
"""

def p6(n):
    sum_of_squares = 0
    square_of_sums = 0

    for i in range(0, n+1):
        sum_of_squares += i * i
        square_of_sums += i

    return abs(sum_of_squares - (square_of_sums ** 2))

print p6(10)
