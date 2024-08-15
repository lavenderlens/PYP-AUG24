total = 0

def add(num):
    global total
    total += num

def sub(num):
    global total
    total -= num

def mul(num):
    global total
    total *= num

def div(num):
    global total
    total /= num

def equals():
    global total
    return_value = total
    total = 0
    return return_value
