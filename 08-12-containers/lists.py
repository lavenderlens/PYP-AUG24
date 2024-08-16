"""a list is a mutable, indexed/ordered container 
permits duplicates
commonly used to store elements of the same type
but need not be
"""

# creation
# empty list
nums = []
nums = list()
nums = [1,2,3]

# /element referencing
#  a single element by index
print(nums[2])

# reassigning elements
nums[2] = 4

# /extending by adding elements
nums.append(5)
print(nums)

# slicing: the creation of a new list from all or part of the original
fib = [0,1,1,2,3,5,8,13,21,34]
print(len(fib))

# slice arguments startIndex inclusive, endIndex exclusive, step

print(slice1 := fib[4:8])
print(slice2 := fib[7:])
print(slice3 := fib[7:10])
# print(fib[10])#IndexError: list index out of range
print(slice4 := fib[::2])
print(slice4 := fib[::-1])

# builtins
print(f"num elements: {len(fib)}")
print(f"sum elements: {sum(fib)}")
print(f"min elements: {min(fib)}")
print(f"max elements: {max(fib)}")

#  we may add lists
print(list5 := fib + [55,89,144])

# we may multiply lists
print(list6 := list5 * 10)

# we can return index, value pairs 
for index, element in enumerate(fib):
    print(index, element)

# list comprehension enables us to pass in a loop function 
# to transform elements of a list
# and return a new list with the transformations applied
# in that it transforms original data but does not mutate it
# it may be considered a Functional Programming (FP) technique
# mutating a list: Save
# transforming a list: Save As

# scale original list of numbers
scaled_list = [el * 2 for el in fib]
print(scaled_list)

# filter original list of numbers for those <=10
list_of_under_10s = [el for el in fib if el <= 10]
print(list_of_under_10s)