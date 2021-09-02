from typing import List, Set, Dict, Tuple
import random 
from functools import reduce
from operator import mul


#q1
def splitstr(s: str) -> list:
    """This function takes in a string and breaks it into a list of characters.
    
    doctests:
    >>> splitstr("sriharsha")
    ['s', 'r', 'i', 'h', 'a', 'r', 's', 'h', 'a']
    >>> splitstr("abc")
    ['a', 'b', 'c']
    """
    x = list(s)
    return x

#q2
def join(list_word: list) -> str:
    """Returns string after joining the characters in the string.
    
    doctests:
    >>> join(['h', 'a', 'r', 's', 'h', 'a'])
    'harsha'
    >>> join(['a', 'b', 'c'])
    'abc'
    """
    x1 = "".join(list_word)
    return x1

#q3
def randomList(num: int) -> list:
    """Returns a list of n random numbers where n is the integer.

    doctests:
    >>> randomList(1)
    [1]
    >>> randomList(0)
    []
    """
    L1 = random.sample(range(1, num + 1), num)
    return L1

#q4
def descending(num_List: list) -> list:
    """Returns a sorted list of descending order from the given list.

    doctests:
    >>> descending([1, 2, 3])
    [3, 2, 1]
    >>> descending([3, 4, 1, 2, 5])
    [5, 4, 3, 2, 1]
    """
    L2 = sorted(num_List, reverse=True)
    return L2

#q5
def countFrequency(num_List: list) -> dict:
    """Returns the frequency of each number in the list.

    doctests:
    >>> countFrequency([1, 1, 3, 2, 3, 2, 3, 2, 2])
    {1: 2, 3: 3, 2: 4}
    >>> countFrequency([1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2])
    {1: 5, 5: 2, 3: 3, 4: 3, 2: 4}
    """
    d1 = {}

    for i in range(len(num_List)):
        key = num_List[i]
        value = num_List.count(key)
        d1.update({key: value})
    return d1

#q6
def unique(l: list) -> set:
    """Returns the unique values from the list.

    doctests:
    >>> unique([1, 2, 3, 2, 3, 3, 1, 1])
    {1, 2, 3}
    >>> unique([2, 2, 5, 6])
    {2, 5, 6}
    """
    x = {}
    x = set(l)
    return x

#q7
def repeat(num_List: list) -> set:
    """Returns the first repeating number from the list.

    doctests:
    >>> repeat([1,3,5,1,3,7,8,7])
    1
    >>> repeat([45,67,90,67,45,87,34,98])
    67
    """
    r = set()
    for i in num_List:
        if i in r:
            return i
        else:
            r.add(i)

#q8
def sqrcube(num: int) -> dict:
    """Returns a dictionary containing keys from 0 to n with square and cube.
     
    doctests:
    >>> sqrcube(3)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27]}
    >>> sqrcube(1)
    {0: [0, 0], 1: [1, 1]}
    """
    d2 = {}
    for i in range(num+1):
        key = i
        value = [i ** 2, i ** 3]
        d2.update({key: value})
    return d2

#q9
def zipList(l1: list(), l2: list()) -> tuple():
    """Returns tuples formed of each consecutive element of same index from two lists.

    doctests:
    >>> zipList([1, 2, 3], ['x', 'y', 'z'])
    ((1, 'x'), (2, 'y'), (3, 'z'))
    >>> zipList([1, 2 ,3], ['a', 'b', 'c'])
    ((1, 'a'), (2, 'b'), (3, 'c'))
    """

    n = tuple(l1)
    m = tuple(l2)
    tuplereq = zip(n, m)
    t = tuple(tuplereq)
    return t

#q10
def squares(num: int) -> list:
    """Returns a list of squares from 0 to num using list comprehension.
    
    doctests:
    >>> squares(2)
    [1, 4]
    >>> squares(5)
    [1, 4, 9, 16, 25]
    """
    n = [x**2 for x in range(1, num)]
    return n 

#q11
def sqrdict(num: int) -> list:
    """Returns a dictionary of squares 0 to n using dict comprehension.

    doctests:
    >>> sqrdict(5)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    >>> sqrdict(2)
    {0: 0, 1: 1, 2: 4}
    """ 
    d3 = {x: x**2 for x in range(num+1)}
    return d3

#q12
class MyClass: 
    """ Created a class to apply the method 'apply' on a list of atomic values with exception handling. 

    doctests:
    >>> c1 = MyClass([1, 2, 3, 4])
    >>> c1.apply(lambda x: x**2)
    [1, 4, 9, 16]
    >>> c1 = MyClass([1, 2, 3])
    >>> c1.apply(lambda x: x + 2)
    [3, 4, 5]
    """
    def __init__(self, var):
        self.var = var

    def apply(self, func):
        try:
            return list(map(func, self.var))
        except TypeError:
            raise Exception("Error") from TypeError()

#q13
def uppercase(word_List: list) -> list:  
    """Returns a list of words that has been uppercased from an existing list using 'functools.map'.
    doctests:
    >>> uppercase(['aa', 'bb', 'cd', 'e'])
    ['AA', 'BB', 'CD', 'E']
    >>> uppercase(['harsha', 'sanju'])
    ['HARSHA', 'SANJU']
    """
    l4 = list(map(str.upper, word_List))
    return l4

#q14
def product(num_List: list) -> int:
    """Returns the product of all the numbers in the list using 'functools.reduce'.
    
    doctests:
    >>> product([1, 2, 3, 4, 5])
    120
    >>> product([6, 5])
    30
    """
    product = reduce(mul, num_List)
    return product


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    