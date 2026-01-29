# -------------------------------
### RETURN VALUES

# Example 1
def greet(input):
	if "hello" in input:
		print("hello, there")
	else:
		print("I'm not sure what you mean")


greet("hello, computer")

>>> hello, there





#Example 2 : Using return
def greet(input):
	if "hello" in input:
		return "hello, there"
	else:
		return "I'm not sure what you mean"


greet("hello, computer")

>>> 
(NOTHING HAPPENS)





#Example 3 : Using return storing values and print it
def greet(input):
	if "hello" in input:
		return "hello, there"
	else:
		return "I'm not sure what you mean"


greeting = greet("hello, computer")
print(greeting)

>>> hello, there





#Example 4 : Other input
def greet(input):
	if "hello" in input:
		return "hello, there"
	else:
		return "I'm not sure what you mean"


greeting = greet("how's the weather")
print(greeting)

>>> I'm not sure what you mean


Tip: 
Using return you can modify the return values after receiving and them print  as you want in your code




#Example 4 : Modifying greeting
def greet(input):
	if "hello" in input:
		return "hello, there"
	else:
		return "I'm not sure what you mean"


greeting = greet("how's the weather")
print("Hm," + greeting)

>>> Hum, hello, there

Return - value of return value is that it allows us to modify things in the code and use the output in some fucntion later on

