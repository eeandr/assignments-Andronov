#! /usr/bin/env python

from __future__ import print_function, division

#  Task 2

""""
:param a: str
:param b: str
"""""

def p_distance(a,b):
    if len(a) != len(b):
        raise ValueError('lengths differ')
    diffs = 0
    gaps = 0
    for pair in zip(a,b):
        if pair[0] == pair[1]:
            diffs += 1
        elif '-' in [pair[0], pair[1]]:
            gaps += 1
    return diffs / (len(a) - gaps)


#  Task 3

""""
:param a: list
:param b: list
"""""

def matrix_product(a, b):
    ia = len(a)
    ja = len(a[0])
    mb = len(b[0])
    matr = [[[0] * mb] for _ in xrange(ia)]
    for m in xrange(0, mb - 1):
        for i in xrange(0, ia - 1):
            for j in xrange(0, mb - 1):
                matr[m][i] += (a[i][j] * b[j][i])  #  'a problem: matr[m][i] is list, not integer'
    return matr

# compu_complexity O(N1 * N2* N3)

# Task 1
# nat_row = [1,2,3 .... n]
# For any i,j <= n / 2  : nat_row[i-1] + nat_row[-i] = nat_row[j-1] + nat_row[-j]
# sum(nat_row) = (nat_row[0] + nat_row[-1]) * n / 2




