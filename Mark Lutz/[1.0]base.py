# Introduction to Data-Types

# Programs do certain actions on things

# certain actions - operations that build up the program
# things - objects that operations work with

print("Data in Python is an Object containing a value")
# there are some built-in objs and u acn create ur owns too

print(
    "Basically, data is a memory area with value and attached\
 operations that can be proceeded upon it"
)


# Hierarchy of program components:
print("Programms divide into modules")
# module - file containing commands and expressions

print("Modules contain commands")
# commands that are performed and executed by an interpreter

print("Commands consist of expressions")
# experssion - single unit commands

print("Expression render and produce objects")
# object = smallest unit


# Basic Data Types
# to create objects in certain type use literals

print("literal - expression specific for all types")


# numbers - digits
print(1234, 3.1415, 3 + 4j)


# strings - text
print("spam", "stan'o'war", b"a\x01c")


# lists - collection
print([1, [2, "three"], 4])


# dictionary - search grids
print({"20": "Wendy", "age": 16, "quality": "cute"})


# tuples
print((1, "spam", 4, "U", True))


# files
# myFile = open('crack.txt', 'r')
# print(myFile)

# set - unordered collection
print(set("abc"), {123, "banana", True})


# other basic types
print("types themselves", None, "logical values")


# structural elements
class Ape:
    def __init__(self) -> None:
        pass


def walk():
    pass


print(Ape, walk, "modules")


# development associated types
print("compiled code", "call flow")


# Numbers

print("Base:", "int(even numbers)", "float(with decimal point)")

subtraction = 17 - 21.4
# symbol dash means subtraction

division = 10 / 5
# symbol slash means division

power = 2**10
# double star means power up

print(subtraction, power, division)

"""
float can be strange at first
>>> 3.1415 * 2
6.2830000000000004
>>> print(3.1415 * 2)
6.283

#1 - repr(program code that calculates precisely)
#2 = str(output readable and convenient for a reader)
"""

print("Beside expressions there are some modules")

import math

print(math.pi)

print(math.sqrt(121))
# module math contains more complex mathematical operations


import random

print(random.random())

chosenOne = random.choice(["Jake", "Tanisha", "Greg", "Mike"])
print(chosenOne)
# module's name speaks for itself


# Strings
print("text info is expressed as strings")
# plus it's the basic example of collections\sequences

# elements are stored and ejected by it's index in a seq.
print("string is just round of seperate letters")

# operations under sequences


# function len() and indexing are appliable to str to as seq.
long_phrase = "wuba-luba dub-dub"
print(long_phrase, len(long_phrase))  # 17 symbol long

# certain precise symbol can be accessed using indexing
name = "stanward"
print(name[0])  # count starts at 0
# so first symbol has index 0

print(name[-4] + "endy")  # negative index uses reversed count

# vars are not declared in advance
# they're created in a process of value assignment

print("Var can be assignment any datatype")
# when used in expressions name of var replaced with its value

# for var to be used it should be assigned a value first
# to save a value for a later use store it in a var

word = "all grils are the same"
print(word[4], word[-4])  # pos. index from left | neg. from right

# formally negative indexes come with string length
print(word[-8], word[len(word) - 8])  # same result | but 1st's compact

print("It's not strictly only literals are allowed in value receivers")
# expressions & vars are also welcome

# from math import ceil

nick = "wendy"
print(
    nick[len(nick) // 2] + " is in center of" if len(nick) % 2 != 0 else "no center in",
    nick,
)
# i used function call + var + arithmetic operation instead of index


# Slicing
# to cut off a part of the current string - segment\sub-string
meal = "pizza"
print(meal[1:4])  # ejecting a row of symbols at a time
# str[start:end]   # ending point is not included in new cut object

print(meal[1:])  # all except first
# default values for start:end points are> 0:len(str)

print(meal[:4])  # the same as [0:3] | all except last

print(meal[:-1])  # same as previous

print(meal[:])  # copy of original

# Concatenation
# getting a new string by gluing together other 2 strings
s = "Steve"
print(s + "n Strange")  # Dr.Strange


# Repeat
# getting a new string by multipling another string
lol = "ah"
print(lol * 6 + " XD")


# Immutability
print("Strings can NOT change! They are cloned with alternations*")

platform = "land"
print("U're on:", platform)

# platform[0] = 's'  # !!! can't do that
platform = "s" + platform[1:]
print("U're on:", platform)


# numbers, strings & tuples are immutable
# lists & dicts can change at anytime & any of their part


# Specific Operations
# attached and are run by calling them like function


# find & replace
# 1: finds a substring in a string | 2: global search with replacement
word = "Python"

print(word.find("!"), word.replace("P", "J"))  # -1 search was failed
# all uppercase P's were replaced with J


# split
# breaking down a sting by certain symbols
line = "aaa,bb,ccccccc,dddd"
print(line.split(","))  # breaks down everytime coma's met > list


# upper > raises symbols to uppercase
word = "eggs"
print(word.upper())


# isalpha > checking content for alphabetical symbols
print("abZZzz0".isalpha())  # 0 is not in alphabet


# isdigit > checking content for numeric symbols
print("909251795".isdigit())  # all numbers


# rstrip > deletes ending whitespaces
line = "the end..         \n\n\n  "
print(line.rstrip())

# formatting
# 2.6
print("%s is turning %d today! %s" % ("Simon", 18, "HOORAY!"))

# 3.0
print(
    "{1} was noticed with {0}{3} in her {2}".format(110000, "Shu", "credit card", "$")
)


"""
# GETTING HELP
# func: dir
# calling a dir function on an object will return list of operations
abailable on the type
"""

name = "Susan"
print(dir(name))

# to see what does certain method or function do
# func: help
print(help(name.lower))


# More about strings
# speical characters marked with backslash before them

s = "A\nB\tC"  # \n - end of a line  # \t - tab
print(s, len(s))  # special characters count as 1 character

print(ord("\n"))  # byte with 10 num value

s = "A\0B\0C"  # \0 is binary 0 | it's not a period
print(s)


# Multi-line string literals
msg = """Get the hell outta my face.
U know what u did, boy?

U lettin baby mama down, bitch
Fuck yo attitude, dumb ass

Craig.
"""

# when string continues by a new line it puts \n at the end.


# Template Search
# there's no support of a template search

# module 're' is used to deal with this problem

import re

mat = re.match("Hello[ \t]*(.*) world", "Hello   Python world")

print(mat.group(1))

# start with Hello _\t [anything'd be groupped as match] world

mat = re.match("/(.*)/(.*)/(.*)", "/stanward/projects/wardonut")
print(mat.groups())


# Lists

"""
List - index ordered collection of objects of varying types
number of which is not limited.
"""

print("Lists are mutable")
# they can change through offset assignment & with their methods

print(
    "since they support same operations as str, \
only thing differing should be resulting datatype"
)
# which is [list] not [str]

L = [5135, "wardolyn", 0.223]
print(len(L))  # getting length of a list

print(L[-1])  # accessing object through its index
# last object in the list

print(L[:-1])  # slicing sublist from a parent
# with all objects except last

print(L + ["scrap", True, 101001])  # concatenation
# which like slicing - creates a new list

print(L)  # proof that nothing didn't change in the OG list


# Lists' specific methods

# !- lists can store not only one type of data -!
# the last list had three datatypes in it

todo = ["make tea", "code", "play ball", "buy batteries"]
print(todo)


# .append() - adds given object to the end of the list
todo.append("sleep 2hrs")
print(todo)


# .pop() - removes and returns removed object, by index | 0
done = todo.pop(-2)
print(todo, done)

# analog: del todo[index]
del todo[0]
print(todo)

# .insert - adds the object in needed cell [index]
todo.insert(1, "web dev 1.5 hrs")
todo.remove("play ball")
print(todo)


# since lists are mutable, most methods process with OG list
todo.sort()  # sorts out in binary order | ord() for help
print(todo)

todo.reverse()  # reverses the order of elements
print(todo)


# Range pass check
print(
    "Tough, theres no certain size range, \
Python prohibits refering to non-existant elements"
)
# so passing the index range will always lead to an ERROR

# print(todo[7])  # let's see what's the 8th task in the list
# oops there's only 3 tasks

# todo[7] = 'water trees'  # u cannot even assign anything
# first assign value for a 3rd element


# Nested Lists

# great feature of collections: they can nest each other
# any combination's possible

# Matrix
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(M)  # the list containing 3 other lists that make up 3x3

# u can adress the structure in several ways
print(M[1])  # second line access

# or specific element outta any of those lists
print(M[-1][0])  # first object of the last list
# connected indexing operation can go as deep as needed


# List Comprehension

# it simplifies processing structures like matrice m.b
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# let's say we need the second column
print(M, "But I'm made of rows")

col2 = [row[1] for row in M]  # picks out 2nd col. elements
print(col2)

# does that effected the matrix anyhow?
print(M, "Nope. Same old row-ish matrix.")

"""
Comprehensions let u create new sequences, applying commands &
expressions on every element of a sequence, by one at a time.

They embed in square brackets to show that they process a list,
and use loop construction that uses one var name for whole the
wole process. [ejecting (1)2nd element for every 'row' in M]
"""

# comprehensions can get more complex with practice
col3_div = [int(row[-1] / 3) for row in M]
print(col3_div)  # 3rd column values divided by 3

col1_odd = [row[0] for row in M if row[0] % 2 != 0]
print(col1_odd)  # even numbers in 1st column skipped
# comprehension uses if-checks to exclude even nums from result


# comprehension can be applied to any sequence supporting iter.
diag = [M[i][i] for i in [0, 1, 2]]
# picking elements on grid's diagonal
print(diag)


doubles = [c * 2 for c in "spider"]  # doubling str symbols
print(doubles)  # the result of comprehension is always a list


# embing comprehension in () brackets u can control the result
G = (sum(row) for row in M)
print(next(G))
print(next(G))
# elements of rows summarized


# Interesting Analog
"""
Using function [map], u generate outputs, feeding objects to other
function. Packing the call of [map] function - forces it to push
all values.
"""

G = list(map(sum, M))  # iter picks up lists from a list
# which is then processed with [sum] function
print(G)


# comprehension syntax lets u process [dicts] and [sets]
sums_pack = {sum(row) for row in M}
print(sums_pack)

# pair key table
sums_md = {M.index(row): sum(row) for row in M}
sums_md_bookV = {i: sum(M[i]) for i in range(3)}  # not uni
print("mine version:", sums_md, "book's version:", sums_md_bookV)


# comprehensions can do: lists, dicts & sets
char_code_list = [ord(l) for l in "Stanward"]
print(char_code_list)

no_duplicates = {ord(l) for l in "Stanward"}
# set can't contain two identical elements
print(no_duplicates)

# keys are genuine
better_storage = {l: ord(l) for l in "stanward"}
print(better_storage)  # case-sensitivity!


# Dictionaries
"""
# they are not sequences, but displays
# displays - collections, elements of which are accessed not by
their offset but by the keys they're attached to.

No indexing and order apply to dicts. It's like pack of vars:
they have keys(names) and values.

Dicts are the only display type & they're mutable & can change
their size anytime they're wanted to.
"""

print("Syntax -", "key:", "value")  # embed in {} brackets

dinner = {"food": "sanwich", "quantity": 4, "content": ["jam", "butter"]}

print(dinner["food"])
# adressing elements is done by putting their key in [] brackets
print("I ate 2 already")

dinner["quantity"] -= 2
# changing value of an amount key
print(dinner)


# refering to non-existant key
print('dictionaries in action are primarily empty')
stomach = {}

print('then they\'re filled up with content during process')
stomach['breakfast'] = 'veggie sandwiches'
stomach['dinner'] = 'mama\'s meal'

# if you refer to non-existant key, u won't see an error
# but creation of a new key
stomach['lunch'] = None

'''
Later u will use dicts as a search tool since they work faster
than search mechanisms implemented in Python.
'''


# Nested ?

rec = {'name': 'Tahir',
       'job': 'pixel artist',
       'age': 16.8}

# this is an example of simple dict
# looks like paper forms, ain't it?

print(rec)  # but what if we need more complex structure

# like full name and multiple occupations

rec = {
    'name': {'first': 'Stan', 'second': 'Pines'},
    'job': ['pixel artist', 'coder'],
    'age': 16
}
print(rec)

# so there are three highlevel keys: name, job, age
# and child keys that are nested in name key: first & second names
print(f"Mr.{rec['name']['second']}")

# we have list of job occupations, that can be expanded in a long-term
print(f'He a {rec["job"][0]}')

rec["job"].append('video-editor')
print(rec)

# nested list is a seperate area in the RAM so it can expand with no lim.
print("He a bad", rec['job'].pop(0), 'tho.')
print(rec)


# unused data is removed from RAM, when last link to it dissapears
rec = 0  # for example container's been assigned other value
# HAIL to the PYTHON'S TRASH COLLECTOR


# Sorting by keys
D = {'a': 1, 'c': 3, 'b': 2}
# since dicts are not sequences they don't support any sorting approaches

print(D)  # but what if we need them to be sorted?

# we can get list of all keys using .keys() method
ks = list(D.keys())  # then sort em up using list's .sort() method
print(ks)

ks.sort()
print(ks)

# printing em out through iteration
for key in ks:
    print(key, '=>', D[key])

# this process consisting of 3 stages can be shorted to single operation
for key in sorted(D):  # built-in function sorted
    print(key, '=>', D[key])
# it can sort different objects and return result


# a little about loops
# you can use for loop for carrying out sequence traversals
# and while going through them execute block of code on each of em
room = ['[@]', '[$]', '[&]', '["]', '[:]', '[/]', '[`]', '[*]']
for box in room:
    print('Oh look! A box:', box)

# variable defined by the user is a link to the current item of a seq.
# [box] in the e.g.

print('''
for and its relative while loop are the main ways to implement repetetive
actions in scripts.

for is a sequence operation, and it works with objects that are sequences
and with some objects that are NOT sequences.
''')

for c in 'spam':
    print(c.upper())
# so here's the string traversal that prints out letters in an upper case


# while loop represents more universal tool for executing repetetive act.
x = 4
while x > 0:  # it's not directly connected to sequential obj.
    print('spam!' * x)
    x -= 1


# Iteration and Optimization

print('comprehensions and loops are very similar')
# they both able to work with any object that support iteration protocol

print('iter. -  when object generates(returns) one item at a time')


# if iterable obj. returned, when it's given to iter() func.
# obj. is iterable

# iterable - means you get an object that allows you to traverse
# when called function next() with that obj. as an argument


# any mechanism that scans the object left-to-right uses iteration
# next() with dicts return the next key

squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)  # any comprehension like the given one

# can be implemented using for-loops
squares = []
for x in [1, 2, 3, 4, 5]:
    squares.append(x ** 2)

print(squares)  # same result


# however: comprehensions and related mechanism like map and filter
# proceed and execute faster | nearly 2x speed

# python is developing language so optimization figures 
# can differ from-version-to-version

print("Readability > Performance")

# so when it comes to optimization you will meet instruments, like:
# time, timeit & profile


# KeyError: if-conditions

D = {'a': 1, 'c': 3, 'b': 2}
print(D)

D['e'] = 84
print(D)

# wanna_see_an_error = D['f']  # KeyError: 'f'
# print(wanna_see_an_error) 
# although, assigning to non-ex key, creates one with that name & value
# refering to non-ex key can lead to an error | can't do that!


# so we wanna check if certain key is in dictionary
print('f' in D)  # False | there's no key called 'f' in D
# operator in [check for a membership xd]

if not 'f' in D:
    print('missing')

# if --> expression (true\false) --> block of code that executes w\true
# full formation of if-conds can include else(default action block)
# and 1 or more blocks of elif(else if)  # for other conditions

print('There are other ways of creating dicts')
# and non-ex key refering error exceptions

# method: get | addressing which you can give default output
value = D.get('x', 0)  # method returns 0 if key's not found
print(value)

# try <-- takes over an error and process an exception
# conditional operator if shrank down to 1-line
value = D['x'] if 'x' in D else 'not found'
print(value)


# Tuples

# generally a list that can not be changed
# tuples are seq's but immutable like str

# syntax: ()  <-- round brackets are used to create a tuple literal
# they also can store any type of data; support sequential operations

T = (1, 2, 3, 4)
print(len(T))  # returning the length

# or accessing the item through its index
print(T[-1])  # negative 1: 4


# tuples have 2 methods that are appliable to sequences\collections
print(T.index(1))  # getting the index of the item(1)

T = (1, 0, 2, 3, 0, 4)
# counting the amount of given item that's in the tuple
print(T.count(0))  # there're two 0's


# main difference is that; you can't change it after its created
# T = (1, 0, 2, 3, 0, 4); T[-2] = 5  <-- leads to an error


T = ('spam', 3.0, [11, 22, 33], True, (255, 255, 255))  # can't store anything
# supports nesting; but can't change its size; IMMUTABLE


# then, why do we need those? they provide you with unity
# for example, if components of program should not be able to alter the seq.
# use tuples!


# Files

# file objects - main interface amoung program code and external files in h.d
# h.d - hard drive

# basic, but unusual (since you can't create 'em as literals)
# instead, use built-in function open; give access mode and directory path


# e.g:
f = open('lutz.txt', 'w')  # 'w' - write (mode that is used to output)
# so u give filename and the mode 'w' to create an output text file

f.write('Hello\n')  # writing text in the file
print('See in The Explorer')

f.write('world\n')

f.close()  # closes the file, pushes output buffers to the drive

# filename can contain full path, if file's stored somewhere else

# 'r' - read; to read what's in the file
print('Let\'s read using default mode \'r\'')  # which is put; if arg. skipped
# content is perceived as 'a string' <-- always.

f = open('lutz.txt')  # let's skip the 'r'

text = f.read()  # file is read as a whole
print(text)  # let's print em out; outputting on the console ignores s.c
# s.c = speical characters

words_in_file = text.split()
print(words_in_file)


f.close()
# method .read() has optional arg. - byte amount
# readline .readline()  reads one line at a call

f = open('lutz.txt', 'r')
print(f.readline())
f.seek(0)  # seek relocates the scan position

print(f.readlines())
# it's not recommended to read the file content all at once

# files provide iterators that can be used in for-loops or any other context
print('Text content: UNICODE characters are en\\de-coded')

# binaru content
print('Binary content are presented as specific byte-strings')
# content is not transformed or changed

data = open('rain.xnb', 'rb').read()
print(data)  # long byte-string

# this is SV's rain tyle-sheet
print(data[0:3])  # this is its format


# Other Basic Types:

# Sets - collection of unique and immutable objects
# syntax: {}  <-- dictionary with no values

X = set('crononberg')  # can be created using sequences
Y = {'h', 'a', 'm', 'b', 'u', 'r', 'g', 'e', 'r'}

print(X, Y)  # no duplicate(r, o, n) in X, and no second r in Y 

# binary operations (that i don't understand, yet*):
print(X & Y)  # crossover; defines what two sequences have in common

# conjuction; concatenation (but with sets, duplicates are removed) 
print(X | Y)

# difference
print(X - Y)  # opposite of crossover; what's different in between


# Set Comprehension
Z = {x ** 0.5 for x in [81, 49, 36, 25, 121, 64]}
print(Z)


# Floats with Fixed Preciseness & Rationals (numerator + denominator)

# 2 ways of access:

# New Floats
# ~ 1: 
bad = 1/3
print(bad)  # kinda no fixed preciseness

# ~ 2:
import decimal
good = decimal.Decimal('3.141')

print(good + 1)  # here you go, simple example

# now look:
decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
# you get precisely two numbers after flaoting point


# Fractionals

# ~ 1:
bad = (2/3) + (1/2)
print(bad)

from fractions import Fraction
good = Fraction(2, 3)
print(good + 1)  # (1 (2/3) ==> (5/3))


# logic in Python: True & Falls: that are (1, 0) in action
print(1 > 2, 1 < 2)  # False, True

print(bool('spam'))  # string contains smth but not nothing: True

# here u go:
print(int(True), int(False))  # as it been said


# None: used in primary\temporary initiation of var\obj's

x = None
print(x)  # temporarily empty

x = 'smth...'
print(x)  # now contains smth

L = [None] * 34
print(L)  # like a brand new notebook


# WHAAA???
print(type(L))  # nothing special; printing out the type of the object in L
# which is 'a list'; <class 'list'>

# but what if
print(type(type(L)))  # even types themselves are objects


# checking the type (if needed)

if type(L) == type([]):  # no comments; quite easy
    print('yes')


if type(L) == list:
    print('you can do it using the name of the type')


if isinstance(L, list):  # Objective-oriented style
    print('yessir')


# checking if object belongs to certain type class spoils the flexibility in code
# there IS need to control types, and IS supported, but don't think THAT way!!!

# polymorphism: you code can serve wider range of types...


# classes defined by the user

print('Classes define new data-types')

class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)  # * hdiw?


# given class defines new type(for office workers, let's say)
# it has two attributes: name, pay (smt attr are called status info)

# plus, there are two bahavior scenearios (type's methods)
# refering to class' name as to the function creates a new sample of a type
# object with that type*

# methods get link to the current sample, that's proccessed by them
# (argument: self)

bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Jones', 60000)

print(bob.lastName())

sue.giveRaise(.10)
print(sue.pay)


# all beings in Python - classes

# only discussed types are basic, and are runners for NOT basic types
# NOT basic types are based on the basic types
# and are part of (functions, modules, classes, objects of compiled code)
# and AIN'T syntax elements.
