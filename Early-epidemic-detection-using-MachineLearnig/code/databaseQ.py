from py2neo import authenticate, Graph, Node, Relationship
import getpass
import db_vis1
import re
import numpy as np

options = {"Disease":'name','Patient':'name','Term':'name','PatientMaritalStatus':'name',
           'Gender':'name','District':'name','Age':'name'}

uname = "neo4j"
passw = "beta"

authenticate("localhost:7474",uname,passw)
graph = Graph("http://localhost:7474/db/data/hackthon") # create instances of a Graph() class 

Q2 = '''
match (u:Disease) with u,size( ()-[]->(u)) 
as topDisease order by topDisease desc limit 5 return u.name as label, topDisease
'''
data2 = graph.run(Q2)
topDisease = []

for d1 in data2:
    #print(d1)
    topDisease.append(re.findall(r"'(.*?)'",str(d1), re.DOTALL)[1])

def query2graph(query):
    list_result=[]
    resultQuery = graph.run(query)
    for data in resultQuery:
        list_result.append(data)
    return list_result

def findCommonPatient(cmDisease):
    ResultQuery = graph.run(cmDisease)
    common_patient = []
    for data in ResultQuery:
        val = str(data)
        val = re.findall('"([^"]*)"',val)
        common_patient.append(val[0])
    return common_patient

def ask_question_Neo(query):
    lst = query
    source = lst[0]
    target = lst[1]
    target_name = lst[2]
    if target == "Disease":
    	target_name = target_name+" "
    query_x = "match (u:Patient)-[r1]->(t:"+target+') WHERE t.name="'+target_name+'" RETURN u AS source_node, id(u) AS source_id, r1, t AS target_node, id(t) AS target_id'
    s1 = "First we look into what are the common 'patient' for this target: %s" %(target_name)
    print(s1)
    CD = findCommonPatient(query_x)
    list_result = query2graph(query_x)
    CD = sorted(set(CD), key=lambda x:CD.index(x))
    for eachelement in CD:
        query_y = "match (u:Patient)-[r1]->(t:"+source+') WHERE u.name="'+eachelement+'" RETURN u AS source_node, id(u) AS source_id, r1, t AS target_node, id(t) AS target_id'
        res = graph.run(query_y)
        c=2
        for dt in res:
            if c>0:
                list_result.append(dt)
                c=c-1
    data = list_result
    options = {"Disease":'name','Patient':'name','Term':'name','PatientMaritalStatus':'name','Gender':'name','District':'name','Age':'name'}
    db_vis1.draw(data,options,'/home/putus/working_directory/hackathon/hackathon/myhack/templates/myhack/result_')
    #return data