print(10 + 5)
# result: 15

print(10 - 5)
# result: 5

print(10 * 5)
# result: 50

print(10 / 5)
# result: 2.0 [???]


# advanced operators:
print(10 ** 2)  # 100
# 10 to the power of 2

# floor divide: //
print(10 / 3)  # 3.33333333...

print(10 // 3)  # 3
# not rounding, BUT truncating

print(7 // 4)  # if you round: 4 cuz 3.5 roudned is 4
# result: 3

# getting the remainder
print(7 % 2)  # looking for 2-hold units to get the number
# |o| |o| |o| |o|
#        		[->o<-] # 1 unit that remains
# |o| |o| |o| |o|


# brackets
print(5 + 5 * 2)  # 15: multiplication has higher priority
print((5 + 5) * 2)  # barckets have the highest operator

print(10 > 5)  # result: True
print(10 < 5)  # result: False


# Task:

# average between 1 and 7: 1 + 2 + 3 + 4 + 5 + 6 + 7 / 7
numbers = list(range(1, 8))
result = sum(numbers)/len(numbers)
print(result)

print((1+2+3+4+5+6+7)/7)  # well...

# decimals are welcome:
print(1.1 + 5)  # 6.1
