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


# Formats of Displaying Numbers

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