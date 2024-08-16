'''
a dict is a mutable, unordered container of key: value pairs
keys must be unique, and, ideally, immutable (numbers or strings)
values may be duplicated
dicts are commonly used to represent complex data
and to facilitate sharing between different languages in any stack
eg. JavaScript > json > Python > json > Java

use a class where you want a uniform list of props and functions that modify those props
use a dict where you have a one-off scenario or props/data shape change
'''

book = {}
book = dict()

# adding/updating props
book["title"] = "Scary Smart"#adds a key:value pair
book["author"] = "Mo Gawdat"#adds a key:value pair
book["published"] = 2019#adds a key:value pair
print(book)

# getting values
print(book["title"])
print(book.get("author"))

# there exist various other dict methods
print(pub_year := book.pop('published'))#mutates object, returns value for given key
print(book)# pop() REMOVES and returns specific prop
# 
# iterating:
for key in book:
    print(key)

for value in book.values():
    print(value)

for key, value in book.items():
    print(key, value)

# possible to use keys to access values
for key in book:
    print(f"{key}: {book[key]}")

# copying, references, deep and shallow copies
# applies to any object, container or class

book2 = book#copy of the book reference only
# one object: two references to same
book2["published"] = 2020
print(book)

# shallow copy
book3 = book.copy()
book3["published"] = 2021
print(book)#2020 - original unchanged

# the above ok for one level of reference
# IF, however, there are furyther NESTED references, 
# they will still be shallow copies
book["ratings"] = [4,4,3.5,5]
print(book)
book4 = book.copy()
book4["ratings"].append(1)
print(book)

# using the copy() module
import copy

book5 = copy.deepcopy(book)
book5["ratings"].append(0)
print(book)#completely immutable copying in one line!
print("all books:")
print(book)
print(book2)
print(book3)
print(book4)
print(book5)


