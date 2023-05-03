import math  # to import a module write import + mdname 

# Math Functions

# abs - making absolute numbers outta negatives
a = abs(-5.6)  # first we save result in a var
print(a)  # then we print it out


# min() - picks out minimum value outta list
b = min(3, 5, -2, 5, 657, 8)
print(b)


# max - min's opposite
print(max(-2, -119, 0, -0.1))


# pow - power raise
print(pow(8, 2), pow(121, 0.5))


# round - cutting the decimal part yielding num to the closes
print(round(1.5), round(10.5))

# round has 2nd optional argument
print(round(3.1415, 2))

# if it is negative rounding applies on the left side of a dot
print(round(421.54561, -1))  # rouding tens


# Nested Calls
nest = max(1.9, abs(min(12, -2, 4))+.3, 2.2, -3)
print(nest)


# Module Math

# function: ceil()  | rounding to greatest int
print(math.ceil(5.3))  # 6
print(math.ceil(-4.9))  # -4  (greater than -5)


# func: floor()  |  rounding to the leist int
print(math.floor(5.99))  # 5
print(math.floor(-3.3))  # -4 (less than -3)


# func: factorial()  |  calculating the factorial 
print(math.factorial(6))  # 720

# func: trunc()  |  analog of int(truncificate)
print(math.trunc(5.125862189561))


# func: sqrt()  |  square root
print(math.sqrt(81))


# constants
print(math.pi)  # pi
