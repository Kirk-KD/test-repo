
def add(x, y):
    """add"""
    return x + y

def subtract(x, y):
    """subtract"""
    return x - y

def multi(x, y):
    """multiply"""
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("division by zero")
    return x / y