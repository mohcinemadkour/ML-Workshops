from os import sys
sys.path.insert(0, '/home/putus/working_directory/hackathon/code/')
from elements import nodelabels
from databaseQ import ask_question_Neo

def rfe(ask_question):
	if ask_question[0]==False and ask_question[1]==False and ask_question[2]==False:
		print("startNeo")
	else:
		ask_question_Neo(ask_question)