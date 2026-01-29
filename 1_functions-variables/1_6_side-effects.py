# -------------------------------
### SIDE EFFECTS


#Example 1
emotion = "v.v"

def main():
	say("Is anyone there?")
	say ("Oh, hi!")

def say(phrase):
	print(phrase + " " + emoticon)


main()

>>> Is anyone there ? v.v





#Example 2
emotion = "v.v"

def main():
	say("Is anyone there?")
	emoticon = ":D"
	say ("Oh, hi!")

def say(phrase):
	print(phrase + " " + emoticon)


main()

>>> Is anyone there ? v.v
>>> Oh, hi! v.v




#Example 3: Using Global variable
emotion = "v.v"

def main():
	global emoticon 
	say("Is anyone there?")
	emoticon = ":D"
	say ("Oh, hi!")

def say(phrase):
	print(phrase + " " + emoticon)


main()

>>> Is anyone there ? v.v
>>> Oh, hi! :D


