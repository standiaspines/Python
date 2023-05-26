# Methods

# are exactly like funcs but connected to an object through [.]

# "a word" + [.] + method_name + brackets + arguments
# "penguin".fly(15meters)  <-- smth like that

word = 'penguin'
print(word.upper())

test = 'A word'
print(test)

test = 'A word'.upper()  # here the changed word is being
# restored(overwritten) over the previous state
print(test)  # so variable contains a new string here

test = 'basketball'
print(test.upper())  # same thing?
# nope.
print(test)  # it's still lower case in a var


# more practical example
username = 'JOhn SmIthXX'  # we want: John Smith
print(username)

username = username.title()
print(username)  # first letters in uppercase

# you can combine methods calling them one after another
username = 'JOhn SmIthXX'.title().strip('X')
# so if title capitalizes the fist letters
# strip removes any wanted characters from the end

print(username)  # nothing changed?
# but why?

# in the original words x's were in a upperacase
# title made them lowercase; but since Python is case-sensitive
# strip's looking for uppercase x's
username = 'JOhn SmIthXX'.title().strip('x')
print(username)


# if you wanna know what methods are available
print(dir(username))  # returns you the list of methods
# that are available to operate with the object

# isalpha: all characters are alphabetical
name = 'John Smith'
print(name.isalpha())  # False; since space is not in alphabet

name = 'JohnSMITH'
print(name.title().isalpha())  # done.

# dir is not that useful as it seems
# cuz it gives you only list of methods
# not the description of their functionality

# help(): the name speaks for itself
# print(help(name.isalpha))  # explanation is here.


# Task:

# replace puppies with kittens in: 'I like puppies'
exercise_string = 'I like puppies'
result = exercise_string.replace('puppies', 'kittens')
print(result)

# replace has a third argument
# that defiens how many times primary_string should be replaced

practice_string = 'I like puppies. Puppies like to play. \
Puppies are energetic'

result = practice_string.lower().replace('puppies', 
'kittens', 2)

print(result.title())  # looks good
