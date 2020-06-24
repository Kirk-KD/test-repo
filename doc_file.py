
import doctest

def mult(a, b):
    """
    >>> mult(2, 3)
    6

    >>> mult(2, 2)
    4
    """
    return a * b
    
def div(a, b):
    """
    >>> div(4, 2)
    2
    """
    return a / b

if __name__ == '__main__':
    
    doctest.main()

