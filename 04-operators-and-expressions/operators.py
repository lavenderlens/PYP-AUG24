# an expression involves operators and operands. In the following:
x = 1
x = x + 1
# the first line initialises x with a single value
# the second line assigns x the result of an expression
# the expression has an operator, +
# and two operands, x (again), and 1

# arithmetic operators
# +
# -
# *     - 2 squared is 2 * 2
# **    - 2 cubed is 2 ** 3
# /
# %     - remainder, whole number division
# //    - quotient, whole number division (floor division)

print(10 / 2) #5
print(10 % 2) #0

print(10 / 3) #3.3333333333333335 *promotion going on
print(10 % 3) #1
print(10 // 3) #3

print(f"formatted output: {(10 / 3):.2f}") #3.3333333333333335 *promotion going on

# *promotion;
print(9 + 2)#11
print(9 + 2.0)#11.0

# non-numeric arithmetic
print("ho" * 3)
print("* " * 50)

# assignment operators
#  = assigment
# compound assignment
# += compound addition(and string concatenation)]

my_num = 1
my_num += 1
my_num += 1
print(my_num)

my_string = "I "
my_string += "love "
my_string += "Python. "
print(my_string)

# note this way of string building is expensive when long starings are involved.
# how many strungs (strings are immutable) are created in memory with the above 3 lines of code
# https://www.tracedynamics.com/python-string-builder/ shows other methods

# -=    - compound assignment (subtraction)
# *=    - compound assignment (multiply)
# /=    - compound assignment (division)
# %=    - compound assignment (modulus)
# **=   - compound assignment (exponent)
# //=   - compound assignment (floor division)


# walrus operator :=
#  returns and assigns in one go
x = 1
print(x)
# print(x = 1) # TypeError: 'x' is an invalid keyword argument for print()

print(y := 2)#works

# increment/decrement operators ++ and --
# DO NOT EXIST in Python
# Guido Van Rossum applied a number of optimisations when creating Python
# stuff that Guido couldn't see the point of
x = x + 1 # Python equivalent of x++

# multiple assigment (useful but not very Pythonesque)
x = 1; y = 2; z = 3
# may be rewritten as follows (very useful AND Pythonesque)
x, y, z = 4, 5, 6
print(x,y,z)
# often seen in JS as destructuring assignment
# uses include saving dictionary props or list elements to individual variables
my_dict = {"name": "Alan", "age": 21}
name, age = my_dict["name"], my_dict["age"] # square brackets notation for dict props, dot notation for object props
print(name, age)
my_nums = [1,2,3]
first, second, third = my_nums[0], my_nums[1],my_nums[2]
print(first, second, third)

# assignment operator chaining (more specialised, avoid writing if possible)
x = 1
y = 1
# may be rewritten as
x = y = 1

# comparison operators
# <         less than
# <=        less than or equal to
# >         greater than
# >=        greater than or equal to
3 >= 4      #order important
# !=        not equal to
# is        tests for IDENTITY: references the same object as

my_list = [1,2,3]
my_other_list = [1,2,3]
my_copied_list = my_list

print(my_list is my_other_list) #False - the two variable reference two separate objects
print(my_list is my_copied_list) #True - the two variable reference the same object

print(id(my_list)) #4305246592
print(id(my_other_list)) #4305347584
print(id(my_copied_list)) #4305246592

# TODO
# above show different IDs each run
# how == differs from is

print(my_list == my_other_list) # True
# == is COMPARISON operator, 'is' is IDENTITY operator
# going forwards, to classes session
# the REASON my_list == my_other_list
# is because the __eq__ method in the spec for list is overridden to say:
# IF the members are the same, in the same order, then return True
# since the start of the cousre we have been running the __str__ method of objects
# it returns a string representation
print(my_list)
# is equivalent to saying
print(my_list.__str__())
# these Double UNDERscore methods are called
# DUNDER or sometimes magic methods
# they come with properly written classes
# and are called intrinsically or under-the-hood
# print() calls __str__ (under the hood)
# == calls __eq__ (under the hood)


# 'in'- the membership operator

print(1 in my_list) #True
print(4 in my_list) #False
print(4 not in my_list) #True
# checks for membership


# logical operators

# and, or, not

# evaluate to either true or False

print( bool(0) and bool(1) ) #False: both operands need to be true
print( bool(0) or bool(1) ) #True: one operand needs to be true
print( not (bool(0) or bool(1)) ) #False: true is inverted

list_1 = [1,2,3]
list_2 = [1,2,3,4]
list_3 = [1,2,3]

print(list_1 or list_2 == list_3) #TODO [1,2,3]
print(list_1 and list_2 == list_3) #TODO False

print(list_1 == list_3 or list_2 == list_3) #True

# operator precedence
print(10 + 10 * 2)#30 - */ are higher precedence than +-
print((10 + 10) * 2)#40 
print(3 / 2 * 10)#15 - order is L-R for operators that have EQUAL PRECEDENCE
# BODMAS / BOMDAS





