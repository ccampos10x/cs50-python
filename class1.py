# ---------------------------
# Say hello to user
print("hello, world")

VS Code

input ("Whats your name ?")
print("hello, David")


# Store input to a variable
name = input ("Whats your name ?")
print("hello, David")

# 
name = input ("Whats your name ?")
print("hello,")
print(name)


pseudocode using #comments to think in parts of the programming
Example:

# Ask user for their name
name = input ("Whats your name ?")

# Say hello to user
print("hello,")
print(name)


# Ok, but missing space after the question and another one misssing after the hello
name = input ("Whats your name ?")
print("hello," + name)


# Correct version
name = input ("Whats your name ? ")
print("hello, " + name)

# Different way with same result - concatetening left with right sides
name = input ("Whats your name ? ")
print("hello,", name)


# https://docs.python.org/3.15/library/functions.html#print documentation of print function
# print(*objects, sep=' ', end='\n', file=None, flush=False)
name = input ("Whats your name ? ")
print("hello, ")
print(name)




# Explaning with details PRINT
# print(*objects, sep=' ', end='\n', file=None, flush=False)
print - function name
() - arguments inside the function - whats you can pass
*objects - means can be using for multiple objects inside
sep=' ' - separator: means they will be separator with a single space
end='\n' - ends with new line (\n) - cursos will temrinate with new line in the end




# Version with end="" - will not mover mouse cursor new line
name = input ("Whats your name ? ")
print("hello, ", end="")
print(name)

# Testing anything in sep=""
name = input ("Whats your name ? ")
print("hello, ", sep="???")
print(name)




'' Single is Python default
"" You can use both

# Not work - Invalid syntax 
print("hello, "friend"")

# Correct - can use mixed quotes 
print('hello, "friend"')

# backslashes \ to refer a quote text
print("hello, \"friend"\")



# f{} format string
name = input ("Whats your name ? ")
print(f"hello, {name}")


# Remove whitespace from str
name = input ("Whats your name ? ")
name = name.strip()
print(f"hello, {name}")


# Capitalize users name only first letter
name = input ("Whats your name ? ")
name = name.strip()
name = name.capitalize()
print(f"hello, {name}")



# Capitalize users name every word
name = input ("Whats your name ? ")
name = name.strip()
name = name.title()
print(f"hello, {name}")


# Mixing functions
name = input ("Whats your name ? ")
name = name.strip().title()
print(f"hello, {name}")

# You can use them in diffrent way 
name = input ("Whats your name ? ").strip().title()
print(f"hello, {name}")



# Split user's name into first and last name
name = input ("Whats your name ? ").strip().title()
first, last = name.split
print(f"hello, {first}")


# --------------------------
int - INTEGER numbers
+
-
*
/
% module operator - rest of dividion


Interactive Mode
Python interpretor - runs code imediatly
>>>

Create a new file 
code namedoc.py 




# 1 Example
x = 1 
y = 2

z = x + y
print (z)

>>> result 3


# 2 Example: user can digit x and y
x = input("What's x? ")
y = input("What's y? ")

z = x + y
print (z)

>>> result 12
Because it is concateneting strings one with another - right side with left side it happens when you input anything in your pc, cellphone etc.. will be text string, even it seems like number, but when it comes from keyboard it is a string


# 3 Example: user can digit x and y and it converts to INT
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)
print (z)

>>> result 3


Tips:
- when you are typing "python calc.." you can PRESS TAB to the terminal completes for you
- UP and DOWN you can go to your typing history


# 4 Example: Its not cool to creat z and not use anymore so reduce everything to appear clean
x = int(input("What's x? "))
y = int(input("What's y? "))

print (x + y)

>>> result 3

Tip:
- Priorize redability to understand the code
- Keep it simple



# 5 Example: Cleaner in one line of code
print (int(input("What's x? "))+ int(input("What's y? ")))

>>> result 3

Tip: Is nicer but its a little complicated to get the idea



# ---------------
float - Decimals numbers

# 1 Example float: you can type 1.2 or 3.4 for examples
x = float(input("What's x? "))
y = float(input("What's y? "))

print (x + y)

>>> result 4.6


# Documentation: round(number[, ndigits])


# 2 Example float: round the numbers
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print (z)

>>> result 5


# 3 Example float: format z to get `,` in th result typing 999 + 1
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print (f"{z:,}")

>>> 1,000


# 4 Example float: Division typed 2 / 3
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print (z)

>>> 0.66666666666666



# 5 Example float: Division typed 2 / 3 using round
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2)

print (z)

>>> 0.67


# 5 Example float: Division typed 2 / 3 using f string
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print (f"{z:.2f}")

>>> 0.67



# ---------------------
def - FUNCTIONS define


# 1 Example : Using def in hello
def hello():
	print ("hello")

name = input("What's your name? ")
hello ()
print (name)

>>> hello
>>> David


# 2 Example : def hello(to)
def hello(to):
	print ("hello,", to)

name = input("What's your name? ")
hello (name)

>>> hello, David


# 3 Example : def hello(to="world") to avoid def is not called without parameter
def hello(to="world"):
	print ("hello,", to)

hello()
name = input("What's your name? ")
hello (name)

>>> hello, world
>>> hello, David


# 4 Example : syntax error because def must be in the beginnig
hello()
name = input("What's your name? ")
hello (name)

def hello(to="world"):
	print ("hello,", to)

>>> syntax error


Tip:
def functions MUST BE in the begining of the code because it has to exist before you use them


# 5 Example : only defining functions without calling them
def main():
	name = input("What's your name? ")
	hello (name)

def hello(to="world"):
	print ("hello,", to)


>>> NOTHING HAPPENS



# 6 Example : calling them
def main():
	name = input("What's your name? ")
	hello (name)

def hello(to="world"):
	print ("hello,", to)

main()

>>> hello, David



# 7 Example : scope problem
def main():
	name = input("What's your name? ")
	hello ()

def hello(to="world"):
	print ("hello,", name)

main()

>>> NameError: name 'name' is not defined

Tip: If use name variable in a function is has to be only their and not in anywhere else



# 8 Example : Resolving scope problem
def main():
	name = input("What's your name? ")
	hello (name)

def hello(to="world"):
	print ("hello,", to)

main()

>>> hello, David





# 9 Example : DEF Calculator
def main():
	x = int(input(What's x?"))
	print("x squared is", square(x))

main()

>>> NameError: name 'square' is not defined



# 10 Example : Correcting with def square 
def main():
	x = int(input(What's x?"))
	print("x squared is", square(x))

def square(n):
	return n * n

main()

>>> x squared is 9


# 11 Example : Another way
def main():
	x = int(input(What's x?"))
	print("x squared is", square(x))

def square(n):
	return n ** 2

main()

>>> x squared is 9

# 12 Example : Another way with pow
def main():
	x = int(input(What's x?"))
	print("x squared is", square(x))

def square(n):
	return pow(n, 2)

main()

>>> x squared is 9