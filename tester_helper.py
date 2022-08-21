import random
from string import digits, ascii_letters


def pw_generator(length=8):
    s = ''
    for i in range(length):
        s += random.choice(digits + ascii_letters)
    return s


print(pw_generator())


def ID_generator(length=8):
    s = ''
    for i in range(length):
        s += random.choice(digits)
    return s


print(ID_generator())
