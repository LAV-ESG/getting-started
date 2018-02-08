from math import gcd


def my_print():
    print("Hello World!")


def get_vector_gcd(v):
    """ This function returns the single greatest common divisor of a linear
    vector. Input numbers must be integers.
    """

    a = v[0]
    for x in v[1:]:
        a = gcd(a, x)
    return a


def specific_share(tot, asset, share):
    """ This function returns 1 if 'asset' represents at least 'share' percent
    of the total production 'tot'.
    """

    if asset/tot > share:
        return 1
    else:
        return 0
