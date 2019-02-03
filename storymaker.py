import logging
import random

class conf:
	startwords = ["mom"]
	#Any words that the story can start with.
	
	length = 10
	#The amount of words for the story to have.
	
	story = open("story.txt", "r").read().split(" ")
	
	newstory = []
	
	wordbank = {}
	
	log = logging.getLogger(__name__)
	
	logfile = logging.FileHandler("storymaker.log")
	
	logformat = logging.Formatter(fmt="%(asctime)s : %(levelname)s - %(message)s")
	
	
	

def setup():
	conf.log.setLevel(logging.DEBUG)
	conf.logfile.setLevel(logging.DEBUG)
	conf.logfile.setFormatter(conf.logformat)
	conf.log.addHandler(conf.logfile)
	conf.log.info("Run started.")
	
	
def config_word():
	conf.log.info("Word Configuration started.")
	x = 0
	while x < len(conf.story):
		conf.wordbank[conf.story[x]] = []
		conf.log.info("Checked index for token " + conf.story[x])
		x = x + 1
	x = 0
	lastwordchecked = 0
	while x < len(conf.story):
		tempword = conf.story[lastwordchecked]
		try:
			conf.wordbank[tempword].append(conf.story[lastwordchecked + 1])
		except IndexError:
			pass
		x = x + 1
		lastwordchecked = lastwordchecked + 1
	conf.log.info("Word indexing finished. Results: " + str(conf.wordbank))
			
def getWords():
	lastword = random.choice(conf.startwords)
	conf.newstory.append(lastword)
	x = 0
	while x < conf.length:
		try:
			nextword = random.choice(conf.wordbank[lastword])
		except:
			pass
		conf.newstory.append(nextword)
		conf.log.info(lastword + " token detected. Chose " + nextword + " to be next word.")
		lastword = nextword
		x = x + 1
		
		

if __name__ == "__main__":
	setup()
	config_word()
	getWords()
	print(" ".join(conf.newstory))  	  
