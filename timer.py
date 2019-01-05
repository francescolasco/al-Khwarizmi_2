"""
    File name: timer.py
    Author: Ovidiu Daniel Barba
    Date created: 10/12/2018
    Python Version: 3.7

    Decorator che fa profiling di una funzione
"""

from time import time


def timer(func):
    """
    Decorator che calcola il tempo di esecuzione della funzione
    :param func:
    :return: funzione di wrap
    """
    def wrapping_function(*args, **kwargs):
        start = time()
        value = func(*args, **kwargs)  # chiamata alla funzione da decorare
        elapsed = time() - start
        print(f'Function {func.__name__} with args {args} took {elapsed} seconds')
        return value
    return wrapping_function