# -------------------------------
### VARIABLES

Variables are some kind of container that stores a value that can change over time

# 1 Example 
guess = 10

>>> 10

- means that 10 is inside guess 


# 2 Example : Function to guess
def get_guess()
	guess = 10
	return guess

print (get_guess())

>>> 10



# 3 Example : Whatever user types will be stored in guess
def get_guess()
	guess = input ("Enter a guess: ")
	return guess

print (get_guess())

>>> 10


# 4 Example : Get guess from user and print
def get_guess()
	guess = input ("Enter a guess: ")
	return guess

def main():
	guess = get_guess()
	print (guess)

main()

>>> 10



# 5 Example : Get guess from user and compares with the guess
def get_guess()
	guess = input ("Enter a guess: ")
	return guess

def main():
	guess = get_guess()
	if guess == 50:
		print("Correct!")
	else:
		print("Incorrect!")


main()

> 50
>>> Incorrect!

Its happens because they are comparing numer with string 
50 is different to "50"
50 == "50" ? Nop




# 6 Example : Correction Get guess from user and compares with the guess
def get_guess()
	guess = int(input("Enter a guess: "))
	return guess

def main():
	guess = get_guess()
	if guess == 50:
		print("Correct!")
	else:
		print("Incorrect!")


main()

> 50
>>> Correct!

Tip:
Depending of the context you may need string or numbers so be attention of eveything
