ecture 3 - Loops


code cat.py

# Example 1: repeating 3 times meow
print("meow")
print("meow")
print("meow")


----------------------
WHILE

While is one way it will be executing the looping again and again


# Example 2: Using WHILE but attention to infinite looping
i = 3
while i != 0:
	print("meow")



# Example 3: Close the loop

i = 3
while i != 0:
	print("meow")
	i = i - 1


# Example 4: Improving

i = 0
while i < 2:
	print("meow")
	i += 1


Tips:
- SOme dev people like to starts counting by 0




---------------------------
FOR



# Example 1: using for
for i in [0, 1, 2]:
	print("meow")


# Example 2: for i in range

for _ in range(3):
	print("meow")

- use undersdcore to define variable thats will be only used in that scenario in the code


# Example 3: print fucntion using multiplier
print("meow" * 3)

>>>meowmeowmeow

print alltogether


# Example 4: print fucntion using multiplier
print("meow\n" * 3, end "")

>>>meow
>>>meow
>>>meow



--------------------
WHILE TRUE: while something is true it will stay in the loop

# Example 5: using WHILE TRUE

while True:
	n = int(input("What's n? "))
	if n > 0:
		break

for _ in range(n):
	print("meow")




# Example 6: using Functions

def main():
	meow(3)

def meow(n):
	for _ in range (3):
		print("meow")

main()





# Example 6: More Functions


def main():
	number = get_number()
	meow(number)

def get number():
	while True:
		n = int(input("What's n? "))
		if > 0:
			break
	return n

def meow(n):
	for _ in range (n):
		print("meow")

main()




--------------------------------

code hogwarts.py

# Example 1: Print each item list
students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])




# Example 2: Print any item of list without kning how long is

students = ["Hermione", "Harry", "Ron"]

for student in students:
	print(student)


Tip: You dont need necessary to declare any variable before you use, in python it dos itself automatically


# Example 3: You can print rank of each on the list together

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
	print(i+1, students[i]) # using +1 because starts with 0



---------------------------------
DIC - dictionary: index and value


# Example 1: Associating 2 lists

students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

- This way is easy to associate, buy if could have many ? in a messy way ? How we would associate ? using dictionary


# Example 2: Using dic

students = {
	"Hermione": "Gryffindor",
	"Harry": "Gryffindor",
	"Ron": "Gryffindor", 
	"Draco": "Slytherin",
	}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

>>>Gryffindor
>>>Gryffindor
>>>Gryffindor
>>>Slytherin




# Example 3:

students = {
	"Hermione": "Gryffindor",
	"Harry": "Gryffindor",
	"Ron": "Gryffindor", 
	"Draco": "Slytherin",
	}

for student in students:
	print(student)

>>>Hermione
>>>Harry
>>>Ron
>>>Draco


- Tip: by dafult in python they print the key value of each one






# Example 4: Print both name and school together

students = {
	"Hermione": "Gryffindor",
	"Harry": "Gryffindor",
	"Ron": "Gryffindor", 
	"Draco": "Slytherin",
	}

for student in students:
	print(student, students[i], sep=", ")




# Example 5: List with Dict

students = [
	{"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
	{"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
	{"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
	{"name": "Draco", "house": "Slytherin", "patronus": None} # None when is empty
]

for student in students:
	print(student["name"], student["house"], student["patronus"], sep=", ") # can print each data you want




--------------------------------------

code mario.py

# Example 1:

def main():
	print_column(3)


def print_column(height):
	print("#\n" * height, end="")

main()






# Example 2
def main():
	print_row(4)


def print_row(width):
	print("?" * width)

main()

 





 # Example 3

def main():
	print_square(30)


def print_square(size):
	
	# For each row in square
	for i in range(size):

		# For each brick in row
		for j in range(size):

			# Print brick
			print("#", end="")
		print()

main()






# Example 4:


def main():
	print_square(30)


def print_square(size):
		for i in range(size):
			print("#" * size)

main()








# Example 5:


def main():
	print_square(30)


def print_square(size):
		for i in range(size):
			print_row(size)


def print_row(width):
	print("#" * width)


main()
