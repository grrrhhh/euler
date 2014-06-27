"""
Special Pythagorean Triplet for which a + b + c = 1000
"""
x = 1000
for a in range(1, x):
    for b in range( a, x):
        for c in range(b, x):
            if a + b + c == 1000:
                if a * a + b * b == c * c:
                    print a, b, c
                    print a * b * c






"""
Soltution
200 375 425
31875000
"""