# Variables do not have any keywords, 
# apart from global and nonlocal, 
# which are special case and to do with variable scope 
# (what the variable sees and where it is seen itself)
# VARIABLES SHOULD NAMED SHORT BUT DESCRIPTIVELY

num1 = 1
print(type(num1)) # int

num2 = 1.0
print(type(num2)) # float

name1 = "one"
print(type(name1))

# we may assign one variable's value to another
num3 = num2
print(type(num3)) # float: the type of num3 when it was initialised

# variable DECLARED when you give it a name
# variable ASSIGNED when you give it a value
# in Python, these two must almost always occur together
# variable is INITIALISED when you give it a name and a value at once
# the thing is, when we see code like this:
num2 = 2.0
# there is NOTHING to tell us whether num2 has or has not existed in the script before this point
print(num3) # 1.0 - the value of num2 WHEN num3 initialised
# variable num3 doesn't track changes made to num2


