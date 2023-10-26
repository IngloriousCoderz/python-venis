from typing import Iterable


def average(values: Iterable[float]) -> float:
    """
    Computes the arithmetic mean of a sequence of numbers.

    >>> average([20, 30, 70])
    40.0

    # >>> average([20, 30, 50])
    # 40.0
    """
    return sum(values) / len(list(values))


def factorial(n):
    """
    Computes the factorial of a number.

    >>> factorial(5)
    120

    >>> factorial(5.5)
    Traceback (most recent call last):
    ValueError: n must be exact integer
    """
    import math

    if not n >= 0:
        raise ValueError("n must be >= 0")

    if math.floor(n) != n:
        raise ValueError("n must be exact integer")

    if n + 1 == n:
        raise OverflowError("n too large")

    r = 1
    f = 2
    while f <= n:
        r *= f
        f += 1
    return r


if __name__ == '__main__':
    import doctest
    doctest.testmod()
