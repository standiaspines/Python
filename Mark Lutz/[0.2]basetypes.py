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
