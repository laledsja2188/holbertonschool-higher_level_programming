#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Get first element, use 0 if tuple is empty
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0

    # Get first two elements from tuple_b, use 0 if missing
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0

    return (a1 + b1, a2 + b2)
