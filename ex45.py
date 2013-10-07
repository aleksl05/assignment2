from sys import exit
from random import randint
from operator import eq
import ex45to


class Scene(object):
	
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)
		
class Engine(object):
	def __init__(self,scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n---------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
			
class finished(Scene):

	def enter(self):
		print "Finished"
		exit(1)
			
class Hall(Scene):

	
	def enter(self):
		self.visited = 0
		self.place = 'hall'
		self.letter = ['p']
	
		print "You are in the %s" %self.place
		print "Your objective in this game is to find different letters"
		print "in all the rooms. Type 'help' to get a list of commands"
		print "You have to be in this room to answer the question"
		print "The question what is the word hidden in all the letters"
		print "laying around in the house"
		
		
		
		action = raw_input("> ")
		
		if action == "letter":
			print self.letter
			return self.place
		elif action == "check notebook":
			ex45to.checkbook()
			return self.place
		elif action == "store letter":
			ex45to.addbook(self.letter)
			return self.place
			print "letter are now stored in your notebook"
		elif action == "kitchen":
			return 'kitchen'
		elif action == "bedroom":
			return 'bedroom'
		elif action == "hall":
			return 'hall'
		elif action == "livingroom":
			return 'livingroom'
		elif action == "bathroom":
			return 'bathroom'
		elif action == "help":
			ex45to.help()
			return self.place
		elif action == "guess":
			ex45to.guessword()
			return self.place
		elif action == "skriv":
			skriv()
		else:
			print "Please choose one of the commands"
			return self.place
		
		
		
			
class Livingroom(Scene):
	
	def enter(self):
		self.place = 'livingroom'
		self.letter = ['o']
	
		print "You are in the %s" %self.place
		print "Check which letters that are in this room"
		
		
		
		
		action = raw_input("> ")
		
		if action == "letter":
			print self.letter
			return self.place
		elif action == "check notebook":
			ex45to.checkbook()
			return self.place
		elif action == "store letter":
			ex45to.addbook(self.letter)
			return self.place
			print "letter are now stored in your notebook"
		elif action == "kitchen":
			return 'kitchen'
		elif action == "bedroom":
			return 'bedroom'
		elif action == "hall":
			return 'hall'
		elif action == "livingroom":
			return 'livingroom'
		elif action == "bathroom":
			return 'bathroom'
		elif action == "help":
			ex45to.help()
			return self.place
		elif action == "guess":
			ex45to.guessword()
			return self.place
		elif action == "skriv":
			skriv()
		else:
			print "Please choose one of the commands"
			return self.place
class Bathroom(Scene):
	
	def enter(self):
		self.letter = ['t']
		self.place = 'bathroom'
	
		print "You are in the %s" %self.place

		
		action = raw_input("> ")
		
		if action == "letter":
			print self.letter
			return self.place
		elif action == "check notebook":
			ex45to.checkbook()
			return self.place
		elif action == "store letter":
			ex45to.addbook(self.letter)
			return self.place
			print "letter are now stored in your notebook"
		elif action == "kitchen":
			return 'kitchen'
		elif action == "bedroom":
			return 'bedroom'
		elif action == "hall":
			return 'hall'
		elif action == "livingroom":
			return 'livingroom'
		elif action == "bathroom":
			return 'bathroom'
		elif action == "help":
			ex45to.help()
			return self.place
		elif action == "guess":
			ex45to.guessword()
			return self.place
		elif action == "skriv":
			skriv()
		else:
			print "Please choose one of the commands"
			return self.place
class Bedroom(Scene):
	
	def enter(self):
		self.letter = ['y']
		self.place = 'bedroom'
	
		print "You are in the %s" %self.place

		
		action = raw_input("> ")
		
		if action == "letter":
			print self.letter
			return self.place
		elif action == "check notebook":
			ex45to.checkbook()
			return self.place
		elif action == "store letter":
			ex45to.addbook(self.letter)
			return self.place
			print "letter are now stored in your notebook"
		elif action == "kitchen":
			return 'kitchen'
		elif action == "bedroom":
			return 'bedroom'
		elif action == "hall":
			return 'hall'
		elif action == "livingroom":
			return 'livingroom'
		elif action == "bathroom":
			return 'bathroom'
		elif action == "help":
			ex45to.help()
			return self.place
		elif action == "guess":
			ex45to.guessword()
			return self.place
		elif action == "skriv":
			skriv()
		else:
			print "Please choose one of the commands"
			return self.place
class Kitchen(Scene):
	
	def enter(self):
		self.letter = ['h', 'n']
		self.place = 'kitchen'
	
		print "You are in the %s" %self.place

		
		action = raw_input("> ")
		
		if action == "letter":
			print self.letter
			return self.place
		elif action == "check notebook":
			ex45to.checkbook()
			return self.place
		elif action == "store letter":
			ex45to.addbook(self.letter)
			return self.place
			print "letter are now stored in your notebook"
		elif action == "kitchen":
			return 'kitchen'
		elif action == "bedroom":
			return 'bedroom'
		elif action == "hall":
			return 'hall'
		elif action == "livingroom":
			return 'livingroom'
		elif action == "bathroom":
			return 'bathroom'
		elif action == "help":
			ex45to.help()
			return self.place
		elif action == "guess":
			ex45to.guessword()
			return self.place
		elif action == "skriv":
			skriv()
		else:
			print "Please choose one of the commands"
			return self.place
		
class Map(object):

	scenes = {
		'hall': Hall(),
		'kitchen': Kitchen(),
		'livingroom': Livingroom(),
		'bedroom': Bedroom(),
		'bathroom': Bathroom()
	}
		
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
			
a_map = Map('hall')
a_game = Engine(a_map)
a_game.play()
		
		
		
	
