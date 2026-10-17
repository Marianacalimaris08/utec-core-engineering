#!/usr/bin/env python3


def uppercase(str):
    """Print str in uppercase (a-z only) using ASCII conversion."""
    result = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
