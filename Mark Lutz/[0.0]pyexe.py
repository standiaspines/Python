# Python - not only a Programming Language but a package
# Interpretator - module that executes other programs

# Code --> Interpretator --> CPU

# Interpretator reads components of ur code and exe's them

# Execution:

# Developers Vision
print("Hello Universe!")
print(2 ** 10)

# scenario(program) has 2 instructions that output smth

# 1st prints out a string(text) "Hello Universe!"
# 2nd outputs result of arithmetic equation: 2 powered 10
# it all comes out in output flow (flow)

'''
To create a scenario or a script in Python create a file with

'.py' 

extension. As soon as u done writing ur instructions into the
file, save it and request Python to run it.

It will execute all of the instructions from up-to-down.
Mostly it all happens in the same window where script was run
'''


# Pythons Vision
print('When script is run Python translates it into byte code')
# the text inside script is translated into machinary code

print('Compilation - process of code being translted')

'''
Byte Code - low-level, platform-depending projection of source
code. Interpretator translates the code breaking em down into
groups, it increases the performance speed.

If Python has rights to write it'll create a file with binary
translation down, so that launching the script next time can be
done without it being translated again and much faster.

.pyc - the extension of compiled code files.

Next time u launch the same script it'll run faster, in case if
the sourse code wasn't altered from the last compilation.

If it was - it will be recompiled.
'''

print('.pyc files are rescuers for big programs.')


# PVM - Python Virtual Machine
print("Compiled byte code is delivered to PVM that runs them")

'''
PVM is just a big loop that will run through compiled code and
execute associated operations. It's the part of the interpret.
That's what executes and performs all ur scenarios.
'''

# Process
print('m.py')
print('m.pyc')
print('PVM')


print('PVM runs the code not the CPU')
# the execution by PVM is slower than with microprocessors

print('There\'s no difference between Exe Env and Dev Env')


# Frozen Compilation
print('.pyc and PVM glued together')
# .exe files that hide source code and can be run in any machine

print('py2exe', 'pyinstaller', 'freeze')


# Conclusion
print('Interpretator pack of instruments to run scipts')

print('Source Code is code that u write down into files')

print('Byte Code is translated and compiled version of s.c')

print('PVM is machine that reads & performs byte code')

print('.py -> .pyc -> PVM | freeze .exe')

print()
