#!/usr/bin/env python3


def pow(a, b):
    """Return a raised to the power b using a loop (no ** operator)."""
    result = 1
    for _ in range(abs(b)):
        result *= a
    if b < 0:
        return 1 / result
    return result
