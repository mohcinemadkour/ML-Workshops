import csv
import os
import json
import subprocess
from time import sleep
from django.shortcuts import render,HttpResponse
import glob
from os import sys
sys.path.insert(0, '/home/putus/working_directory/hackathon/code/')
from elements import nodelabels
from databaseQ import ask_question_Neo
from .medcore import rfe

Patient,Term,Disease,PatientMaritalStatus,Gender,District,Age = nodelabels()

def home(request):
    return render(request, 'myhack/home.html', {})


def graph(request):
    return render(request, 'myhack/result_graph-42.html')

def Upload(request):
    for count, x in enumerate(request.FILES.getlist("files")):
        def process(f):
            with open('/home/putus/working_directory/hackathon/hackathon/file_'+str(count), 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        process(x)
    # return HttpResponse("File(s) uploaded")
    sleep(0.01)
    return render(request, 'myhack/search.html', {})

def search(request): 
    cname = request.POST.get('dropdown1',False)
    if request.POST:
        #Disease_query = request.POST['dropdown1']
        f1 = request.POST.get('selectx',False)
        f2 = request.POST.get('meal',False)
        f3 = request.POST.get('category',False)
        ask_question = [f1,f2,f3]
        print(ask_question)
        rfe(ask_question)
        return render(request, 'myhack/search.html', {'previous_query':ask_question,'content1': Patient, 'content2':Term,
            'content3':Disease, 'content4':PatientMaritalStatus, 'content5':Gender, 'content6':District, 'content7':Age})
    else:
    	return render(request, 'myhack/search.html', {'previous_query':ask_question,'content1': Patient, 'content2':Term,
            'content3':Disease, 'content4':PatientMaritalStatus, 'content5':Gender, 'content6':District, 'content7':Age})


      
