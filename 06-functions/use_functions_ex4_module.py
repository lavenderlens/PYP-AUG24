from functions_ex4_module import get_greeting, \
    get_greeting_to, get_product, get_first, \
        get_name, get_circumference

print(get_greeting())

print(get_greeting_to("Matt"))

print(get_product(2,4))

nums = [1,2,3] #separately instantiated
print(get_first(nums))

print(get_name({"name": "martin"}))#passed directly

print(get_circumference(10))