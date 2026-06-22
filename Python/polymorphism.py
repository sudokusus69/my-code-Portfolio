class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print('drive!')

class ship:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print('sail!')

class airplane:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print('fly!')

for x in (car('toyota', 'camry', 2020), ship('titanic', 'cruise', 1912), airplane('boeing', '747', 1968)):
    print(x.brand, x.model, x.year)
    x.start()


'''This code demonstrates how to use Python's iterator protocol with the iter() and next() functions. Here's a step-by-step explanation:

Tuple Creation:

A tuple named mytuple is created containing three string elements: "apple", "banana", and "cherry". Tuples are immutable sequences in Python.

Creating an Iterator:

The iter() function is called on mytuple. This creates an iterator object (myit) that allows sequential access to the elements of the tuple. An iterator is an object that implements the __iter__() and __next__() methods.

Accessing Elements with next():

The next() function retrieves the next item from the iterator:

The first next(myit) returns "apple".
The second next(myit) returns "banana".
The third next(myit) returns "cherry".
Each call to next() advances the iterator to the next element in the sequence.

Key Concepts:
Iterators: Objects that allow you to traverse through a collection one element at a time without needing to know the underlying structure.
iter(): Converts an iterable (like a tuple, list, or string) into an iterator.
next(): Retrieves the next item from the iterator. If there are no more items, it raises a StopIteration exception.
Output of the Code:
When you run this code, the output will be:

Gotchas:
If you call next(myit) again after the third call, it will raise a StopIteration exception because there are no more elements in the tuple.
Iterators are stateful. Once you consume an element using next(), it cannot be accessed again unless you recreate the iterator.
'''