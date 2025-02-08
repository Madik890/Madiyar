def filter_prime(num):
    def isprime(x):
        if x <= 1:
            return False
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True
    
    r = [ x for x in num if isprime(x)]
    print(r)
    return r


y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filter_prime(y)