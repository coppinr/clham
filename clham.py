#!/usr/bin/env python
"""
CLHAM

Command-Line (Canadian) HAM:
Test generator for the Industry Canada amateur radio question banks

by Rhiannon Coppin, North Vancouver, B.C.

Updated: Oct. 10, 2015

Quick Start:

Usage: clham.py -i <input textfile>

OPTIONAL arguments:

       -a (use for advanced question set [DEFAULT is basic])
       -m (mode: "exam" for exam silumator [DEFAULT is "all" questions])
       -f (use to select Francais [DEFAULT landuage is English])

Enter "q" anytime to quit.

Notes:

    The input text file can be the Industry Canada delimited question bank, or the output of "wrong answers" obtained from a previous run of this program.

    The exam mode ("-m exam") runs through one pseudo-randomly chosen question from each section (though you can restrict which sections to pull from), resulting in a generated test of 50 questions for the Advanced set, and of 100 questions for the Basic set.

    You are given the option after finishing the test, or even after entering "q" to quit, to save the questions you got wrong to a text file. You can then rerun that text file as input, and run a test from only your 'problem' questions.

    The French translation of the intro and section labels is poor; the labelling of the section in English may also be questionable.

Sample Usage:

To run one or more entire sections from the Advanced Question Bank:

    python clham.py -a -i amat_adv_quest/amat_adv_quest_delim.txt

To run a simulated Advanced exam:

    python clham.py -a -i amat_adv_quest/amat_adv_quest_delim.txt -m exam

To run one or more entire sections from the Basic Question Bank:

    python clham.py -i amat_basic_quest/amat_basic_quest_delim.txt

To run a simulated Basic exam:

    python clham.py -i amat_basic_quest/amat_basic_quest_delim.txt -m exam

To run the set of questions you got wrong and save to a textfile (say, name "wrong_answers.txt") from a previous run this program:

    python clham.py -i wrong_answers.txt

To run the Industry Canada question banks in French instead, add the switch "-f" to any of the commands above
Details:

This command-line python utility reads in and presents various forms of the basic and advanbced question banks, which are made available as dual-language delimited text files from Industry Canada's website.

The URLs of these file (zipped) at this time (Oct. 2015) are:

    http://apc-cap.ic.gc.ca/datafiles/amat_basic_quest.zip
    http://apc-cap.ic.gc.ca/datafiles/amat_adv_quest.zip

Locator URL on Industry Canada site: http://www.ic.gc.ca/eic/site/025.nsf/eng/h_00004.html

Note: If the format of the file changes substantially, this program may need modification to function.

The current schema of the text question bank is, as Industry Canada states:

Each record has the following data, separated by ";"

    Question ID
    English Question
    Correct English Answer
    Incorrect English Answer 1
    Incorrect English Answer 2
    Incorrect English Answer 3
    French Question
    Correct French Answer
    Incorrect French Answer 1
    Incorrect French Answer 2
    Incorrect French Answer 3


"""

title = """
##################################################################
####                                                          ####
####      CCCCCC  LLL     HHH  HHH      A      MM       MM    ####
####	 CCCC     LLL     HHH  HHH     AAA     MMMM    MMM    ####
####	CCC       LLL     HHH  HHH    AA AA    MMMMMMMMMMM    ####
####    CCC       LLL     HHHHHHHH   AAAAAAA   MMM  M  MMM    ####
####	 CCCC     LLL     HHH  HHH  AAA   AAA  MMM     MMM    ####
####	  CCCCCC  LLLLLLL HHH  HHH AAAA   AAAA MMM     MMM    ####
####                                                          ####
##################################################################

"""
intro = [
"Command-Line HAM: Helping you study for the Canadian Amateur Radio Licensing exam(s)",
"Command-Line HAM: Vous aidez a etudier pour l'examen 'Canadian Amateur Radio Licensing'"]
section_select = [ [
		"""Which sections would you like to run?\nHit 'Enter' for all or type a single digit (e.g. 1), a range (1-8) or a list of comma-separated values and/or ranges ( (1,3,4,5,6) or (1,3,4-6) ) and then hit 'Enter':
    	1 - Regulations and Policies (25 subsections)
    	2 - Operating and Procedures (9 subsections)
    	3 - Station Assembly, Practices and Safety (21 subsections)
    	4 - Circuit Components (6 subsections)
    	5 - Basic Electronics and Theory (13 subsections)
    	6 - Antennas and Feedlines (13 subsections)
    	7 - Propagation (8 subsections)
    	8 - Interference and Suppression (5 subsections)
    	""",
    	"""Quel(s) sections voulez-vous essayer?\nAppuyez 'Enter' pour tous, ou entrez un chiffre, un 'range' (1-8), ou une series de nombres comme ca: (1,3,4):
    	1 - Regulations
    	2 - Operations
    	3 - Station Assembly, Practices and Safety
    	4 - Electronique (1)
    	5 - Electronique (2)
    	6 - Les antennas
    	7 - Propagation
    	8 - L'Interference et la Suppression
    	"""
	],
	[
		"""Which sections would you like to run?\nHit 'Enter' for all or type a single digit (e.g. 1), a range (1-8) or a list of comma-separated values and/or ranges ( (1,3,4,5,6) or (1,3,4-6) ) and then hit 'Enter':
    	1 - RF current, time constant, RLC circuit resonance and Q (5 subsections)
    	2 - Diodes, op-amps, frequency multipliers, crystal oscillators, filters (12 subsections)
    	3 - Measuring with voltmeter, oscilloscope, freq. counter, dip meter (6 subsections)
    	4 - Transformers and power supplies (4 subsections)
    	5 - Modulation (9 subsections)
    	6 - Signal processing (5 subsections)
    	7 - Antennas and tuning (9 subsections)
    	""",
    	"""Quel(s) sections voulez-vous essayer?\nAppuyez 'Enter' pour tous, ou entrez un chiffre, un 'range' (1-7), ou une series de nombres comme ca: (1,3,4):
    	1 - RF / RLC (5)
    	2 - Semiconductors (12)
    	3 - Measurements (6)
    	4 - Power (4)
    	5 - Modulation (9)
    	6 - Signal processing (5)
    	7 - Antennas (9)
    	"""
	]
]

"""
TO DO
FIXED - UNICODE French character compatibility problem
Better french translation
Timer for test simulator mode
ADD URL downloadability
"""
import re
import time

def usage():
    return """\nUsage: clham.py -i <input textfile> \nOPTIONAL arguments: \t-a <advanced question set [DEFAULT is basic]> \n\t\t\t-m <mode: all [DEFAULT], exam>\n\t\t\t-f <selects francais -- English is DEFAULT>"""

def pause():
	print("(Hit enter to continue.)")
	inp=raw_input()


class CLHAM:

    def __init__(self):
    	# input filename or URL
        self.__filename = ''
        self.__test_type = 0 #basic
        #mode = all questions, just some sections, or an exam simulation mode
        self.__mode = 'all'
        #default language is english
        #self.__language = 'english'
        self.__lang_sel = 0
        self.__fullbank = []
    	self.__workingbank = []
    	self.__wronganswers = []
    	self.__starttime = 0
    	self._endtime = 0
    	
    def parseOptions(self, args):
    	import getopt
    	try:
    		optlist, arglist = getopt.getopt(args, 'i:m:af')  #f is a switch and doesn't require an arg. 'a' too.
    	except getopt.GetoptError, e:
    		print e
    		return None
    	
    	for option, value in optlist:
    		if option.lower() in ('-i', ):
    			self.__filename = value
    		if option.lower() in ('-a', ):
    			self.__test_type = 1 #advanced
    		elif option.lower() in ('-m', ):
    			self.__mode = value
    		elif option.lower() in ('-f', ):
    			self.__lang_sel = 1


        if not self.__filename:
            sys.exit("Error: filename or URL not given")
    
    def print_intro(self):
    	print intro[self.__lang_sel]
            
    def loadquestionbank(self):
		print("Loading question bank from \""+ self.__filename+ "\"")
		count = 0
		try:
			f = open(self.__filename, 'r')
			#This is to ensure the Latin-1 or whatever encoded text file works in Terminal, esp. with French characters
			sourceEncoding = "iso-8859-1"
			targetEncoding = "utf-8"
			raw_text = f.readline().rstrip()
			while raw_text:
				count += 1
				raw_text = unicode(raw_text, sourceEncoding).encode(targetEncoding)
				self.__fullbank.append(raw_text.split(';'))
				raw_text = f.readline()
		except (OSError, IOError), e:
			print e		
				
		
    def generatetest(self):
    	from random import shuffle
    	import random
    	text = section_select[self.__test_type]
    	print text[self.__lang_sel]
    	inp = raw_input()
    	tempbank = []
    	if inp == '':
    		if self.__test_type == 0:
	    		sections = [1,2,3,4,5,6,7,8]
	    	else:
	    		sections = [1,2,3,4,5,6,7]
        elif inp.lower() == 'q':
	    	quit()
        else:
    		ranges = (x.split("-") for x in inp.split(","))
    		sections = [i for r in ranges for i in range(int(r[0]), int(r[-1])+1)]
    	
    	if self.__mode == 'all':
    		for section in sections:
    			for item in self.__fullbank[1:]:
	    			if int(item[0].split('-')[1]) == int(section):
    					tempbank.append(item)
    	
    	if self.__mode == 'exam':
    			print "Generating exam simulator from selected sections. (This means each subsection per major section is represented in exactly one question.)"
    			current_section = 1
    			subsection = 1
    			mini_subbank = []
    			for item in self.__fullbank[1:]:
    				if int(item[0].split('-')[1]) in sections:
    					current_section = int(item[0].split('-')[1])
    					if subsection == int(item[0].split('-')[2]):
    						mini_subbank.append(item)
    					else:
    						winner = random.choice(range(0,len(mini_subbank)))
    						tempbank.append(mini_subbank[winner])
    						mini_subbank = []
    						subsection += 1
    					if int(item[0].split('-')[2]) < subsection:
    						current_section +=1
    						subsection = 1
    			#Finish the final loop
    			winner = random.choice(range(0,len(mini_subbank)))
    			tempbank.append(mini_subbank[winner])
    			#for item in tempbank:
    			#	print item[0]
 
    		#print "Generating exam simulator from sections "+ ''.join(str(sections))
    		#Since this isn't a real exam, I'm just going to shuffle them all and take the first 100
    		#shuffle(tempbank)
    		#tempbank = tempbank[0:100]
				    	
    	#Generate question bank for test
    	# Begin to parse out questions: Choose language
    	offset = self.__lang_sel
    	for question in tempbank:
    		set = [question[0], question[1+offset]]
    		temp = []
    		for i in range(2,6):
    			temp.append(question[i+offset])
    		set.append(temp)
    		self.__workingbank.append(set)
    	shuffle(self.__workingbank)
    	for question in self.__workingbank:
    		correct_answer = question[2][0]
    		shuffle(question[2])
    		question.append(correct_answer)

    	temp = [self.__fullbank[0][1]]
    	temp.append(self.__fullbank[0][2+offset:6+offset])
    	temp.insert(0,self.__fullbank[0][0])
    	self.__wronganswers.append(temp)
    	#print self.__wronganswers
    	
    	
    	print(('Test generated with '+ str(len(self.__workingbank)) +' question'+ ('s' if (len(self.__workingbank) >1) else '') +'.'))
    	
    def get_time_elapsed(self):
    	m, s = divmod(time.time() - self.__starttime, 60)
    	h, m = divmod(m, 60)
    	return "%d:%02d:%02d" % (h, m, s)
   	
    def go(self):
    	self.__starttime = time.time()
    	count = 0
    	total = len(self.__workingbank)
    	correct = 0
    	key = ['a','b','c','d']
    	print "Running quiz. Enter your answer as A, B, C or D (upper or lower case). Press Q to quit."
    	for question in self.__workingbank:
    		count += 1
    		noanswer = True
    		print str(count)+ " of "+ str(total) +". Time elapsed: "+ self.get_time_elapsed() +"\n"
    		print question[0]
    		print question[1]
    		print "[A] - "+ question[2][0].rstrip()
    		print "[B] - "+ question[2][1].rstrip()
    		print "[C] - "+ question[2][2].rstrip()
    		print "[D] - "+ question[2][3].rstrip()
    		answer = ''
    		while answer not in key:
    			if answer == 'q':
    				return
    			elif answer != '':
    			    print "You need to input either 'a', 'b', 'c', or 'd' only."
    			answer = raw_input().lower()
    			
    		if question[2][key.index(answer)] == question[3]:
				print "HAMtastic!!! That is CORRECT"
				correct +=1
    		else:
    			print "\nWRONG - The correct answer was: \n["+ key[question[2].index(question[3])].upper()+"] "+ question[3]
    			#Need to unshuffle answers to put correct one first again
    			index = question[2].index(question[3])
    			if index != 0:
    				temp = question[2][0]
    				question[2][0] = question[2][index]
    				question[2][index] = temp
    			self.__wronganswers.append(question)
    		pause()
    		percent = round((float(correct)/float(count))*100,2)
    		print "You have "+ str(correct)+" correct and "+ str(count-correct) +" wrong answers, which is a score of "+str(percent)+" %.\n"
    
    
    def save(self):
    	#self.__endtime = time.time()
		print "Total time elapsed is: "+ self.get_time_elapsed()
		print "You are leaving the CLHAM. \nWould you like to save the set of questions you got wrong to a text file?\n(You can use that file as input into the CLHAM later.)\nEnter N or n for 'no,' or type in the filename if 'yes,' and then press Enter."
		response = raw_input()
		if response == '':
			print "Goodbye."
		elif response.lower() == 'n':
			print "Your loss."
		else:		
			print "Saving questions for review to "+ response
			f = open(response, 'w')
			print self.__wronganswers
			for line in self.__wronganswers:
				temp = ';'.join(line[2])
				f.write(';'.join([line[0],line[1],temp])+'\n')
			f.close()
		#pause()
    
def main():
	print title
	
	import sys
	#To handle French characters
	reload(sys)  
	sys.setdefaultencoding('utf8')
	
	if len(sys.argv)<3:
		sys.exit(usage())
	quiz = CLHAM()
	quiz.parseOptions(sys.argv[1:])
	quiz.print_intro()
	quiz.loadquestionbank()
	quiz.generatetest()
	quiz.go()
	quiz.save()
    
	
if __name__=="__main__":
    main()
    