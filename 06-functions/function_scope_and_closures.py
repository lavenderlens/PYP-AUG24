'''
scope defines the visibility and lifespan of a variable
local scope:
-   declared within a function
-   visible only within the function or its blocks
-   lives and dies with the function execution
global scope:
-   declared outside of any functions
-   visible to all functions in the script
-   lives whilst the whole script is executing

'''

next_num = 1 # global

# impure function, depends on the global var
def get_next_num():
    return next_num

print(get_next_num())

# suppose i wish to modify the var next_num?

def increment_next_num():
    # next_num += 1 #UnboundLocalError: cannot access local variable 'next_num' where it is not associated with a value
    return next_num

# print(increment_next_num())

# what on earth is going on?
# next_num IN FUNCTION is assumed to be local to that function
# when we attempt to ASSIGN anything to next_num we cannot
# this is because Python assumes any assignment to be to a LOCAL variable
# and next_num LOCAL has not been initialised
# they are DIFFERENT variables in DIFFERENT scopes, with the SAME name

def increment_next_local_num():
    # declare and initialise a local var
    next_num = 2
    next_num += 1 #works because LOCAL next_num has been initialised
    return next_num

print(increment_next_local_num()) #3
# but global var (just happens to have the same name but is totally separate)
# what if we want to modify the global var from inside the function?
# we must explicitly BIND it inside the function

def increment_global():
    # bind local var to global
    global next_num #now refers to global var in next scope level up
    next_num += 1 #works because LOCAL next_num has been initialised
    return next_num

print(increment_global())
print(next_num) # now 2: a binding has been created, 
# the script remembers the value of the global from one function invocation to the next

# this is useful: it gives the script state
# however, other functions may also access and modify global vars in the same way
# so we could end up with many functions modifying the same global(s)

# what if we could encapsulate global variable state inside a function?

# functions in Python are first order objects - they can be passed TO AND returnd FROM other functions
# this is known as CLOSURES

# stage 1: define an inner scope by writing an inner function,
# then the EFFECTIVE global scope is the scope of the outer

def increment_with_closure():
    # this scope here is local to the outer function
    # but will become EFFECTIVELY GLOBAL IF
    # we define an inner function
    next_num = 100
    def get_next_num():
        print(next_num)
    get_next_num()

increment_with_closure()

# stage 2:
def increment_with_closure():
    next_num = 100
    def get_next_num():
        # next_num += 1 #UnboundLocalError: cannot access local variable 'next_num' where it is not associated with a value
        return next_num
    get_next_num()

increment_with_closure()

# stage 3:
# bind the function-scoped variable to the inner function
#  two things make a closure:
# a lexically-scoped variable in an outer function
# an inner function returned that references the lexically-scoped variable
def increment_with_closure():
    next_num = 100 # this scope is called lexically-scoped and is effectively global to inner func
    def get_next_num():
        nonlocal next_num
        next_num += 1 #UnboundLocalError: cannot access local variable 'next_num' where it is not associated with a value
        return next_num
    # return get_next_num() #don't call function just return its code
    return get_next_num

print(increment_with_closure())
print(increment_with_closure())

my_closure = increment_with_closure()
print(my_closure())
print(my_closure())
print(my_closure())
print(my_closure())

# reset? make another closure

my_closure2 = increment_with_closure()
print(my_closure2())
print(my_closure2())
print(my_closure2())
print(my_closure2())

