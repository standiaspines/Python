# Variables

# var - container for any kind of data

variable = 'test'
# [varname] [assignment operator] [data]

10 + 5  # python did calcualte the result
# but Python was not told to print it out

print('result',  10 + 5)
# on the next stage you have var name and a value

result = 10 + 5
# assignment operator comes in between
print(result)

# you can use var in any other operation you want
result2 = result / 2
print(result2)  # the value stored in result was divided by 2


# Variable Naming Conventions
test = 'test'  # can contain letters

test_2331_CAPITALLetters = 'test'  # can caontain [_] and 0-9

# 2test = 'test'  # the first symbol CAN'T be a number
# SyntaxError: invalid decimal literal.

two_test = 'test'  # perfectly fine
two_test_2 = 'test'  # fine as well


# two test_2 = 'test'  # seems like there are two variables
two_test_2 = 't'  # several words can be linked through [_]


# Snake Case style:
snake_case = 'tss...'  # all seperate words start with lowercase
# and connected through [_]

test_variable_practice = 'test'
print(test_2331_CAPITALLetters, test_variable_practice)

test_2 = 'test'
print(test_2, two_test_2)  # correct; wrong


x = 'some words'
print(x)  # time passes, and name of a var can become
# CONFUSING!

num1 = 10
num1 = num1 + 8
print(num1)

num1 = 20
num1 += 4
print(num1)

# it works with other math operations as well
number = 7
number -= 4
print(number)

number *= 8
print(number)

number /= 2
print(number)

number //= 4
print(number)

number **= 3
print(number)


# Task:

# create a var in snake_case with any value
# increase it by 20 and then print it (3 lines in total)

beautiful_number = 1001
beautiful_number += 20
print(beautiful_number)

# or...
beautiful_number = 888; beautiful_number += 12
print(beautiful_number)
