# ensure that the command line prompt is in this dir before executing

with open("data.txt") as file:
    for line in file:
        print(f"a line {line}")

# no need to close
# no need to call read methods
# the file is the context (hence name context manager)
# __enter__ and __exit__ dunder methods are called under the hood
# instead of having try-except to handle erros
# the __exit__ method will handle ALL the exception handling code
# no need tow rite exception handling!
# optionally we may write our own custom context managers