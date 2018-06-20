from os import path
import sys
from tqdm import tqdm
sys.path.append(path.abspath('./util'))
from dataclean import *
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
np.random.seed(10)

#no_feature = 300


trData = pd.read_csv("TrainDataSet.csv",sep="\t")
trData.drop(['Unnamed: 0'], axis = 1, inplace = True)

holdtext = np.array(trData['text'])
vect = CountVectorizer(max_features=5000)
vect.fit(holdtext)
simple_train_dtm = vect.transform(holdtext)
std   =  simple_train_dtm.toarray()
print("Extracted feature dimension: "+str(std.shape))
tab = pd.DataFrame(simple_train_dtm.toarray(),columns=vect.get_feature_names())
#tab.to_csv("Genrated_feature_vector.csv")
print("Enter n_component of PCA: ")
no_feature = int(input())


from sklearn.decomposition import PCA
pca = PCA(n_components=no_feature)
fit = pca.fit(std)
tx = pd.DataFrame(pca.components_,columns=tab.columns)
td  = np.array(tx)
tmp = td[-1]
newA = np.copy(tmp)
pos=[]
for i in range(no_feature):
    mx = np.where(newA==np.max(newA))
    pos.append(mx[0][0])
    newA[mx[0][0]]=-999

newcolname = tx.columns[pos]
newcolname
val = []
for i in newcolname:
    val.append(i)

redu_features = tab[val]

print("Selected feature dimension: "+str(redu_features.shape))

X = np.array(redu_features)
y = np.array(trData['lable'].astype('int'))

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=10)

print("------------ SVM -------------")
from sklearn import svm
clf = svm.SVC()
clf.fit(X_train, y_train) 
result1 = clf.predict(X_test)
print("Confusion_matrix SVM: ")
print(confusion_matrix(y_test,result1))
print(" ")
print("Accuracy_score: SVM ")
print(accuracy_score(y_test,result1))
print(" ")


print("------------ Boosted Tree -------------")
import xgboost as xgb
model_xgboost = xgb.XGBClassifier()
model_xgboost.fit(X_train,y_train)
pred = model_xgboost.predict(X_test)
print("Confusion_matrix Boosted Tree: ")
print(confusion_matrix(y_test,pred))
print(" ")
print("Accuracy_score: Boosted Tree ")
print(accuracy_score(y_test,pred))