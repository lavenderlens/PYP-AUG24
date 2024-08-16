"""
a tuple is an IMMUTABLE, indexed(ordered) conatiner
permits duplicates
commonly used to store different types od data together
such as that returned from a function
to ensure the data cannot be modified
*args function paramters pack n number of args into a tuple
"""

my_tuple = ("alan", 21, ["walking", "photography"], True)
my_empty_tuple = ()
my_empty_tuple = tuple()
fib = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144)

# tuple methods
print(fib.count(1))
print(fib.index(144))

# we can slice tuples as we would lists
# returns another tuple
print(low_numbers := fib[:6]) #(0, 1, 1, 2, 3, 5)

# we can iterate through tuples

for el in fib:
    print(el)

# we can return index, value pairs 
for index, element in enumerate(fib):
    print(index, element)

# tuple arithmetic
print(fib + (233, 377))
print(fib * 2)