Python is an interpreted language. 
That means that you can run yourPython programs without the need to first link or compile them.

Two different modes:

Interactive Mode
Meant for experimenting with your code one line or one expression at a time

Standard Mode
Used to run the program from start to finish

Python 3 is not backward compatible
Ie. Anyone having Python 2 cannot run a Python 3 code

## Objects:

All the data in a Python program is represented by object and by relationship between objects.

The value of some objects can change in the course for program execution.
Objects whose value can change are said to be mutable objects (dictionaries and lists)
Where are objects whose value is unchangeable after they’ve been created are called immutable. (strings and tuples)

Each object in Python has three characteristics:

- Object type - (number, string, etc)
- Object value - data value
- Object identity - identity number

Each distinct object in the computer's memory can have its own identity number.

## Attributes:

Most Python objects have either data or functions associated with them. These are known as attributes.

The name of the attribute follows the name of the object.
Both the name of the attribute and the name of the object are separated by a dot.

### Types of attributes:
Data Attribute:
It is a value that is attached to a specific object.
Method
    It is a function that is attached to an object.
    And typically a method performs some function or some operation on that object.



x = np.array([1,3,5])
x.mean() - has brackets - so it is a function/method
X.shape - does not have brackets so is an attribute


Video 1.1.3 Modules and Methods



Python modules are libraries of code that can be used using the import statement

Difference between numpy and math ‘sqrt’ functions
Import math
math.pi
math.sqrt(10)

```
>>> import math
>>> import numpy as np

>>> np.sqrt
<ufunc 'sqrt'>

>>> math.sqrt
<built-in function sqrt>

>>> math.sqrt(2)
1.4142135623730951

>>> np.sqrt(2)
1.4142135623730951

>>> np.sqrt([1, 2, 3])
array([1.        , 1.41421356, 1.73205081])

>>> math.sqrt([1, 2, 3])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    math.sqrt([1, 2, 3])
TypeError: a float is required
```



How to determine the type of the object

def(variable_name)


While asking for help

>> help(name.upper)


Q. Suppose that math.sqrt and numpy.sqrt had identical behavior. Are they the same function?
No. Because they belong to different namespaces, Python treats them separately, regardless of their behavior. 


Video 1.1.4 Numbers and Basic Calculations

Python’s different numeric types:

Integers
Floating point numbers
Complex numbers

Python has unlimited precision for integers - that means that your number is never too ong to fit into Python’s integer type.


Integer Division - Rounds the number to the closest integer less than the actual floating point number

For integer division - use two slash signs

```
>>> 15/7
2.142857142857143
>>> 15//7
2
```

## Sequences: String, List, Tuple

Indexing: access any item in the sequence using an index

## What is the difference between a list and a tuple?

A **list** is **mutable** while a **tuple** is **immutable**.
Ie. objects in the tuple cannot be modified after they are created

Slicing - Slice out substrings, sublists subtuples using indexes.
[start : end+1 : step]

>>> x = 'computer'
>>> print(x[1:4])
omp
>>> print(x[1:6:2])
opt
>>> print(x[3:])
puter
>>> print(x[:5])
compu
>>> print(x[-1])
r
>>> print(x[-3:])
ter
>>> print(x[:-2])


### Adding / Concatenation: Combine two sequences of the same type using +

```
>>> x = 'horse' + 'shoe'
>>> print(x)
horseshoe


>>> y = ['pig', 'cow'] + ['horse']
>>> print(y)
['pig', 'cow', 'horse']


>>> z = ('Kevin', 'Niklas', 'Jenny') + ('Craig', ) # for the second tuple to be considered, we need to include a comma. If we don’t have a comma, it’s just a string in parenthesis.

>>> print(z)
('Kevin', 'Niklas', 'Jenny', 'Craig')
```


### Multiplying

```
>>> x = 'bug' *3
>>> print(x)
bugbugbug

>>> y = [8, 5] *3
>>> print(y)
[8, 5, 8, 5, 8, 5]


>>> z = (2,4) *3
>>> print(z)
(2, 4, 2, 4, 2, 4)
```

### Checking membership - test whether an item is or is not in a sequence

- in and not in

```
>>> x = 'bug'
>>> print('u' in x)
True


>>> y = ['pig', 'cow', 'horse']
>>> print('cow' not in y)
False


>>> z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
>>> print('Niklas' in z)
True
```


Iterating - iterating through the items in a sequence

```
>>> x = [7,8,3]
>>> for item in x:
    print(item)

    
7
8
3

>>> y = [7, 8, 3]
>>> for index, item in enumerate(y):
    print(index, item)

    
0 7
1 8
2 3
```

### Numbers of item  - count the number of items in a sequence

```
>>> x = 'bug'
>>> print(len(x))
3


>>> y = ['pig', 'cow', 'horse']
>>> print(len(y))
```

### Minimum - find the minimum item in a sequence lexicographically
- Alpha or numeric types, but cannot be mixed types.

```
>>> x = 'bug'
>>> print(min(x))
b


>>> y = ('pig', 'cow', 'horse')
>>> print(min(y))
Cow
```

### Sum - find the sum of items in a sequence
- The entire sequence must be numeric

```
>>> y = [2, 5, 8, 12]
>>> print(sum(y))
27


>>> print(sum(y[-2:]))
20


>>> z = (50, 4, 7, 19)
>>> print(sum(z))
80
```

### Sorting - returns a new list of items in a sorted order

- Does not change the original list
- This is not an in-place sort, it returns a new list with a sorted list

```
>>> x = 'bug'
>>> print(sorted(x))
['b', 'g', 'u']


>>> y = ['pig', 'cow', 'horse']
>>> print(sorted(y))
['cow', 'horse', 'pig']
```


### count(item) - returns the count of the item

```
>>> x = 'hippo'
>>> print(x.count('p'))
2


>>> y = ['pig', 'cow', 'horse', 'cow']
>>> print(y.count('cow'))
2
```

### Index(item) - returns the index of the first occurence of an item

```
>>> x = 'hippo'
>>> print(x.index('p'))
2


>>> y = ['pig', 'cow', 'horse', 'cow']
>>> print(y.count('cow'))
1
```

### Unpacking - unpack the n items of a sequence into n variables

```
>>> x = ['pig', 'cow', 'horse']
>>> a, b, c = x
>>> print(a, b, c)
pig cow horse
```

