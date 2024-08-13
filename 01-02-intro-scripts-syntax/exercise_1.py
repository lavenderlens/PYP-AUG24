name = input("enter your name: ")
age = input("enter your age: ")

print("Name:", name, "Age:", age)
print(type(name)) #<class 'str'>
print(type(age)) #<class 'str'>

age = int(age)
print(type(age)) #<class 'int'>

print("Name:", name, "Age next birthday:", age + 1) # builtin str() function being called implicitly
# before number conversion:
# TypeError: can only concatenate str (not "int") to str

print("Name: " + name + " Age next birthday: " + str(age + 1)) 
# WITHOUT cast to str()
#TypeError: can only concatenate str (not "int") to str

# placeholders, Python 3>
print("Using Python 3> placeholders")
print("Name: {} Age next birthday: {}".format( name, str(age + 1)))

# placeholders, Python 3.5>
print("Using Python 3.5> placeholders (f-strings)")
print(f"Name: {name} Age next birthday: {age + 1}") # str() runs implicitly for everything in {}

# placeholders, Python 3.7>
print("Using Python 3.7> placeholders (triple-f-strings)")
print(f"""
Name: {name} 
Age next birthday: {age + 1}""") # preserves line breaks in code

