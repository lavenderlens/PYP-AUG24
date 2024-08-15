'''
args - multiple positional arguments
denoted in parentheses as *args
the word args is arbitrary
the * is mandatory

kwargs - multiple named (keyword) arguments
denoted in parentheses as **kwargs
the word kwargs is arbitrary
the ** is mandatory
'''

# args
#  zero, one, or many positional arguments get packed into a tuple
# *args parameter must be after any other posiional parameters
def greet(name, hobbies):
    print(f"Hello my name is {name}")
    print(f"My hobbies are {hobbies}")

greet("Alsn", "Photography, music, food")
greet("Alsn", ["Photography", 'music', "food"])
# greet("Billy no mates") #TypeError: greet() missing 1 required positional argument: 'hobbies'

def greet_with_args(name, *hobbies):
    print(f"Hello my name is {name}")
    print(f"My hobbies are {hobbies}")
    # print("My hobbies are ".format(str(hobbies)))
    # print("My hobbies are " + str(hobbies))
    # print("My hobbies are", str(hobbies))

greet_with_args("Billy")
greet_with_args("Billy", "walking", "cycling")


# kwargs (Keyword Arguments)
#  zero, one or many named arguments get packed into a dict
# must be after *args in parameter list

def greet_with_kwargs(name, *hobbies, **other_details):
    print(f"Hello my name is {name}")
    print(f"My hobbies are {hobbies}")
    print(f"I also have other details {other_details}")

greet_with_kwargs("Billy no mates")
greet_with_kwargs("Alan", "music", "photography", county="donegal", country="Ireland")
