# we cannot call the functions directly
# they are props of an object
# we must create an object first
from calculator_oo import Calculator

calculator = Calculator()

calculator.add(5)
calculator.mul(3)
calculator.sub(1)
calculator.div(2)
result = calculator.equals()
print(result)
print(calculator.total)