import re

address_list = []
while True:
    email = input("Enter your email address or 0 to quit:")
    # go to the online tool first to test your expression
    if email == "0":
        break
    email_pattern = '\w+@\w+.\w+.\w+'
    match = re.match(email_pattern, email)#returns boolean
    if match:
        print(f"email address {email} is valid")
        address_list.append(email)
    else:
        print(f"email address {email} is INVALID - not added to list")
print(address_list)