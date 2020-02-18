# Python

Python is an *interpreted* language.</br>
That means that you can run your Python programs without the need to first link or compile them.

### Two different modes:

- Interactive Mode: </br>
Meant for experimenting with your code one line or one expression at a time.

- Standard Mode: </br>
Used to run the program from start to finish.

Python 3 is **not backward compatible**
i.e. Anyone having Python 2 cannot run a Python 3 code.

## Objects:

- All the data in a Python program is represented by object and by relationship between objects.
- The value of some objects can change in the course for program execution.
- Objects whose value can change are said to be mutable objects (dictionaries and lists).</br>
Whereas objects whose value is unchangeable after they’ve been created are called immutable. (strings and tuples)

Each object in Python has three characteristics:

- Object type - (number, string, etc)
- Object value - data value
- Object identity - identity number

Each distinct object in the computer's memory can have its own identity number.

## Attributes:

- Most Python objects have either data or functions associated with them. These are known as attributes.
- The name of the attribute follows the name of the object.
- Both the name of the attribute and the name of the object are separated by a dot.

### Types of attributes:

### Data Attribute:
It is a value that is attached to a specific object.

### Method:
- It is a function that is attached to an object.
- And typically a method performs some function or some operation on that object.

```python
x = np.array([1,3,5])
x.mean() - has brackets - so it is a function/method
x.shape - does not have brackets so is an attribute
```

Video 1.1.3 Modules and Methods



Python modules are libraries of code that can be used using the import statement

Difference between numpy and math ‘sqrt’ functions
Import math
math.pi
math.sqrt(10)

```python
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


## How to determine the type of the object?

```python
def(variable_name)
```

While asking for help

```python
>> help(name.upper)
```

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

```python
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

### Slicing - Slice out substrings, sublists subtuples using indexes.
[start : end+1 : step]

```python
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
comput
```

### Adding / Concatenation: Combine two sequences of the same type using +

```python
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

```python
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

```python
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

```python
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

```python
>>> x = 'bug'
>>> print(len(x))
3


>>> y = ['pig', 'cow', 'horse']
>>> print(len(y))
```

### Minimum - find the minimum item in a sequence lexicographically
- Alpha or numeric types, but cannot be mixed types.

```python
>>> x = 'bug'
>>> print(min(x))
b


>>> y = ('pig', 'cow', 'horse')
>>> print(min(y))
Cow
```

### Sum - find the sum of items in a sequence
- The entire sequence must be numeric

```python
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

```python
>>> x = 'bug'
>>> print(sorted(x))
['b', 'g', 'u']


>>> y = ['pig', 'cow', 'horse']
>>> print(sorted(y))
['cow', 'horse', 'pig']
```


### count(item) - returns the count of the item

```python
>>> x = 'hippo'
>>> print(x.count('p'))
2


>>> y = ['pig', 'cow', 'horse', 'cow']
>>> print(y.count('cow'))
2
```

### Index(item) - returns the index of the first occurence of an item

```python
>>> x = 'hippo'
>>> print(x.index('p'))
2


>>> y = ['pig', 'cow', 'horse', 'cow']
>>> print(y.count('cow'))
1
```

### Unpacking - unpack the n items of a sequence into n variables

```python
>>> x = ['pig', 'cow', 'horse']
>>> a, b, c = x
>>> print(a, b, c)
pig cow horse
```


## Lists

- Grow and shrink in size as needed - continue to add and delete elements so the size changes automatically, Python does that for you.
- Sequence type - all the sequence functions are useful for lists.
- sortable.

### Constructors - Creating a new list

### delete - delete a list or an item in a list

**del()**

### append - add an item to the end of the list

### extend - append a sequence to the list

### insert - inset an item at a given index

### pop - pop the last element of the list and return the item

### remove - remove the first instance of an item

### reverse - reverse the order of the list. It is an in-place sort. I.e. it changes the original list.

### sort - sort the list in place

- sorted(x) - returns a new sorted list w/o changing the original list x
- x.sort() - sorts the list in-place

### reverse sort - sort items in descending order

- Use reverse = True parameter to the sort function


