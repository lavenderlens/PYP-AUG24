'''
functions, as in any other language, wrap one or more LOC in a function name
to be called zero, one, or many times at some time in the future
functions are commonly defined in a script ON THEIR OWN, with no runtime code
the script with the runtime code in it, that USES the functions,
is separate, and IMPORTS them from the first script
the first script is called a module
how short can a function be?
1 LOC
why? to make code more declarative
the function name may be more descriptive than its workings
how long can a function be?
Not too long.
As a rule of thumb I would be wary of functions over 50-100 LOC
It is very likely they will have dependencies on other code.
If that other code were to break, so would your function.
You may never know this while unit testing
'''

def add_two_numbers(num1, num2):
    return num1 + num2

result = add_two_numbers(1,2)
print(result)
print(add_two_numbers(3,4))

# pure vs impure functions

# global variable
my_var = "hello"

def first_character_of_word():
    print(my_var[0])

first_character_of_word()#h

my_var = "goodbye"

first_character_of_word()#g

# idemptotence: the property of certain operations in mathematics and computer science 
# whereby they can be applied multiple times without changing the result 
# the result chould not caange for a given input
# the input above is nothing
# but the output changes
# this is very easy to fix

def first_character_of_word_pure(word):
    print(word[0])

first_character_of_word_pure(my_var)#g

my_var = "slàn"

first_character_of_word_pure(my_var)#s
# this second, idempotent approach to coding a function counts as using the same input
# if the input changes, that's OK!

# functions in Python are objects Too!
print(first_character_of_word_pure)
# <function first_character_of_word_pure at 0x104140b80>

def subtract_two_numbers(num1, num2):
    print(num1 - num2)

subtract_two_numbers(2,1)
result = subtract_two_numbers(2,1)
print(result) #None - no return: nothing persisted or passed on

# rules or return:
# the return statement must be LAST in the function
# any code after return is unreachable
# ÷ you may only return one thing
# but that thing may be a complex expression, or an object (container)
# there should be only one return statement for any branch of the function
# there could be multiple returns withing a function
# but only one will ever execute

# arguments
# arguments at runtime when actual data is substituted
# parameters at definition time, when they are placeholders for data

# postional arguments
def open_account(name, balance):
    # opening bonus
    balance += 100
    return (name, balance)

# positional arguments in right order
acc1 = open_account("alan offshore", 2500)
print(acc1)

# acc_no_named_args = open_account()#TypeError: open_account() missing 2 required positional arguments: 'name' and 'balance'

# positional arguments in wrong order
# acc2 = open_account(3500, "alan offshore")#TypeError: can only concatenate str (not "int") to str
# print(acc2)

# named arguments (enables passing in of default values)
def open_account2(name="customer", balance=0):
    balance += 100
    return (name, balance)

acc3 = open_account2()
print(acc3)

acc4 = open_account2(balance = 300, name="Aaron RBS")#order of named args flexible
print(acc4)

# taking named vs positional args aside, there are 4 basic types of function

# 1. no input, no output (output means a return statement)
def greet1():
    print("Hello")
    print("from greet1")
    print("How are you today?")

greet1()
result_greet1 = greet1()
print(result_greet1) #None

# 2. no input, output
def greet2():
    return "Hello" + "\n" + "from greet2" + "\n" + "How are you today?"

greet2()# not passed on
print(greet2()) #output from function passed as input to print function

# 3. input, output 
def greet3(name):
    return "Hello" + "\n" + name + " from greet3\n" + "How are you today?"

print(greet3("Harry"))

# 4. input, no output 
def greet4(name):
    print("Hello")
    print(name, "from greet4")
    print("How are you today?")

greet4("Mark")
