def subtract(a, b):
    """
    Subtracts a, b. Returns a -b
    
    :param a: number
    :param b: number
    >>> subtract(0, 0)
    0
    >>> subtract(3, 3)
    0
    >>> subtract(10001, 10)
    10000
    # Correct answer is 9991
    """
    return a-b

if __name__=="__main__":
    import doctest
    doctest.testmod(name="subtract", verbose=True)