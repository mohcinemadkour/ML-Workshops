from py2neo import authenticate, Graph, Node, Relationship
import getpass
import db_vis1
import re

uname = "neo4j"
passw = "beta"

authenticate("localhost:7474",uname,passw)
graph = Graph("http://localhost:7474/db/data/hackthon") # create instances of a Graph() class 

q1 = '''
MATCH (n:Patient) RETURN n
'''

q2 = '''
MATCH (n:Term) RETURN n
'''

q3 = '''
MATCH (n:Disease) RETURN n
'''

q4 = '''
MATCH (n:PatientMaritalStatus) RETURN n
'''

q5 = '''
MATCH (n:Gender) RETURN n
'''

q6 = '''
MATCH (n:District) RETURN n
'''

q7 = '''
MATCH (n:Age) RETURN n
'''



def extractElements(q1):
	data = graph.run(q1)
	elements = [re.findall('"([^"]*)"',str(row[0]))[0] for row in data]
	return elements


def nodelabels():
	Patient = extractElements(q1)
	#Patient.append('-all-')
	#Patient.append('-None-')
	Term = extractElements(q2)
	#Term.append('-all-')
	#Term.append('-None-')
	Disease = extractElements(q3)
	#Disease.append('-all-')
	#Disease.append('-None-')
	PatientMaritalStatus = extractElements(q4)
	Gender = extractElements(q5)
	District = extractElements(q6)
	#District.append('-all-')
	Age = extractElements(q7)
	#Age.append('-all-')
	return Patient,Term,Disease,PatientMaritalStatus,Gender,District,Age

