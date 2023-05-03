# Interactive Mode
r"""
It's a mode using which u can only work on 1-time session
which clears the whole code history when it's closed.

It's often used while debugging or unit testing new or 
unknown functions, so it leaves no code debris on scripts
"""


# File Mode
"""
Ur code is saved and can be run or altered everytime it's 
opened. Files are called 'scripts' and have '.py' extension

In contrast with console interactive mode, u should use func's
to output the result or wanted objects to a console.
"""

3 + 5
16 / 2
1.6 * 5
# result of those actions is not displayed

print(3 + 5)
print(16 / 2)
print(1.6 * 5)
# function print is used to push messages to console

print(0)  # printing integer number
# integers are whole numbers - int

print(3.1415)  # printing float number
# float number is decimal point number - float

print("wussup")  # printing a string
# string is a text object - str

# Rule #1: command starts with no odd indentation
# Rule #2: commands are written in seperate lines 
# Rule #3: commands are executed from up to down

# functions can be called or mentioned

# mention does nothing
print

# call runs the function
print()  # some functions need nothing (no arguments)
# arguments are written inside brackets

# Course Task:
print("Hello Python!")  # traditional kick-off

print(6 + 7)  # should get 13
