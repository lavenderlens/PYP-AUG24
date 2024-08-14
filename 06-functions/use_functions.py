# 3 ways of importing functions from another script (module)
import functions #everything from module is available

# using functions from a module that DON'T have return statements yields None
print(functions.greet4("Martin"))
print(functions.greet1())
print(functions.greet3("Andrew"))
# negative: functions. doesn't show the next developer what functions we are actually using
# positive: every function call MUST be prefaced by the module name
# so it makes it very clear that the functions come from outside this script

from functions import greet1, greet2, greet3, greet4

greet1()

# I know exactly which functions I will use 
# but it may not be clear that they come from outside ths script
# in my opinion this is the best way

#  probably the worst way:
from functions import * #wildcard, imports everything, but unqualified

acc1 = open_account("alan offshore", 2500)
acc2 = functions.open_account("alan savings", 1500) #CAN fully qualify but often people don't

print(acc1, acc2)

def greet1():
    print("overridden greet1!")

greet1()
