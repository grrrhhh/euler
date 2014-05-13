"""
    Find the largest palindrome made from the product of two 3-digit numbers.
"""
def is_palindrome(n):
    n = str(n)
    return n == n[::-1] #return True if n = palindrome(n) else False

products = (x*y for x in range(999, 0, -1) for y in range(999, x, -1))
print max(p for p in products if is_palindrome(p))