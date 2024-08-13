# the standard built-in datatypes
# single values or expressions that evaluate to them
# immutable by default

# bool
# values: True or False (OR some expression that evaluates True or False)
# immutable type (may not be changed)
my_bool = True
my_bool = False # a reassignment, NOT a mutation of True

# int (INTEGERS, OR WHOLE NUMBERS)
# values: whole numbers, positive or negative (OR some expression that evaluates to them)
# immutable type
my_int = 1

# float (floating-point numbers)
# values: any fractional number, positive or negative (OR some expression that evaluates to them)
# immutable type
my_float = 1.0

# str (strings)
# values: ANY characters of zero or more
# immutable type
# single, OR double, OR triple quotes (triple in f-strings or docstrings - see functions)
# indexed from zero (first character)
# length prop
my_str = "hello"
first_character = my_str[0]
print(first_character)
print(len(my_str))#length

print(my_str.upper())
print(my_str)# original immutable
my_str = my_str.upper() # can be changed via re-assignment
print(my_str)

# types for multiple values
# mutable by default (except tuple)
# list / lst
# commonly used for elements of the ame type
my_list = ["bat", "ball", "gloves"]
print(my_list)
print(type(my_list))
print(len(my_list))
print(my_list[0])
print(type(my_list[0]))
my_list.append("whites")
print(my_list)
print(len(my_list))
my_list[0] = "stumps"
print(my_list)
my_list_2 = list([1,2,3])
print(my_list_2)

# tuple
#  a datatype that may not be have its elements re-assigned
my_tuple = ("bat", "ball", "gloves")
# my_tuple. - less methods available
# my_tuple[0] = "stumps" # TypeError: 'tuple' object does not support item assignment

# commonly used for results/return values from other functions
# where elements are not necesaarily same type
my_ultimate_tuple = (42, "The ultimate answer")
print(type(my_ultimate_tuple))

my_other_tuple = tuple([1, "The ultimate question"])
print(type(my_other_tuple))

# sets
# values: the elements of a set can be of any type
# sets are NOT ORDERED
# sets may NOT CONTAIN DUPLICATES
# set methods compare and combine sets for difference, similarity
my_set = {1,2,2,3,4,5,5} # curly braces for single elements: set, for key:value pairs: dict
print(my_set)
my_other_set = {"one", "two", "two", "forty-four", "ninety-one", "a-one"}
print(my_other_set) 
# {'two', 'one', 'forty-four', 'ninety-one', 'a-one'}
# {'a-one', 'two', 'forty-four', 'one', 'ninety-one'}
# {'forty-four', 'a-one', 'two', 'one', 'ninety-one'}
print(type(my_set))

# dict (dictionary)
# values: key: value pairs
# keys MAY BE of any type but are commonly strings
# keys must be unique
# values may be of any type and may be duplicated
#  mutable
# note: a Python DICT IS NOT the asame as an object, even though both print out with curly braces and key: value pairs!
# objects are made by classes
# theoretically EVERYTHING is an object in Python

my_dict = {"name": "fred", "age": 21, "employed": True}
print(my_dict)
print(type(my_dict))

# None type (equivalent of null in other languages)
# means references no object / points nowhere
my_none = None
print(my_none)
print(type(my_none)) #<class 'NoneType'>
