'''
sets are mutable, unordered containers that do not permit duplicates
as such, they are often used for converting lists with duplicates into lists with unique values
moreover, they have utility methods for comparing between sets, useful for data science
'''
# creation
unique_nums_1 = {44,55,66,44,55,66}
print(unique_nums_1)#{66, 44, 55}
# unique_nums_2 = set(44,55,66,44,55,66)#TypeError: set expected at most 1 argument, got 6
unique_nums_2 = set((44,55,66,44,55,66))# ALL work
unique_nums_2 = set({44,55,66,44,55,66})# just needs to be grouped somehow
unique_nums_2 = set([44,55,66,44,55,66])# converts from a list to a set
# note: sets do not convert from dicts

print(unique_nums_2)
print(type(unique_nums_2))
# convert BACK to a list from a set:
unique_nums_list = list(unique_nums_2)
print(unique_nums_list)#[66, 44, 55]
print(type(unique_nums_list))

# comparing sets is very powerful for data analytics
unique_nums_3 = {55,66,33,22,11}
print(common_values := unique_nums_1.intersection(unique_nums_3))#reflexive
print(common_values := unique_nums_1.difference(unique_nums_3))#non-reflexive
print(common_values := unique_nums_1.symmetric_difference(unique_nums_3))
print(unique_nums_1, unique_nums_3)#don't mutate
# print(common_values := unique_nums_1.symmetric_difference_update(unique_nums_3))#warning: mutates originals!
# print(unique_nums_1, unique_nums_3)#{33, 11, 44, 22} {33, 66, 22, 55, 11}

