from os import sys
sys.path.insert(0, '/home/putus/working_directory/hackathon/code/')
from elements import nodelabels
from databaseQ import ask_question_Neo

print(ask_question_Neo(['Disease', 'District', 'Jodhpur']))
