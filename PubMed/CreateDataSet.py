from os import path
import sys
from tqdm import tqdm
sys.path.append(path.abspath('./util'))
from dataclean import *
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
cancer_file_loc = "./Dataset/train/cancer/"
non_cancer_file_loc = "./Dataset/train/noncancer/" 
files_cancer = loadFiles(cancer_file_loc)
files_noncancer = loadFiles(non_cancer_file_loc)
cancer=[]
for i in tqdm(files_cancer):
    xmlDoc = open(i, 'r')
    xmlDocData = xmlDoc.read()
    html=xmlDocData
    cleanhtml = clean_html(html)
    text = html2text(cleanhtml)
    soup = BeautifulSoup(html,"lxml")
    text2 = soup.get_text()
    cancer.append([text2,'c'])

noncancer=[]
for i in tqdm(files_noncancer):
    xmlDoc = open(i, 'r')
    xmlDocData = xmlDoc.read()
    html=xmlDocData
    cleanhtml = clean_html(html)
    text = html2text(cleanhtml)
    soup = BeautifulSoup(html,"lxml")
    text2 = soup.get_text()
    noncancer.append([text2,'nc'])

cnT  = pd.DataFrame(cancer,columns=['text','lable'])
NcnT = pd.DataFrame(noncancer,columns=['text','lable'])
cm = [cnT,NcnT]
df = pd.concat(cm,ignore_index=True)
df = df.sample(frac=1).reset_index(drop=True)

data   = df
data   = np.array(data['text'])
lable  = df['lable'].map({"c":1,"nc":0})
lable  = np.array(lable)

dataset = cleanDatset(data)
t1=pd.DataFrame(dataset,columns=["text"])
t2=pd.DataFrame(lable,columns=["lable"])
trData = pd.concat([t1,t2],axis=1)

trData.to_csv("TrainDataSet.csv",sep='\t',encoding='utf-8')