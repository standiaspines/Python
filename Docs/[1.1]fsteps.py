# First Steps Towards Programming

# fibonacci series

# multiple assignment
cup, glass = 'coffee', 'milk'  # cup-a-coffee & glass-o-milk
# ? 2 vars cup & glass are simultaneously given values ?
print(cup, glass)

cup, glass = glass, cup  # cross swaping values
# now theres milk in a cup & coffee in a glass
print(cup, glass)  # printint in the same order


'''
while is a command that builds a loop and re-runs the code in its body
till the condition, in this case i < 100, returns True, but as soon as i becomes greater
than 100 the loop stops working. 

loops body is indented with tab(s) or spaces, which is python's approach of grouping 
lines of code... 

print <-- writes unlimited amount of arguments it's given to the console, puttin white-
-space in between to make it readable. it also writes a new line after it's done with 
arguments, so that the next output is seperated from the last one.

# ? but it can be changed using end='...' argument ?
'''
i = 2
while i < 100:
    i += i - 1
    print(i)

# oops! too much
