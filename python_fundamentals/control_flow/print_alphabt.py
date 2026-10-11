#!/usr/bin/env python3
letters = "".join(chr(c) for c in range(97, 123) if chr(c) not in "qe")
print("{}".format(letters))
