# How user runs code?

# Interacitve mode

print("Eaziest way's to run statements in interpretator prompt")
# which is often called an interactive shell

# if python is installed as executable package
# easiest way here is to type: python in cmd of ur OS

print("if python ain't put into PATH u enter full dir to call")
# or u can go to that dir in cmd and call it same way

print('Or else, u can use Shell to call interactive session')
# or... python command line


print('>>> is a prompt invitation')
# in interactive mode ur statements are put into run immediately
# after they're typed out and Enter is pressed.


print('Was an instruction in 2.6, became a function in 3.0')

# since expressions are output automatically u DON'T print

'''
>>> lumberjack = 'okay'
>>> lumberjack
'okay'

>>> 2 ** 8
256

>>> ^Z  # to exit use (Ctrl+Z) that'll put special character
# and after Enter the session is quited
'''


# Where and Why
print('Interactive Shell isn\'t 4 long commands')
# it'll get messy with long ones

# but...
print('U can use it 2 experiment features and tests on files')


# if u hesitate to use any construction of Python
print('Try it on interactive shell and look what happens')


mltp = 'wendy!'*7
# imagine u don't know what this does

'''
>>> 'wendy!'*7
'wendy!wendy!wendy!wendy!wendy!wendy!wendy!'
>>> # it clearly shows u what it does
>>> 'string duplication.'
'string duplication.'
'''

print('When with nums: multiplication - num * num')

print('When with str: multiple concatenation - str + str + str')


# Testing
print('U can import ur own modules and check functionality')
# and all that can be done in the interactive shell

'''
>>> import os
>>> os.getcwd()
'D:\\Code Notes'
'''

# Working with ISH

print('Use only Python commands no OS commands')
# tho they can be reached through os.system module

print('i am no need in there')
# print is useless in ISH

print('Be careful with indentation (4 now)')
# nested and block construcions are ahead

print('There are multi-line commands 4 ISH too')
# but prompt will change from primary(>>>) to nested(...)

print('Multi-line commands are finished with empty line')
# coming soon

print('One command at a time!')
# tough rules of ISH

# code on ISH is not stored in disk memory
# so to run it once more u gotta rewrite it over again


# To be able to re-run the code anytime, save it in files



# Files | Modules | Scripts
# Module - text file containing instructions in Python lang

# module files are called programs
# program - written in advance so it can be run when needed

# example scenario
import sys
print(sys.platform)

print(2 ** 100)
x = 'Blanco'
print(x + 'Lechuza')

# comments - are explaining text that follows the code*

# .py - extension for modules that should be able to be imported


# Running Scripts from CMD

# go to dir where file locateed > python filename.py
# we all cool


# we can apply all functionality of a command shell
print('python filename.py > saveit.txt')
# this will relocate the output flow to text doc

'''
saveit.txt

win32
1267650600228229401496703205376
BlancoLechuza

they won't be displayed on the command output prompt
'''

# and output will be saved in the doc

r'''
Common Mistakes made when running scripts from cmd:

~ Automatic extension assignment
~ Full directory\name should be shown in run, not in import
~ Use print in files, otherwise u'll see no output 
'''

print('U can run modules by just clicking on their icon')
# but as soon as instructions exe'd output window'll be closed
# which is super-fast

print('input function awaits for a in-put from a keyword')
# it freezes the flow untill Enter is pressed 
print('So putting in at the end can kinda solve the problem')
# unless there are errors in the code
# which will just crash the whole thing
print('So unless u debugged the code, it is useless to click')


# Importing and Reloading modules
# a program can refer to other components by importing it
# import loads in the module giving access to its content

# large projects are broken down into several modules
print('There\'s a main high-level module that launches all')
'''
By importing a module u run all possible calls in the module
that's being imported.

For instance, in interactive session u can import a module
that has function calls in it, and by importing it u get output
of all of em.

!- It launches the whole thing only once and imporing it again
will not run the calls repeatedly. -!
'''

print('If u need to re-run it without reopenning the session')
# use reload() func.

# it's not buil-in function so it should be imported in advance

from subfiles import script
from subfiles import script
from subfiles import script

from imp import reload
reload(script)



# from command coppies the function from the module

# reload loads the current version\state of the module
# if it was altered or changed
print('import is limited? then use the cheat - reload')
print('Alert! It only accepts modules that are imported')

# plus the name is embed with brackets
print('import\'s a command')
print('reload\'s a function, that is called')

# so that is why u give a modulename as an argument
# and that's why there's a info line after at the end

# Attributes
print('Module = pack of var names')
# every single name is connected to its object

r'''
code that impors gets access to all names in a higher
level that are defined in a module file

those names are linked to functional components:
classes, funcs, vars and etc.

from outside the access is gained through import\from
'''

from subfiles import myjob
print(myjob.occupation)
# in this case not only occupation can be accessed


from subfiles.myjob import gun
print(gun, 'came with the scope')
# here, i copy exactly only gun so it's not attr but var
# from coppies the name, and var appears in current env

print('whatever way done, the code in the myjob\'s run')

# names can be used in\outside the module
from subfiles import lifestyle
print(lifestyle.c, 'seriously?')


# func: dir
print(dir(lifestyle))
# returns list of available names in a module

# underscored names are always there and defed by inter.
# they carry vital data

module_def = 'they are biggest units of programms'
# programs consist of multiple modules linked by import

print('Modules are independant and duplicate names dont\
 conflict with each other')
# unless u use [from]

# last option to run a file
juice = 999
# exec(open('drink.py').read())
# conflict between names occurs and juice's content alts
