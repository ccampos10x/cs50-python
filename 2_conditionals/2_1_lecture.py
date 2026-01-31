2# Conditionais Lecture

Hability to ask questions to if this make that or that

symbols / meaning
> greater than
>= greater than or equal to
< less than
<= less than or equal to
== equal (compare)
!= not equal to




IF

code compare.py

x = int(input("What's x? "))
y = int(input("What's y? "))


if x < y:
	print("x is less than y")
if x > y:
	print("x is greater than y")
if x == y:
	print("x is equal to y")


>1
>2
>>> x is less than y

>2
>1
>>> x is greater than y

>1
>1
>x is equal to y



Tips:
- when use if the results will be bollean - true or false
- everything in the indentation of the if is inside it (attention)
- it works but is not properlly desineg, because is using too many IFs


-----------------------------
ELIF

x = int(input("What's x? "))
y = int(input("What's y? "))


if x < y:
	print("x is less than y")
elif x > y:
	print("x is greater than y")
elif x == y:
	print("x is equal to y")


- Will get the same results, looks like the same but its better because is using less IFs and this mean that 
- Asking less in the code your code become more faster then before, its seems simple here and cant notice the difference but in big projects this worth value




-------------------------------
ELSE


ELIF

x = int(input("What's x? "))
y = int(input("What's y? "))


if x < y:
	print("x is less than y")
elif x > y:
	print("x is greater than y")
else
	print("x is equal to y")


Same results even better, because else dont wask anything is just the result of the IFs before using logic flow



---------------------------------------
OR

x = int(input("What's x? "))
y = int(input("What's y? "))

if x > y or x > y:
	print("x is NOT equal to y")
else:
	print("x is equal to y")


This example we can use OR in the same IF to ask two questions or more in our logic - its not the better but its a possibility


#Example using !=
x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
	print("x is NOT equal to y")
else:
	print("x is equal to y")




-------------------------------------------------

grade.py


# Example 1
score = int(input("Score: "))

if score >= 90 and score <=100:
	print("Grade A")
elif score >= 80 and score <90:
	print("Grade B")
elif score >= 70 and score < 80:
	print("Grade C")
elif score >=60 and score < 70:
	print("Grade D")
else
	print("Grade F")


>100
>>> Grade A
>91
>>> Grade A
> 89 
>>> Grade B
> 71
>>> Grade C
> 61
>>> Grade D
>0
>>> Grade F






# Example 2: Same thing with compreing inverting

score = int(input("Score: "))

if 90 >= score and score <=100:
	print("Grade A")
elif 80 >= score and score <90:
	print("Grade B")
elif 70 >= score and score < 80:
	print("Grade C")
elif 60 >= score and score < 70:
	print("Grade D")
else
	print("Grade F")


>>> same results


# Example 3: Simplest way of the last version

score = int(input("Score: "))

if 90 >= score <=100:
	print("Grade A")
elif 80 >= score <90:
	print("Grade B")
elif 70 >= score < 80:
	print("Grade C")
elif 60 >= score < 70:
	print("Grade D")
else
	print("Grade F")


>>>sale results





# Example 4: Reduced version 
score = int(input("Score: "))

if score >= 90:
	print("Grade A")
elif score >= 80:
	print("Grade B")
elif score >= 70:
	print("Grade C")
elif score >=60:
	print("Grade D")
else
	print("Grade F")






# Example 5: TEsting Revert ELIFS to IF
score = int(input("Score: "))

if score >= 90:
	print("Grade A")
if score >= 80:
	print("Grade B")
if score >= 70:
	print("Grade C")
if score >=60:
	print("Grade D")
else
	print("Grade F")


>91
>>>Grade A
>>>Grade B
>>>Grade C
>>>Grade D
>>>Grade F


- If yoy uses only IFs the code you compare in every section if its true and thats why they you output many results as not expected



----------------------------

code parity.py


operator / meaning
+ add
- minus
* multiple
/ divide
% module operator (the rest of division)


# Example 1: 
x = int(input("What's x? "))

if x % 2 == 0:
	print("Even")
else:
	print("Odd")




# Example 2: Function of parity

def main():
	x = int(input("What's is x? "))
	if is_even():
		print("Even")
	else:
		print("Odd")

def is_even(n):
	if n % 2 == 0:
		return True
	else:
		return False





# Example 3: Pythonic way

def main():
	x = int(input("What's is x? "))
	if is_even():
		print("Even")
	else:
		print("Odd")

def is_even(n):
	return True if n % 2 == 0 else False

Pythonic term used in the community to do ellegant thinds in code



# Example 4: Pythonic v2

def main():
	x = int(input("What's is x? "))
	if is_even():
		print("Even")
	else:
		print("Odd")

def is_even(n):
	return n % 2 == 0


Just simple in is_even because the return is bool and it mean that is always give True or False



-------------------------
house.py

# Example 1:

name = input("What's your name? ")

if name == "Harry":
	print("Gyffindor")
elif name == "Hermione":
	print("Gyffindor")
elif name == "Ron":
	print("Gyffindor")
elif name == "Draco":
	print("Slytherin")
else:
	print("Who? ")





# Example 2: Improvments using OR

name = input("What's your name? ")

if name == "Harry" or "Hermione" or "Ron":
	print("Gyffindor")
elif name == "Draco":
	print("Slytherin")
else:
	print("Who? ")



# Example 3: Using MATCH

name = input("What's your name? ")

match name:
	case "Harry":
		print("Gyffindor")
	case "Hermione":
		print("Gyffindor")
	case "Ron":
		print("Gyffindor")
	case "Draco":
		print("Slytherin")
	case _: 				#whatever is not handle
		print("Who?")



# Example 4: Using |

name = input("What's your name? ")

match name:
	case "Harry" | "Hermione" | "Ron":
		print("Gyffindor")
	case "Draco":
		print("Slytherin")
	case _: 				#whatever is not handle
		print("Who?")


