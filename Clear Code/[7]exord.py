# first line
print('first line')

# second line
print('second line')
# code. nothing. another line of code.
# python ignores empty lines.

# so now organization of your code is fairly simple
# whitespace within a line is also ignored

print(      'this       whitespace is considered'      )
# space in between parts of code is ignored


# but indentation of an entire line
# ____print('bitch, pls...')
# IndentationError

# you can create multiple line of code in one line
# what you see is a physical line; whatever in one line
# what python sees is a logical line

# print('first') print('second line')  # python can't execute two logical
# simultaneously

# semicolon
a = 10; b = 20  # gluing 2 logical lines into 1 physical line
print(a); print(b)

a = 1 + 2 + 3 + 4 \
    + 5 + 6 + 7  # breaking one logical line into 2 physical lines
print(a)
