"""
Distinct powers
How many distinct terms are in the sequence generated by a ^ b for 2 <= a <= 100 and 2 <= b <= 100?
"""

def distinct_powers(a, b):
    distinct_powers_set = set()
    for x in range(2, a + 1):
        for y in range(2, b + 1):
            distinct_powers_set.add(x ** y)

    return distinct_powers_set

print len(distinct_powers(5, 5))
print len(distinct_powers(100, 100))


"""
Solution - 9183
"""