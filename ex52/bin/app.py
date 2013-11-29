import web
import map

urls = (
  '/game', 'GameEngine',
  '/', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('templates/', base="layout")

if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'room': None})
    web.config._session = session
else:
    session = web.config._session

#This is the class that is being "runned" first and where everything starts
#It sets the room to be START, which is bedroom. 
class Index(object):
    def GET(self):
        session.room = map.START
        web.seeother("/game")
		
#Player-class which is used to store letters. Was meant to become bigger and
#the possibility to store keys to open doors and stuff, but didn't get the time to do it.
class Player(object):
	def __init__(self, name):
		self.name = name
		self.notebook = [] 
	
	#Simple function that add letters to the notebook
	def add_to_notebook(letter):
		self.notebook.append(letter)
		

#creates a player-object which is being used in the GameEngine.
player = Player("Aleksander")
		
	
#This is where everything happens, where input is being fetched and analyzed and used.
class GameEngine(object):
	
	def __init__(self):
		self.commands = {'restart': self.restart, 
							'help' : self.help,
							'show letter' : self.show_letter,
							'check notebook' : self.check_notebook,
							'store letters' :  self.store_letter}

	def GET(self):
		if session.room:
			return render.show_room(room=session.room)
		else:
			return render.you_lost()
			
	def store_letter(self):
		if session.room.letter:
			session.room.output = "The letters : %s are stored in your notebook" % session.room.show_letter()
			player.notebook.append(session.room.letter.pop())

		else:
			session.room.output = "There are no letters in this room"
		
	def check_if_letters(self):
		return len(player.notebook) == len(session.room.answer)
	
	def check_notebook(self):
		if len(player.notebook) >0:
			session.room.output = "The letters in your notebook is:  %s" % (str(player.notebook))
		else:
			session.room.output = "There are no letters in your notebook"
			
	def show_letter(self):
		if len(session.room.letter)>0:
			session.room.output = "The letters in this room are: %s"  %session.room.show_letter()
		else:
			session.room.output = "There are no letters in this room anymore" 
			
	def restart(self):
		session.room = map.START
		web.seeother('/game')
		
	#Notifies the player to use right commands
	def warning(self):
		session.room.output = "Please write a correct command, type help to get the commands"
	
	#Display the commands
	def help(self):
		session.room.output = "You are in the %s , the commandlist is: %s"  %(session.room.name, self.commands.keys())
		
	#Different conditions for the form.
	def POST(self):
		form = web.input(action=None)
		if form.action and session.room:
			if self.check_if_letters():
				map.go_to_end()
				if form.action == session.room.answer:
					winner = session.room.go('*')
					session.room = winner
			else:
				transition = session.room.go(form.action)
				if transition == None:
					self.warning()
				elif transition != None:
					session.room = transition
		else:
			session.room.output = "Hey mister, you are doing it wrong, you have to write somee commands! %s" % self.check_if_letters()
		if form.action in self.commands:
			self.commands[form.action]()
	
		web.seeother('/game')

if __name__ == "__main__":
    app.run()