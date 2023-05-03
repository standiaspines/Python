# What can programs do?

# store data
# calculate
# simulate conditions
# create loops


# Data in Python

print('Object - data form in Python')
# object can mean(have value) smth
print('object meaning 16')

# object - memory cell

print('to get access to certain object')
# we use links - vars

a = 7  # a - link's name
# whole statement itself is a var

print(a)  # using object's link to print its value

# equal(=) is assigment symbol

money_amm = 78
# money_amm's a new cell in memory that's been assigned a value

# print(name)  # u can not refer to non-existant var's

name = 'Jacob'
print(name)
name = 17  # u can reassign a var another value at any time
print(name)  # no matter of the value's type

# dynamic typization lets u assign the same var diff values
age = int(67)  # u can skip declaring the type of object


my_wallet = "14$"
her_wallet = my_wallet
# both vars are linked to the same area in the memory


# Cascade Assignment
a = b = c = 'wuba-luba-dub-dub'
print(id(a), id(c), id(b))
# to create severak vars refering to the same value


# Multiple Assignment
a, b = 'coffee', 'milk'
print(a, b)

a, b = b, a  # cross swapping values
print(a, b)


# vars can refer to any type of data
# to figure out what datatype is a var linked to

# func: type()
x = 6.4
s = 'Phantom'

print(x, type(x), s, type(s))  # <class 'type'>


# Naming Rules
# be careful naming values

# var names should be nouns
name = 'Stan'
age = 16


# don't use meaningless names
safagsdhg = 1.5
print(safagsdhg)  # u will soon forget what was that about


# Case-Sensitivity
arg = 0
Arg = 'str'
# both are different

# don't use keywords as names for vars
# True = 10  # big MISTAKE

# first symbol of the name should not be _ or 0-9
