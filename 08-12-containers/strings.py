'''
strings are immutable, ordered containers of characters, 
they may contain duplicate characters
string methods return a new string
the original is unaffected but the same reference may be updated 
to point to the new string
'''

s1 = "Hello"
s2 = "Hello"
print(s1, id(s1))#id SAME: strings are immutable objects
print(s2, id(s2))
print(s1 == s2)

lst1 = ["Hello"]
lst2 = ["Hello"]
print(lst1, id(lst1))#id DIFFERENT: lists are mutable objects
print(lst2, id(lst2))
print(lst1 == lst2)

# number formatting in strings
import math
print(math.pi)
print(f"PI to 4 decimal places: {math.pi:.4f}")
price  = 19.99
print(f"price: {price:.0f}")