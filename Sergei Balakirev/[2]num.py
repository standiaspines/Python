# Numbers

# int - even
# float - with decimal point
# comlex

print(0, 999, -1)  # int

print(6.7, -321.546, 0.001)  # float


# Arithmetical Operations

# [+] - addition
print(12 + 7)  # 19
# the result of expression is not stored anywhere

result = 12 + 7  # if wanted to be stored
print(result)


deci = 3 + 2.0  # when operating with int & float = float.
print(deci)


# [-] - subtraction
print(4 - 7)  # -3 negative output
print(6.9 - 1.9)  # still the result is float 5.0


# [*] - multiplication
print(2 - 2 * 8)  # math priority in action
# 14 | !0


# [/] - division
print(4 / 2, 17 / 3)  # result is always float
# 2.0


# [//] - integer division
print(10 // 3)  # straight opposite of [/]

print(-7 // 2)  # -4
# -3.5 was floored down to get the minimum value


# [%] - module division
print(10 % 3)  # division remainder
# 1

print(-9 % 5)
# when dividant is negative closest minimum value 
# which is -10, and difference is calculated
print(-9 - -10)  # 1

print(9 % -5) # we find closes value that excells dividant
# which is 10 | now: 9 - 10
print(9 - 10)

# Note: when both negative it's classic approach


# [**] - power
# power works right-to-left
# while other operations do left-to-right
print(8 ** 2)

# ** 0.5 is the same as square root
print(121 ** 0.5)


# Priority
print(2 ** 3 ** 2)  # 3 ** 2 | 9 ** 2
# right - to - left


# changing the priority
print(2 + 3 * 5)  # 17

print((2 + 3) * 5)  # 25 | changed priority


# short arithmetic assignment
i = 2
j = 7

i = i + 3
print(i)

j = j - 2
print(j)

i -= 1
j += 1
print(i, j)

abc = 27
abc //= 3

print(abc)

# any arithmetic operation can be shortened like this
# +\-\*\/\//\%\**= number
