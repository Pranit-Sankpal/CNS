import random

# Miller-Rabin primality test
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Write n as d*2^r + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Function to generate a random n-digit number
def generate_large_number(digits):
    lower_bound = 10 ** (digits - 1)
    upper_bound = 10 ** digits - 1
    return random.randint(lower_bound, upper_bound)

def generate_prime_no(digits):
    while True:
        number = generate_large_number(digits)
        if is_prime(number):
            return number