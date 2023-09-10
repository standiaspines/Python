# In(formal)tro

# * Using Python as a Calculator *

# int - type for integer numbers
print(type(5), 5)

# float - the ones with fractional part 
print(type(5.0), 5.0, type(2.56), 2.56)

# math expressions' syntax is pretty straightforward
# [+]; [-]; [*]; [/] <-- add, subtract, multiply and divide

# as simple as that
print(2 + 2)

# little math rules work here too
print(50 - 5 * 6)  # first we multiply then do the addition


# ? () can be used to group expessions ?
print((50 - 5*6) / 4)  # division always returns a float

print(8 / 5)  # even with no remainder case


# floor division is done using doube slashes [//]
print(21 // 6)  # 3, cuz nearest(to 21) value that divides to with 0 remainder is 18


# to calculate the remainder use [%] <-- modulo division
print(21 % 6)  # 3 is also the remainder

# floored quotient * divisor + remainder
print(3 * 6 + 3)  # back to 21


# to calcultae powers use [**]
print(8 ** 2)  # 8 squared

# 2 to the power of 7
print(2 ** 7)


# to assign a value to a variable use [=]
width = 20
height = 6 * 7

print(width * height)


# if variale is not "defined" (not assigned a value), error occurs
# print(n)  # no variable called "n" at the moment


# full suppport of float
print(4 * 8.75 - 1)  # operators with mixed operands will convert [int] to [float]


# ? in interactive mode, the last printed output is assigned to var by name '_'

# beside int & float, python supports: Decimal, Fraction and complex numbers
# j or J suffix is used to indicate the imaginary part: 3+5j



# * Text *

# text is represented by type str, so-called "strings"
print('?!#', 'turtle', 'Norway', 'Be right back!')  # symbols, words, names & sentences
# etc.: Yay! :)

# ? they can be enclosed in single ('...') or double quotes ("...") ?

print('game over', "Goin' Back to Indiana")  # single\double quotes
# you can use single quotes inside double one & double ones inside single ones

print("1941")  # digits and numerals in quotes are also strings


# quote a quote

print('doesn\'t')  # backslash [\] --> is an escape character
# now the single quote won't confuse the interpretator
print("doesn't")  # again you can quote singles in doubles

print('"Yes," they said')
# without an escape char
print("\"Yes,\" they said")

# mix
print('"Isn\'t," he said')


# definition and output can look different with strings

s = 'I smiled at my reflection.\nThank god it smiled back this time.'
# \n - new line character
print(s)  # when mentioned the var name in console you see the embing quotes
# and don't see the special characters

# ? print produces a more readable output, omitting enclosing quotes, including \chars ?

# if you want special chars to be ignored, use raw stinrgs by putting r before 1st quote
print('C:\windows\name\telegram')  # \t means 'tab'; \n is 'new line'

# now try raw strings
print(r'C:\users\name\telegram')


# mulitple lines spanned in strings

# ['''...'''] & ["""..."""]: triple quotes
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
# end of lines are automatically included in strings, but you can avoid that using \
# which is why there's no new line before the word 'Usage'


# concatenation: gluing 2 strings together
print('alimi' + 3 * 'ni' + 'um')  # aliminium

# strings can be glued together using [+]; and repeated using [*]

# 2+ string literals written next to each other are automatically concatenated
text = ('No one know how it feels like to be on the other side of the arc. '
		'To be the accidentally created villian. It hurts...')
# put several strings within brackets to get them glued to e.o
print(text)

# ! only two LITERALS put next to each other are concatenated !

prefix = 'Jy'
print(prefix + 'thon')  # to concated variables with(out) literls use [+]


# strings are indexed with the 1st character having index 0
word = 'Stanward'

# 1st character at index 0
print(word[0])  # 'S'

# last character at index 7
print(word[7])  # 'd'

# indices may also be negative numbers
print(word[-1])  # easier way to get the last char. no counting

print(word[-3])  # third-last character

print(word[-8])  # last-last character or just first char


# slicing - can help you get not only an individual char but a substring
print(word[0:4])  # my name can be short

# a whole another name hidden in my name
print(word[2:7])  # anwar :)


# helpful defaults
print(word[:4])  # ommited first index defaults to 0
# my name shortened again

print(word[4:])  # omitted second index defaults to the size of the string being sliced

# ? start is always included & the end is excluded ?
# ? so this makes s[i:] + s[:i] equal to s. look at it again. ?
print(word[:6] + word[6:], word[:4] + word[4:])  # wow


# ?   +---+---+---+---+---+---+   ?
# ?   | P | y | t | h | o | n |   ?
# ?   +---+---+---+---+---+---+   ?
# ?   0   1   2   3   4   5   6   ?
# ?  -6  -5  -4  -3  -2  -1       ?
# cool cheat to remeber the indexes

# when indexing you can go outta range word[42] is an ERROR
# while oppositely, when slicing you can't word[42:] is '' & word[5:42] is 'ard'

# Python strings are immutable - they can't be changed
# therefore, assigning to an indexed position in the string results in error
# ! word[0] = 'E'

# if you need different string, create a new one
new_word = 'Ed' + word[4:]
print(new_word)

new_name = word[:4] + 'ford'
print(new_name)


# ? built-in function len() returns the length of a string ?
s = 'supercalifragilisticexpialidocious'
print(len(s))


# * Lists *

# ? list - seq. comma-seperated obj's between square brackets, often the same type ?
squares = [121, 81, 25, 64, 4]
print(squares)

# like strings and any other built-in sequences list support indexing and slicing

# 1st and last elements
print(squares[0], squares[-1])

# ? slicing returns a new list ?
print(squares[-3:])

# which means you get a shallow copy doing this:
print(squares[:])


# concatenation with lists
print(squares + ['a', 'b', 'c', 'd', 'e', 'f'])

cubes = [1, 8, 27, 65, 124]  # cube of 4 is 64 not 65, and 5 ** 3 is 125
print(cubes)

# so let's fix that
cubes[3] -= 1
cubes[-1] = 125
print(cubes)


# new items can be added at the end of the list using method [append()]

cubes.append(343)  # cube of 7
cubes.append(8 ** 3)  # we don't need cube of 6
print(cubes)

# you can even assign to a slice
letters = list('abcdefg')  # function used to create lists outta iterable obj's
print(letters)

letters[2:5] = ['C', 'D', 'E']
print(letters)

# or they can be removed
letters[2:5] = []
print(letters)

# or we can clear the whole list out by replacing all the elements with an empty list
letters[:] = []
print(letters)


# built-in function [len]
letters = list('abcd')
print(len(letters))


# Nesting lists
# ? nests can contain other lists ?
a = ['a', 'b', 'c']
n = [1, 2, 3]
print(a, n)

x = [a, n]
print(x)

print(x[0])  # first element of 'x' is another list from var 'a'

print(x[1][-1])  # last element('n' level) of second element('x' level)

