#!/usr/bin/env python3
def common_elements(set_1, set_2):
    """Return a new set with the elements present in both sets."""
    return {x for x in set_1 if x in set_2}
