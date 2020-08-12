def factorial_iterative(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    """
    x = 1
    for i in range(n):
        x = x * (i+1)
    return x

