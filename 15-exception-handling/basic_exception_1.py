"""
   from a user POV, exception handling enables the code tor ecover
   and carry on from a catastrophic event
   from a dev POV, it enables us to create and raises Errors 
   according to business logic 
"""
try:
    num1 = float(input("enter first number:"))
    num2 = float(input("enter second number:"))
    total = num1 + num2
    print(f"sum of {num1} and {num2} is {total}")
except:
    print("oops something went wrong")

print("carrying on regardless...")#unreachable code if unhandled exception