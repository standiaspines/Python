# Numbers

# ! Basic Numeric Types !
print('Python has bunch of related numeric types')
# plus, some expressions for processing upon them

print('There are usual(int, float):', 248, 0.01, 'and extra support (other types)')


# * Numeric Literals *

# Number can be written in binary, octal, hex numeric system
# Length of a number is only limited by your memory capacity

# ordinary integers
print(84, 1234, 0, 999999999999999999999999, -1)

# floating point numbers
print(1.23, 1., 3.14e-10, 4E210, 4.0e+210)

# octal, hexidecimal and binary literals (version 2.6)
# print(0177, 0x9ff, 0b101010)

# (version 3.0)
print(0o177, 0x9ff, 0b101010)

# literals of complex numbers
print(3+4j, 3.0+4.0j, 3J)


# *Notes*
# * when python meets a floating point in a num, it starts using math for floats
# * there're 2 types of ints in P2.6: usual 32-bit nums; long ints (end with L or l)
# * which unified into 1 in P3.0: automatic unlimited preciseness support
# * hex: 0x + (0-9, A-F); octal: 0o + (0-7); binary: 0b + (0/1) | not case sensitive

# in P2.6 octal nums could be written without "o"; now it can mix up with decimals so...

# ? all literals create integers with just different presentation ?
# to create a string containing num with any 3 systems' presentation:
print(hex(0x5F6C1D23), oct(0o4427), bin(0b1))

# converting can be done with consideration of numeric system
print(int('0x0A1B0192F', 16), int('0b10', 0), int('0o10', 8))

# * complex nums: real_part + imaginary_part (imag_part ends with j/J)
# technically real_part isn't neccessary; complex: float and float but math is for cmplx

print(complex(4.1j, 3.8j))# built-in func for complex nums

# ? literals of other types: some types're created with funcs defined in external mod. ?


# * Built-in Numeric Operations and Extensions *

# expression operators:
print('expression operators:', '+', '-', '*', '/', '>>', '**', '&')  # etc...

# built-in math funcs:
print(pow, abs, round, int, hex, bin, oct)  # etc...

# helpful modules:
import random, math  # and others...
print(random, math)

# besides, each type has its own methods


# * Expression Operators *

# expression: combination of nums(or other types) and operators, which return values
'''
it's the cooperation of math notation and operators:

for example, to sum up two nums(X and Y): X + Y
which tells python interpretator to:
apply operator(+) to valuezs with names X and Y, which will result in a new num value
'''

# List of ALL Operators
print('yield x', 'send protocol support in generator funcs', sep=' | ')
print('lambda args: expression', 'creater anonymous func', sep=' | ')
print('x if y else z', 'x is processed only if y is true, otherwise z', sep=' | ')
print('x or y', 'logical OR; x is calcualted only if y is True', sep=' | ')
print('x and y', 'y calculated only if x is True', sep=' | ')
print('not x', 'logical negator', sep=' | ')
print('x in y, x not in y', 'entry check (for iterables)', sep=' | ')
print('x is y, x is not y', 'indentity check', sep=' | ')
print('x < y; x <= y; x > y; x >= y', 'subset/superset check; comparison', sep=' | ')
print('x == y; x != y', 'equality check', sep=' | ')
print('x | y', 'binary OR; union of sets', sep=' | ')
print('x ^ y', 'binary XOR; symmetric difference of sets', sep=' | ')
print('x & y', 'binary AND, set intersection', sep=' | ')
print('x << y; x >> y', 'shifting x by y bytes right/left', sep=' | ')
print('x + y', 'addition, set concatentation', sep=' | ')
print('x - y', 'subtraction, set difference', sep=' | ')
print('x * y', 'multiplication, repetition', sep=' | ')
print('x % y', 'remainder, formatting', sep=' | ')
print('x / y; x // y', 'division: true and with flooring', sep=' | ')
print('-x; +x', 'unary minus; indentity', sep=' | ')
print('~x', 'binary NOT(inversion)', sep=' | ')
print('x ** y', 'exponentiation', sep=' | ')
print('x[i]', 'indexing in sequences/mappings/and other obj', sep=' | ')
print('x[i:j:k]', 'slice extraction', sep=' | ')
print('x(...)', 'call(of a function/class/and other callable obj)', sep=' | ')
print('x.attr', 'accessing an attribute', sep=' | ')
print('(...)', 'tuple/subexpression/generator expression', sep=' | ')
print('[...]', 'list/list comprehension', sep=' | ')
print('{...}', 'dictionary/set/set & dict comprehension', sep=' | ')


# * Mixed Operators and  Defining Operator Priority *

# like in other PL's you can create combined/compound expressions
# sum of multiplications: A * B + C * D
# when operator sees expression containing more than 1 operator it divides into parts
# then calculates them in priority order

X, Y, Z = 3, 2, 6
print(X + Y * Z)  # first multiplication: 12; then addition: 15


# * Grouping Subexpressions with Brackets *

# subexpr in round brackets are always calculated first then they blend into rest of expr
# e.g
print((X + Y) * Z)  # now 30

# this one doesn't change anything
print(X + (Y * Z))  # meaningless use of brackets

# ? brackets not only raise the priority but make code more readable ?


# * Mixing Types and Transformation *

# 40 + 3.14
# ? what's the result? int or float ?
# answer is simple: interpretator converts operands to a type of compound operand
# then applies math that's specified for that type

# short description of complexitiy range: int < float < complex

# forced conversion:

# int
print(int(3.1415))  # cuts out the floating part

# float
print(float(3))  # converts into floating point number


# reloading operators and polymorphism

print('2 + 3:', 2 + 3, '<-- addition with nums')
print('[1, 2, 3] + [4, 5, 6]:', [1, 2, 3] + [4, 5, 6], '<-- concatenation with seq.')

# polymorphism - operation depends on types of objects-operands upon which it's running



# ! Numbers in Action !


# * Variables and Simple Expressions *

# vars - names that are assigned values; so that u use them as placeholders
# ? vars created using assignment operation ? 
# ? when calculating expressions names of vars are replaced by their values ? 
# ? before var can go in use, it should be given a value ?
# ? vars are links to objects and ARE NEVER declared in advance ?

a = 3
b = 4

# addition (3 + 1); subtraction (3 - 1)
print(a + 1, a - 1)

# multiplication (4 * 3); division (4 / 2)
print(b * 3, b / 2)

# modulo division/remainder (3 % 2); exponentiation (4 ** 2)
print(a % 2, b ** 2)

# mixing types, transformation happens
print(2 + 4.0, 2.0 ** b)

# ? if it was an interactive session; result of a % 2, b ** 2 would be a tuple (1, 16) ?
# ? cuz lines contain 2 expressions divided by comma ',' ?
# ? we use no print in interactive shell, since the result is displayed automatically ?

# all works smooth since a & b are given values first
# ! print(c * 2)  # NameError: name 'c' not defined. it shoulda been given a value !

# more compound examples:

# priority 
print(b / 2 + a)  # same as: ((4 / 2) + 3) 
# / in P3.0 returns float num

# transformation
print(b / (2.0 + a))  # (4 / (2.0 + 3))
# forcing + operator to be calculated first using (); plus mixing types float + int


# * Formats of Displaying Numbers *

# in interactive shell the result of last calculation can be a bit different:
# b / (2.0 + a) --> 0.80000000000000004

print(b / (2.0 + a))  # print drops extra nums
# ? we got that strange result cuz machinary we operate is limited on float math ?

# example was used to demonstrate the difference between automatic and print's display

# * repr() func as it was said before can be used to fix that problem *

num = 1 / 3.0
print(num)  # 0.33333333333333331 was rounded to 0.3333333333333333

# plus, you can format it yourself
print("%e" % num)

# alternative format presenting float
print('%4.2f' % num)  # ?

print('{0:4.2f}'.format(num))  # new style of formatting for P2.6 & P3.0

# presentation format: repr & str
num = 1 / 3
print(repr(num))  # used for automatic output, like in interactive shell

# friendly format
print(str(num))  # used by print

# ? both funcs convert objects into their string presentation ?
# * repr: outputs obj's the way they were given in the code *
# * str: more friendly way of delivering objects into the console *

# ? interactive shell uses repr() ?
# ? print func uses str() ?


# * Comparison Operations: simple and chained *
 
# operators are the same as in math: they return logical value (True\False)
print(1 < 2)  # less than

# ? mixing different types in comparison is allowed; only if both types are numeric ?
print(2.0 >= 1)  # 1 is converted to 1.0 & float comparison approaches are applied

# equality check
print(2.0 == 2.0)  # they're the same value: True

# inequality check
print(2.0 != 2.0)  # again... they're freaking same: False

# check for membership in a range
A, B, C = -2, 0, 8
print(A < B < C)  # which means that B is in between A's & C's values

# which is short form of more compound logical expression
print(A < B and B < C)  # same result

# for the opposite result you do the same
print(A < B > C)

# any other comparison operators can be involved
print(1 == 2 < 3)  # same as: 1 == 2 and 2 < 3; not: False < 3

print(False < 3)  # which would've return True
# it's more likely: False and True; which returns False


# * Division: classic, division with flooring and true division *

# [/]: X / Y

# int / int = int; if there's float: float
print('in Python 2.6: classic division (trunc when dividing int)')

# any division: float
print('in Python 3.0: true division (keeps the floating part)')


# [//]: X // Y
print('was added in Python 2.2: division with flooring (always cuts off the float part)')
# rounds the number down to the nearest and least value
# if any of the operands are float: .0 is tailed to the result


# Flooring and Truncating

# the significance between truncating and flooring is seen on diving negative numbers
# it's easily demonstrated using module [math]
import math

print(math.floor(2.5))  # 2 is nearest least value to 2.5
# that flooring

print(math.floor(-2.5))  # negative -2.5's nearest least value is -3 not -2; -2 > -3
# flooring negative numbers

print(math.trunc(2.5), math.trunc(-2.5))  # that's the difference

# examples with operands

# with int
integer = 5 / 2, 5 / -2
print(integer)

true = 5 // 2, 5 // -2
print(true)

# with float
integer = 5 / 2.0, 5 / -2.0
print(integer)

true = 5 // 2.0, 5 // -2.
print(true)  # result is just float


# but if you need to truncate the result regardless the division type
print(5 / -2)  # keeps the floating part
# -2.5

print(5 // -2)  # rounds the result down
# -3

# [trunc] function from [math] module
print(math.trunc(5 / -2))  # instead rounding; truncating is done


# * Preciseness of Number Presentation *
print(999999999999999999999999999999 + 1)  # Python 3.0
print(1000000000000000000000000000000)  # Python 2.6

print(2 ** 200)
# ? national budget in cents ?

# since interpretator undertakes extra steps presenting high-preciseness nums
# operations speed can noticable decrease
# but when working with hairy numbers speed is on Plan B


# * Complex Numbers *


# complex numbers are also listed in basic numeric types
# in program code imag.part has suffix J; that's how you distinguish them
# if real part is not 0, complex number is written as addition of both parts: 2 + -3j
# real part: 2; imag.part: -3

# * some actions upon complex nums *
print(1j * 1J)
# (-1+0j)

print(2 + 1j * 3)  # (2+3j)

# distributive multiplication
print((2 + 1j) * 3)  # (6+3j)

# there's a module math adapted for complex numbers
# import cmath
# print(help(cmath))


# * Hexadecimal, octal adn binary *
print(0o1, 0o20, 0o377)  # octal literals
# 1, 16, 255

print(0x01, 0x10, 0xFF)  # hex literals
# 1, 16, 255

print(0b1, 0b10000, 0b11111111)
# 1, 16, 255

# by default interpretator outputs numbers as decimals
# ? but there are function that help you convert decimals to other num sys ?
print(oct(64), hex(64), bin(64))

# ? and reversed converter that converts to integers based on num system given ?
print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))  # 64's


# ! eval() --> interprets the string in the arguments as programm code !
print(eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000'))
print(eval('[e for e in range(0, 8)]'), 'octal system')  # nicest function :)


# lastly, int's can be converted to octal, hex and bin using string formatters
print('{0:o}, {1:x}, {2:b}'.format(255, 255, 255))

print('%o, %x, %X' % (8, 16, 255))

X = 0xFFFFFFFFFFFFFFFFFFFFF
print(X, oct(X), bin(X), sep='\n')


# * Binary Operations *

# [<<]: shifting bytes left
x = 1
print(x << 9)  # 512
# shifted x 9 bites left

print(x | 2)  # binary OR
# 3

print(x & 0)  # binary AND
# 0

# ? 3.1 gave us a method .bit_length which returns amount of bytes for num to be bin ?
x = 99
print(bin(x), x.bit_length())  # ice cold
# 0b1100011 7

print(bin(256), (256).bit_length())
# 0b100000000 9


# * Other Built-In Tools *

import math
print(math.pi, math.e)  # well-known constants
# 3.1415926535897931, 2.7182818284590451

print(math.sin(2 * math.pi / 180))  # sin, tan, cos
# 0.034899496702500969

print(math.sqrt(121), math.sqrt(2))  # square root
# 11.0, 1.4142135623730951

print(pow(2, 4), 8 ** 2)  # exponentiation
# 16, 64

print(abs(-42.0), sum((1, 2, 3, 4)))  # absolute value, summary
# 42.0, 10

print(min(3, -1, 0, 2), max(99, 101, 8**3, 67))  # minimum and maximum
# -1, 512

print(math.floor(2.567), math.floor(-2.567))  # flooring pos and neg nums
# 2, -3

print(math.trunc(2.567), math.trunc(-2.567))  # truncating
# 2, -2

print(int(2.567), int(-2.567))  # converting to int, truncating
# 2, -2

print(round(2.567), round(2.467), round(2.567, 2))  # rouding
# 3, 2, 2.57

print('%.1f' % 2.567, '{0:.2f}'.format(2.567))  # rounding when displaying
# 2.6, 2.57

# ? square root can also be calculated by powering num to 0.5 ?
print(math.sqrt(144), 144 ** .5)  # same result
print(math.pow(144, .5))  # same trick different performer

# modules like math should be imported; modules: external components
# built-in functions're situated in PATH name environment (module [builtin])


# module random can help generating random float numbers from 0 to 1
import random
# or any other number from a given range, implement a random choice from a seq. of obj's

# float
rand_float = random.random()
print(rand_float)

rand_float = random.random()
print(rand_float)


# int
random_num = random.randint(1, 10)
print(random_num)

song = random.choice(['Candles', 'Fast', 'Flaws and Sins', 'Lucid Dreams', 'AGATS'])
print(song)



# ! Other Numeric Types !


# * Numbers with Fixed Preciseness: Decimal *
# ? fixed amount of numbers after floating point, nums after point can be managed ?

print(repr(0.1 + 0.1 + 0.1 - 0.3))  # result shoulda been 0; limited memory problems

# friendly output doesn't help much; limited preciseness level of float nums
print(0.1 + 0.1 + 0.1 - 0.3)


# but numbers with fixed preciseness do the right trick
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))  # 0.0

# or... 
right_trick = repr(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
print(right_trick)  # Decimal('0.0')

# even if you make it difficult by processing different preciseness level nums
trick = repr(Decimal('0.1') + Decimal('0.10') + Decimal('0.1') - Decimal('0.30'))
print(trick)  # 0.00 <-- python picks up the greatest preciseness that suits the case


# Global Preciseness Setup
import decimal
print(decimal.Decimal(1) / Decimal(7))

# let's decrease the amount of hairyness
# decimal.getcontext().prec = 4
print(Decimal(1) / Decimal(7))  # only 4 symbosl after the point


# this feature is especially comfortable within finance apps where cents are 2 numbers
# shortly speaking this is an analog for rounding and formatting numeric values
print(repr(1999 + 1.33))

# decimal.getcontext().prec = 2
pay = decimal.Decimal(str(1999 + 1.33))
print(pay)

# Object Context Manager of a Decimal class

# ? temporary change of preciseness with context manager ?
# after leaving boundaries of an instruction, value goes back to default

# before
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

# after
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))


# * Rational Numbers *

# to avoid inaccuracy in calculations and other limits Fraction class was created
# like Decimal, you can manage precision, since Fraction uses rounding policy
from fractions import Fraction  # ? just like Decimal it has to be imported

x = Fraction(1, 3)
print(x)

y = Fraction(4, 6)
print(y)

# after being created Fraction can be used in math operations
print(x + y)  # niiice :D

# precise result: numerator & denominator
print(x - y, y - x - Fraction(1, 3))  # niiice :))

# ? more pie pieces ?
print(x * y)

# ? rationals can be created outta strings containing float nums ?
pie_left = .25
print(f'Pie Left: {Fraction(str(pie_left))}')  # str() <-- is not strictly necessary

iq_ratio = 1.25
print(f'IQ Points: {Fraction(iq_ratio)}')

sex_group = Fraction('.25') + Fraction(1.25)
print(f'Oops... Someone is ODD: {sex_group}')


# Precision
a = 1 / 3.0  # precision is limited by our machine capabilities
print(a)

b = 4 / 6.0  # precision can be lost in the calculation process
print(b)

# looks normal sometimes
print(a + b)  # 1.0

# gets more hairy & hairy
print(a - b)  # -0.3333333333333333

# so Fractions, huh?
print(a * b)

# ! let's trade: precision for performance speed. deal? !

# shoulda get 0
print(0.1 + 0.1 + 0.1 - 0.3)  # 5.551115123125783e-17  <-- wat u get insted

res = Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10)
print(res, repr(res))

res = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print(res, repr(res))


# moreover, you get more readable and clearer results with Fraction and Decimal
print(repr(1 / 3))  # what you get

# let's fix this
print(Fraction(1, 3), repr(Fraction(1, 3)))

# or maybe Decimal?
with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(Decimal(1) / Decimal(3), repr(Decimal(1) / Decimal(3)))


# e.g
print((1 / 3) + (6 / 12))

# thing is simplified automatically
print(Fraction(6, 12))  # 1/2

# now action
print(Fraction(1, 3) + Fraction(6, 12))

# with Decimal
with decimal.localcontext() as ctx:
	ctx.prec = 2
	print(Decimal(str(1/3)) + Decimal(str(6/12)))


# ? for converting float to Fraction; method as_integer_ratio() was added to float ?
print((2.5).as_integer_ratio())

f = 2.5
z = Fraction(*f.as_integer_ratio())
print(z)  # 5/2  niiice :D

x = Fraction(1, 3)
print(x + z)  # common denominator is 6: so 5/2 * 3 & 1/3 * 2 = 15/6 + 2/6

print(float(x))  # converting Fraction to float

# less hairy
print(float(z))

# hairy again... :(
print(float(x + z), 17/6)  # reasonable


# ? plus from_float() method on the Fraction class ?
print(Fraction.from_float(1.75))  # 4 .25 make up 1; 3 make up .75 | 1.75 niice :D

print(Fraction(*(1.75).as_integer_ratio()))  # same result, longer code


# Mixing Up Types

# Fraction + int --> Fraction
x = Fraction(1, 3)
print(x + 2)

# Fraction + float --> float
print(x + 2.0, x + (4./3))

# Fraction + Fraction --> Fraction
print(x + Fraction(4, 3))  # so fucking beautiful thing

# ? in case if Fraction starts losing precision use .limit_denominator() method ?
