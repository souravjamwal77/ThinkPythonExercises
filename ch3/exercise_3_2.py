""" Answer to the 2nd problem in 3rd chapter.
"""

def print_spam():
    """Prints spam on the CLI.
    """
    print("spam")


def print_twice(v):
    """Prints the given argument twice.

    Args:
        v (any/str): value to be printed twice
    """
    print(v)
    print(v)


def do_twice(f, v):
    """Invokes passed function object twice.

    Args:
        f (function object): a function object to be invoked twice.
        v (Any): value to be passed to the function while invoking
    """
    print_twice(v)


def do_four(f, v):
    """Invoked the given fun obj four times.

    Args:
        f (function object): A function object to be invoked four times
        v (any): Value to be passed to the above fun obj while invoking.
    """
    do_twice(v)
    do_twice(v)
    