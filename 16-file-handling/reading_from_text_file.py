# ensure that the command line prompt is in this dir before executing

file = open("data.txt")#path must be fully qualified
print(type(file))# <class '_io.TextIOWrapper'>
print(dir(file))# TextIOWrapper props

# 1. read (whole file or no. of cahracters)
content = file.read()#all
print(content)
print("*" * 100)
file.close()
file = open("data.txt") #FileNotFoundError: [Errno 2] No such file or directory: 'dat.txt'
# file = open("dat.txt") #FileNotFoundError: [Errno 2] No such file or directory: 'dat.txt'
content = file.read(50)#chars
print(content)
file.close()

# 2. readline()
file = open("data.txt")
line = file.readline()
print(line)
line = file.readline()
print(f"line {line}")
file.close()

# 3. readlines()
file = open("data.txt")
lines = file.readlines
print(f"lines {lines}")
file.close()