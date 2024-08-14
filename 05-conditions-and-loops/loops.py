'''
Loops come in two sorts: the while loop and the for loop
# while loops are commonly used for console IO
# there may be no obvious end to the process
# for loops are commonly used to iterate over containers
# the length of the container is known in advance
The for loop in Python is syntactic sugar for a while loop, 
usually when the number of iterations is known in advance.
There are no for loops at runtime, only while loops that the code is compiled into.
While loops in source code are useful when the number of iterations is not known in advance.

In Python, an optional else clause may be added to the end of both types of loop, for and while.
It is executed if the loop completes and doesn't hit a break statement.
In other words, if the loop completes normally.
To make this clearly readable, add a comment "# no break" next to the else clause.
'''
# for - used for iterating through an iterable, typically a container
# remember lists, sets, and tuples have a len() length prop

names = ['Michael Jackson', 'David Bowie', 'Janet Jackson', 'James Brown',\
         'Gordon Brown', 'David Hume', 'Michael Jackson']

print("\nas LIST:")
for name in names:
    print(name)

print(len(names))

'''
first variable, name is arbitrarily named
makes sense semantically, to be the singular of the plural
second variable name is an ACTUAL list, and should be plural
'''

# list slicing
# very powerful in Python, controls how we iterate the list
# syntax: [startIdx(inclusive) : endIndx(exclusive) : step]

print("\nas sliced LIST (partial):")
for name in names[2:4]:
    print(name)

print("\nas sliced LIST (reversed):")
for name in names[::-1]:
    print(name)

names_set = {'Michael Jackson', 'David Bowie', 'Janet Jackson', 'James Brown',\
         'Gordon Brown', 'David Hume', 'Michael Jackson'}

# sets do not permit duplicates
# are UNordered

# TypeError: 'set' object is not subscriptable
# for name in names_set[::-1]:
#     print(name)

print("\nfrom a set")
for name in names_set:
    print(name)

'''
output
Janet Jackson
James Brown
Michael Jackson
Gordon Brown
David Bowie
David Hume

again;
Janet Jackson
James Brown
Michael Jackson
David Bowie
David Hume
Gordon Brown'''

# looping through dictionaries
coords = {"x": 3, "y": 5, "z": 6}

# keys
for key in coords.keys():
    print(key)

# values
for value in coords.values():
    print(value)

# both keys and values
for key, value in coords.items():
    print(key, value)

#  for loops with strings
word = "opposition"
for letter in word:
    print(letter)

# using a range function to control number of iterations
for i in range(0,10):
    print(i + 1)

# the range function may be used like list slicing:
# print 5-50 in steps of 5
# start index is INCLUSIVE
# end index is EXCLUSIVE
for i in range(5, 51, 5):
    print(i)

# we may chain an optional else to a loop
# it only executes if the loop finishes normally
# unique to Python
for name in names:
    print(name)
    if name == "James Crown":
        print(f"ERROR = {name} too funky for my code")
        break
else:
    print("list processed with no errors")

#  while loops
# for loops are compiled into while loops at runtime

# EITHER use separately declared counter and have a stop condition
# OR
# use while True and have a break condition

counter = 0
while counter < len(names):
    print(names[counter])
    counter += 1

counter = 0
while counter < len(names):
    print(names[counter])
    if names[counter] == "James Brown":
        break
    counter += 1
else:
    # unreachable code
    print("loop completed with break statement")

counter = 0
while counter < len(names):
    print(names[counter])
    if names[counter] == "James Brown":
        counter += 1 # have to also increment counter in this branch
        continue
    counter += 1
else:
    print("loop completed with continue statement")

# while true (looks odd at first but used a lot)
# MUST have a break statement somewhere in the body of the loop
# means that the user can decide to break
list_of_names = []
while True:
    name = input("Enter a name for the guest list, or X to quit")
    # if name.lower() == "x":
    if name.casefold() == "x":#locale-specific conversion to lower case
        break
    list_of_names.append(name)
