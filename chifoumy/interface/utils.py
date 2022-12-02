import time


def create_key():
    """
    Return an unique integer key (int) based on time in ms.
    """
    t = time.perf_counter_ns()
    return t
