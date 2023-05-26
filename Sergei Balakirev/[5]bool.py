# Logical Values & Comparison Operators

# [>]: greater than
print(4 > 2)  
# True

# [>]: less than 
print(4 < 2)
# False


# [<=]: less than\equal to
a = 5
b = 7.8

print(a <= b)  # a less or equal to b

# [>=]: greater than\equal to
a = 3.1415
b = 4

res = a >= b
print(res, type(res))  # <class 'bool'>

# bool - True\False; logical values


# [==]: equal to  (not =, which is assignment operator)
print(5 == 7-2)  # comparison's operands can be even expressions
# as long as they return\produce numbers or comparable obj.


# [!=]: NOT equal to
x = 6
print(x != 6)  # content of x is NOT equal to 6
# False


# whole or odd:
x = 4
print(x % 2 == 0)  # whole means that it divides to 2 without remainder
# here you go

print(x % 2 != 0)  # checking if it's odd

# if you wanna know that certain number is a multiple of another num
a = 30
b = 10
print(a % b == 0)  # a is int multiple of b


# hit the range:

# [and]: checks if two adjacent conditions return True
y = 1.85

print(y >= -2 and y <= 5)

# wise versa.

# [or]: if first cond True - True; otherwise the value of 2nd cond.
print(y < -2 or y > 5)

y = -10
print(y < -2 or y > 5)
# True

# shortening the range check
y = 0
print(-2 <= y <= 5)  # chain comparison
# True


# x is multiple of 2 or 3
x = 6
print(x % 2 == 0 or x % 3 == 0)
# 6 is multiple of both of em

# if we wanna invert this condition
print(x % 2 != 0 or x % 3 != 0)
# we replace == with !=

# or we invert the whole thing at once
x = 11
print(not (x % 2 == 0 or x % 3 == 0))
# True

# brackets needed since [not] has the highest priority

# priority list:
# or: 1
# and: 2
# not: 3


# boolean converter: bool
# any number except 0 is true; 0 is False
print(bool(-1), bool(0), bool(1))  # True, False, True
print(bool(0.0))  # False

# any string except empty one is True; empty one is False
print(bool(" "), bool("abc"), bool(""))  # True, True, False
# space is a char too.
