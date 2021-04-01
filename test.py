import math


def abs_sign(a):
    if a >= 0:
        return a
    else:
        return -a


def abs_square(b):
    c = b * b
    return math.sqrt(c)


print(abs_sign(5))
print(abs_sign(-3))

print()

print(abs_square(5))
print(abs_square(-3))
