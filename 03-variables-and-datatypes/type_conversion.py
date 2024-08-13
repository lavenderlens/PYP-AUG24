# type conversion happens implicitly in Python but may be called explicitly as well.
# each data type has its wrapper function of the same name

# conversion to boolean (bool)
# every data type has its truthy and falsey values (converting to True or False)
# it's easier to remember the falsey values - most values are truthy
# falsey:
# Zero numbers
# empty collections/containers
    # collections include str (a collection of characters)
    # NOTE: empty collections in JS are truthy!!
# None

print("Using bool() wrapper")
# numbers
print(bool(1))
print(bool(0))
print(bool(-0))

# strings
print(bool("hello"))
print(bool(""))

# containers (list)
print(bool([1,2,3]))
print(bool([]))

print("Using int() wrapper")
print(int(True))
print(int(False))
print(int(1.0))
print(int(1.5)) # no rounding, only truncation

print("Using float() wrapper")
print(float(1))
print(float(True))

# can nest these wrapper functions (not very readable!)
print(str(float(True)))

print("Using str() wrapper")
print(str(True))
print(type(str(True)))
print(str(123))
print(type(str(123)))
# print(str(123ex)) #SyntaxError: invalid decimal literal

# there exists also methods for sets and dicts- set(), dict()

