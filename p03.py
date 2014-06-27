def largest_prime_factor(n = 13195):
    """
        Calculates the largest prime factor of a given number
    """
    
    def is_prime(n):
        """
            Check whether the given number is prime or not.
        """
        x = 2
        while x * x < n:
            if n % x == 0: 
                return False
            x += 1
        return True
    
    def factors(n):
        x = 2
        while x*x < n:
            if n%x == 0:
                yield x, n/x
            x += 1
    
    largest_prime_factor = 1
    for x, y in factors(n):
        if is_prime(y):
            return y
        elif is_prime(x):
            largest_prime_factor = x
    return largest_prime_factor


print largest_prime_factor(600851475143)
