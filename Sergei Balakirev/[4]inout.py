print(1)

a = -24.8
print(a)

a -= .2
print(a * 2 // 5)

# flags: sep=seperating_symbol, end=ending_symbol

# sep=" "
a = 'flagman'
b = False
c = 1.4

print(a, c, b, sep=' | ')


# end='\n'
print('hello', end=' ')  # default \n | newline
print('world')
# now it's: hello world


# formatting
x = 5.76
y = -8

print('Ur Coordinates: x = ', x, "; y = ", y, sep='')
# not that convenient, innit?


# f-strings
print(f"Ur Coordinates: x = {x}; y = {y}")
# {} is placeholder for u to fill in


# function: input()
# a = input()  # input returns always str
# a = int(a)  # converts the str containing numbers into num
a = int(input())
b = abs(a)
print(b)

# if anything non-numeric will be in the string int won't help
a = float(input('Length: '))
b = float(input('Width: '))  # input can receive a hint arg
print(f'Perimeter: {(a + b) * 2}')


# key-in through space

# rectangles triangle
a, b = map(float, input('Rectangle Sides: ').split())
print(f'Perimeter: {2 * (a + b)}')


# triangles perimeter
a, b, c = map(float, input('Triangle Sides: ').split())
print(f'Perimeter: {a + b + c}')
