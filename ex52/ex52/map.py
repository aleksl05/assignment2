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
		


Bedroom = Room("Bedroom",
"""
This is a very easy game where the whole point is to
look for letters in each room. You should be able to pick them
up and store them in your notebook. To win the game you have
to get all the letters and guessing the password by mixing up the
letters in the correct way.
""", ["p","y","t","h","o","n"])


Hall = Room("Hall",
"""
This is a very easy game where the whole point is to
look for letters in each room. You should be able to pick them
up and store them in your notebook. To win the game you have
to get all the letters and guessing the password by mixing up the
letters in the correct way.
""", "t")


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


the_end_winner = Room("Livingroom",
"""
This is a very easy game where the whole point is to
look for letters in each room. You should be able to pick them
up and store them in your notebook. To win the game you have
to get all the letters and guessing the password by mixing up the
letters in the correct way.
""","o")


Livingroom = Room("Livingroom",
"""
This is a very easy game where the whole point is to
look for letters in each room. You should be able to pick them
up and store them in your notebook. To win the game you have
to get all the letters and guessing the password by mixing up the
letters in the correct way.
""", "y"
)
Entrance = Room("Entrance",
"""
This is a very easy game where the whole point is to
look for letters in each room. You should be able to pick them
up and store them in your notebook. To win the game you have
to get all the letters and guessing the password by mixing up the
letters in the correct way.
""", ""
)
Victory = Room("Victory",
"""
You have done it, you have won in this unbelievable boring and
simple game. Welcome back later if you want to try again
""", ""
)
Entrance.add_paths({
	'hall' : Hall,
	'*' : Victory
})

Livingroom.add_paths({
	'hall' : Hall,
	'*' : Victory
})

Kitchen.add_paths({
    'hall': Hall,
	'*' : Victory
})

lost = Room("Lost", "You lost because you failed to many times! Write 'restart' to try again.", [])

Bathroom.add_paths({
    'hall': Hall,
    'bedroom': Bedroom,
	'*' : Victory

})

Hall.add_paths({
    'bathroom': Bathroom,
    'bedroom': Bedroom,
		'kitchen' : Kitchen,
		'livingroom' : Livingroom,
		'entrance' : Entrance,
		'*' : Victory
})

Bedroom.add_paths({
    'bathroom': Bathroom,
	'hall' : Hall,
	'*' : Victory
})


START = Bedroom