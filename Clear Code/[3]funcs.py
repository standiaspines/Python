# Functions

# brackets are used to call functions
print()

print('test')  # it prints the word so we can see it

len('another word')  # we don't see anything from it
# when code is launched

word = 'another word'
print(len(word))  # cuz displaying is not the part of len's job
# 12 characters in a phrase; spaces are counted too

word_length = len('Japan')
print(word_length)  # clearer example

print(abs(-50))  # absolute of negative -50 is 50


# adding another argument
print(1, 2, 'three')  # print accepts unlimited number of arg's

# depends on a func. tho
# abs(-30, -14)  # abs accepts only 1 arg.


# max() --> returns the biggest in a iterable
print(max(19, -1, 0, 24, 5))  # put out the biggest number
# which is 24

# so with that info: pretty easy to figure out what [min] does
print(min(19, -1, 0, 24, 5))
