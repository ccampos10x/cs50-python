# -------------------------------
### STRING METHODS


SHOWS = [
	" Avatar: the last airbender",
	"Ben 10",
	"Arthur",
	" Spongebob Squarepants",
	"Phineas and ferb",
	"Kim possible",
	"Jimmy Neutron",
	"the Proud family"
]


How to clean this data with many mistakes ? String methods!


# Example 1: Just print
def main ():
	for show in SHOWS:
		print(show)


main()

>>> Avatar: the last airbender
Ben 10
Arthur
 Spongebob Squarepants
Phineas and ferb
Kim possible
Jimmy Neutron
the Proud family





# Example 2 : capitalize - but only the words without space will work
def main ():
	for show in SHOWS:
		print(show.capitalize())


main()

>>> avatar: the last airbender
Ben 10
Arthur
 spongebob squarepants
Phineas and ferb
Kim possible
Jimmy neutron
The proud family




# Example 3 : title
def main ():
	for show in SHOWS:
		print(show.title())


main()

>>> Avatar: The Last Airbender
Ben 10
Arthur
 Spongebob Squarepants
Phineas And Ferb
Kim Possible
Jimmy Neutron
The Proud Family







# Example 4 : removing spaces with STRIP
def main ():
	for show in SHOWS:
		print(show.strip())


main()

>>>Avatar: the last airbender
Ben 10
Arthur
Spongebob Squarepants
Phineas and ferb
Kim possible
Jimmy Neutron
the Proud family








# Example 5 : Mixing them
def main ():
	for show in SHOWS:
		print(show.strip().title())


main()

>>>Avatar: The Last Airbender
Ben 10
Arthur
Spongebob Squarepants
Phineas And Ferb
Kim Possible
Jimmy Neutron
The Proud Family




# Example 6 : Working with NEW LIST
def main ():
	cleaned_shows = []
	for show in SHOWS:
		cleaned_shows.append(show.strip().title())
	print (cleaned_shows)

main()

>>>['Avatar: The Last Airbender', 'Ben 10', 'Arthur', 'Spongebob Squarepants', 'Phineas And Ferb', 'Kim Possible', 'Jimmy Neutron', 'The Proud Family']







# Example 7 : Using Join in the new list
def main ():
	cleaned_shows = []
	for show in SHOWS:
		cleaned_shows.append(show.strip().title())
	print(' '.join(cleaned_shows))

main()

>>>Avatar: The Last Airbender Ben 10 Arthur Spongebob Squarepants Phineas And Ferb Kim Possible Jimmy Neutron The Proud 
Family



# Example 8 : Using Join in the new list
def main ():
	cleaned_shows = []
	for show in SHOWS:
		cleaned_shows.append(show.strip().title())
	print(', '.join(cleaned_shows))

main()

>>>Avatar: The Last Airbender, Ben 10, Arthur, Spongebob Squarepants, Phineas And Ferb, Kim Possible, Jimmy Neutron, The Proud Family



Tip:
There are many methods in documentation that can be used