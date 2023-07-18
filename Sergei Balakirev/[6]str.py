s1 = "Felicia"
s2 = 'Greg'

print(s1)
print(s2)

# s2 = Panda  # ! avoid forgetting quotes ["|'] !
print(s2)  # ? now Panda is perceived as variable

# strings literals created using: # * ['...'] or ["..."]

# * mutli-line strings *
text = '''I just wanna rewind,
I haven't seen you in a long time.
You got me feeling so lonely.
Even when you come though,
I can tell that it isn't you,
So baby bring it in closely.
'''

print(text, repr(text))  # \n is a 'line shift or \n-ew line' character

a = ""  # empty string
print(a) 

a = " "  # not empty: it has whitespace in it
print(a)

s1 = 'Wuba Luba'
s2 = 'Dub Dub'
print(s1 + s2)  # concatenation

res = s1 + ' ' + s2  # if you need a whitespace in between
print(res)


# concatenation works only with strings
# print(s1 + 5)  # ! it leads to an error !


# but if you need number and string gluing together use: str() <-- converter
print(s1 + str(5))  # ? it converts any data type in Python into a string ?


# repetition operator: *
print('ha' * 9)  # ha 9 times is: hahahahahahahahaha
# ? [*] operator when put with strings repeats the given string given amount of times


# len() func.: returns the length of the given string
a = 'hello'
print(len(a))  # 5 symbols in hello


# in: check for sub-string membership
alphabet = 'abcdef'
print('abc' in alphabet, 'xyz' in alphabet)  # checks if main string contains sub-string


# comparison operators with strings
a = 'hello'

# equal: ==
print(a == "Hello")  # they're not equal since second Hello has uppercase letter


# NOT equal: !=
print(a != 'Hello')  # not equal. correct.

# greater: > | >=
print(a >= 'hello', a > 'ikea')  # it's not about comparison of lengths
# it's about symbols' order in ASCII; 'i's index is greater than 'h's


# less: < | <=
print('abc' < a <= 'hello ')  # True since second hello_ has whitespace

# ? uppercase letters' order indexes are less than lower case letters' 

# to check what oreder index certain symbol has: ord()

print(ord('a'), ord('A'))  # different
