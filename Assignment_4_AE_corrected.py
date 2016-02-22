#! /usr/bin/env python

from __future__ import print_function, division

#  Task 2

def p_distance(seq_1,seq_2):

    """
    :param seq_1: str
    :param seq_2: str

    """
    from itertools import izip
    if len(seq_1) != len(seq_2):
        raise ValueError('lengths differ')
    same = 0
    gaps = 0
    for a, b in izip(seq_1, seq_2):
        if a == '-' or b == '-':
            gaps += 1
        elif a == b:
            same += 1
    return (1 - same / (len(seq_1) - gaps))


#  Task 3 (works well)


def matrix_product(a, b):

    """
    :param a: list
    :param b: list
    """

    #  the first matrix i * j
    #  the second matrix j * k
    #  the matrix_product i * k

    i = len(a)
    j = len(a[0])
    k = len(b[0])

    matr = [[0] * k for _ in xrange(i)]  #  generator of the empty matrix i * k

    for _i in xrange(0, i):             #  cycle for a product line
        for _k in xrange(0, k):         #  cycle for product columns
            for _j in xrange(0, j):     #  cycle for a particular line*column
                matr[_i][_k] += a[_i][_j] * b [_j][_k]
    return matr

# compu_complexity O(N1 * N2* N3)

# Task 1
# nat_row = [1,2,3 .... n]
# For any i,j <= n / 2  : nat_row[i-1] + nat_row[-i] = nat_row[j-1] + nat_row[-j]
# sum(nat_row) = (nat_row[0] + nat_row[-1]) * n / 2




