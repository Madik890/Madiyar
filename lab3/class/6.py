def filter_primes(numbers):
    return list(filter(lambda num: all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)) and num > 1, numbers))