from __future__ import division, print_function

#Task 2
def my_min(object):
    print("My_min is " + str((sorted(object))[0]))
    print("My_max is " + str((sorted(object))[-1]))


object = (1,3,2,6,5,3,0)
my_min(object)


def my_min(object): # another version
    if len(object) == 1 and type(object) is not 'int':  # I do not understand the first condition
        raise ValueError("the only not integer argument")
    for i in xrange(1,len(object)):
        if object[i - 1] < object[i]: #to find my_max change "<" to ">"
            j = object[i - 1]
        else:
            j = object[i]
    print("My_min is " + str(j))


object = (2,7,-9)
my_min(object)


#Task 2.1
# the first argument must contain at least one number in any object, for example dictionaries
# the function can operate with strings (lenght)

#Task 3
def my_map(fn, elements):
    print(map(fn, elements))


def myfun(num):
    return num**2
my_map(myfun,(1,2,3,4))


#_______________________________________


def my_filter(fn,elements):
    print(map(fn,filter(fn,elements)))


def myfun(num):
    return num**2
my_filter(myfun,(1,2,3,0,4,5))



#Task 4 # draft only

import operator
def calculate(numbers,operations):
    import operator
    dicOper = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.div}
    for i in xrange(1, len(numbers)):
        j = dicOper[operators[i-1]](numbers[i-1],numbers[i])
        numbers[i] = j
    print(j)


numbers = [10,5,3,4,2]
operators = ("+", "-", "*", "/")
calculate(numbers, operators)

#test







