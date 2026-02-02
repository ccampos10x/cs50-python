students = [
	{"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
	{"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
	{"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
	{"name": "Draco", "house": "Slytherin", "patronus": None} # None when is empty
]

for student in students:
	print(student["name"], student["house"], student["patronus"], sep=", ") # can print each data you want


