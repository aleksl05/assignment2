#rom-klassen som definerer hvordan rommene skal være og hva som skal beskrives
class Room(object):

	def __init__(self, name, description, letters):
		self.name = name
		self.description = description
		self.paths = {}
		self.output = ""
		self.letter = [letters]
		self.answer = 'python'

	def go(self, direction):
		return self.paths.get(direction, None)

	def add_paths(self, paths):
		self.paths.update(paths)
		
	def add_letters(self, letter):
		self.letter.append(letter)
		
	def show_letter(self):
		return str(self.letter)
		
	
		

def go_to_end():
		Entrance.add_paths({'*' : Victory})
		Livingroom.add_paths({'*' : Victory})
		Kitchen.add_paths({'*' : Victory})
		Bathroom.add_paths({'*' : Victory})
		Hall.add_paths({'*' : Victory})
		Bedroom.add_paths({'*' : Victory})

#I have sadly not written some exciting text here because I was struggeling
#with the code. So its a default text in every room.		
Bedroom = Room("Bedroom",
"""
This is a very easy game where the whole point is to
look for letters in each room. You should be able to pick them
up and store them in your notebook. To win the game you have
to get all the letters and guessing the password by mixing up the
letters in the correct way.
""", "p")

#I have sadly not written some exciting text here because I was struggeling
#with the code. So its a default text in every room.
Hall = Room("Hall",
"""
This is a very easy game where the whole point is to
look for letters in each room. You should be able to pick them
up and store them in your notebook. To win the game you have
to get all the letters and guessing the password by mixing up the
letters in the correct way.
""", "t")

#I have sadly not written some exciting text here because I was struggeling
#with the code. So its a default text in every room.
Bathroom = Room("Bathroom",
"""
This is a very easy game where the whole point is to
look for letters in each room. You should be able to pick them
up and store them in your notebook. To win the game you have
to get all the letters and guessing the password by mixing up the
letters in the correct way.
""", "h")


Kitchen = Room("KKitchen",
"""
This is a very easy game where the whole point is to
look for letters in each room. You should be able to pick them
up and store them in your notebook. To win the game you have
to get all the letters and guessing the password by mixing up the
letters in the correct way.
""","n")

#I have sadly not written some exciting text here because I was struggeling
#with the code. So its a default text in every room.
the_end_winner = Room("Livingroom",
"""
This is a very easy game where the whole point is to
look for letters in each room. You should be able to pick them
up and store them in your notebook. To win the game you have
to get all the letters and guessing the password by mixing up the
letters in the correct way.
""",)

#I have sadly not written some exciting text here because I was struggeling
#with the code. So its a default text in every room.
Livingroom = Room("Livingroom",
"""
This is a very easy game where the whole point is to
look for letters in each room. You should be able to pick them
up and store them in your notebook. To win the game you have
to get all the letters and guessing the password by mixing up the
letters in the correct way.
""", "y"
)
#I have sadly not written some exciting text here because I was struggeling
#with the code. So its a default text in every room.
Entrance = Room("Entrance",
"""
This is a very easy game where the whole point is to
look for letters in each room. You should be able to pick them
up and store them in your notebook. To win the game you have
to get all the letters and guessing the password by mixing up the
letters in the correct way.
""", "o")
Victory = Room("Victory",
"""
You have done it, you have won in this unbelievable boring and
simple game. If you want to do it again for some reason, type "restart"
""", ""
)
Entrance.add_paths({
	'hall' : Hall
})

Livingroom.add_paths({
	'hall' : Hall
})

Kitchen.add_paths({
    'hall': Hall
})

lost = Room("Lost", "You lost because you failed to many times! Write 'restart' to try again.", [])

Bathroom.add_paths({
    'hall': Hall,
    'bedroom': Bedroom
})

Hall.add_paths({
    'bathroom': Bathroom,
    'bedroom': Bedroom,
		'kitchen' : Kitchen,
		'livingroom' : Livingroom,
		'entrance' : Entrance
})

Bedroom.add_paths({
    'bathroom': Bathroom,
	'hall' : Hall
})


START = Bedroom