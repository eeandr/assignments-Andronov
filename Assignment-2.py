from __future__ import division, print_function
import operator
import collections


string = "abcabcabcabcd"
counts = collections.Counter(string[i:i+2] for i in xrange(len(string)-2))

#Task 2
def my_min(object):
    print("My_min is " + str((sorted(object))[0]))
    print("My_max is " + str((sorted(object))[-1]))


my_min(object)

a = object


def my_min(*args, **kwargs):
    if not args:
        raise ValueError("No arguments")
    if len(args) == 1:
        elements = args[0]
        if not isinstance(elements, (tuple, list)):
            raise ValueError("One argument of wrong type")
        current_min = elements[0]
        for num in elements:
            if not isinstance(num, int):
                raise ValueError
            current_min = num if num < current_min else current_min



# another version
    if len(obj) == 1 and type(obj) is not 'int':  # I do not understand the first condition
        raise ValueError("the only not integer argument")

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


def my_map(fn, elements):
    return [fn(element) for element in elements]


def myfun(num):
    return num**2
my_filter(myfun,(1,2,3,0,4,5))



#Task 4 # draft only


def calculate(numbers,operations):
    dic_oper = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
    for i in xrange(1, len(numbers)):
        j = dic_oper[operators[i-1]](numbers[i-1],numbers[i])
        numbers[i] = j
    print(j)


numbers = [10,5,3,4,2]
operators = ("+", "-", "*", "/")
calculate(numbers, operators)

#test







