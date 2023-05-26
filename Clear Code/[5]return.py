# returning values

# any operation returns a value
2 + 2  # returns 4

# funcs & methods return also return values
# .upper() returns uppercase letters of a str

word = 'a word'
returning = abs(len(word) * -10)
print(returning)


test_variable = 'A word'.upper().replace('A', 'X')
# first: statement returned 'A word'
# second: upper returned 'A WORD'
# third: replace returns string with 'A' replaced by 'X'

print(len(test_variable))
# fourth: len counting & returns amount of chars

print(print(len(test_variable)))
# 6; from inner print
# None; from outter that's displaying object returned by inner

None  # it's smth; that means nothing
