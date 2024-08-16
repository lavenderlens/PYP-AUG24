# handling specific exceptions
try:
    num1 = float(input("enter first number:"))
    num2 = float(input("enter second number:"))
    total = num1 / num2
except ValueError:
    print("enter numbers only")
except ZeroDivisionError:
    print("cannot divide by zero")
except:
    print("ERROR")
# we can chain an optional else just as with loops
#  the else will ONLY run IF no exceptions/errors found
else:
    print(f"{num1} divided by {num2} is {total}")
# we can chain a finally block
# the finally will run REGARDLESS of whether an exception/error
finally:
    print("thank you and goodbye!")
    
# ValueError: could not convert string to float: '2x'
# ZeroDivisionError: float division by zero