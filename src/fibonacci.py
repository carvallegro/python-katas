import math

SQRT_OF_FIVE = math.sqrt(5)


def fibonacci(limit):
    a, b = 1, 1
    total = 0
    while a < limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b  # the real formula for Fibonacci sequence
    print(total)
    return total;
