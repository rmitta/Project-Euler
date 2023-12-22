#The Decorators Module for my Project Euler Files

import time
def timed(function):
    """Decorator for timing a function. Prints time taken to run the function."""
    def wrapper(*args,**kwargs):
        before = time.time()
        result = function(*args,**kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute")
        return result
    return wrapper

def memoise(function):
    """Decorator for memoising a function."""
    memo = {}
    def wrapper(*args):
        if (args) not in memo:
            memo[args] = function(*args)
        return memo[args]
    return wrapper

