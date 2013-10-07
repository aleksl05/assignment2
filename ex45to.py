notebook = []
commands = ["letter", 
			"check notebook", 
			"store letter", 
			"kitchen", 
			"bedroom", 
			"livingroom",
			"bathroom",
			"hall"
			]
			
answer = "python"
answerlist = list(answer)
			
def help():
	print "Here are the commands:"
	for x in commands:
		print x
		
	raw_input()

def skriv():
	print answer
	print answerlist
	print len(notebook)
	
	
def guessword():
	myanswer = raw_input("Type your guess here!")
	
	hits = []
	for letter in answerlist:
		if letter in notebook and letter not in hits:
			hits.append(letter)
	if len(hits) == len(answerlist) and myanswer == answer:
		print "You have answered correctly and collected all"
		print "the letters, congratulation, you have won!!!"
		return 'finished'
	else:
		print "You have either answered wrong or not collected all the letters"
		return 'hall'

def checkbook():
	if len(notebook) == 0:
		print "There is nothing in the notebook!"
	else:
		print "The letter in your notebook is: ", notebook
		
	raw_input("Press enter when finished")
		
def addbook(note):
	notebook.extend(note)
	raw_input("Your letter are added, press enter when finished")