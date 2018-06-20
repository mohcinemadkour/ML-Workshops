from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.cross_validation import train_test_split

# KNN Classifier
knn = KNeighborsClassifier(n_neighbors =5) # k = 5

# Loading data
iris = load_iris()
train_data = iris.data
train_class = iris.target

### test on sample data
knn.fit(train_data,train_class)
text_data = [[3, 5, 4, 2], [5, 4, 3, 2]]
print "k = 5, sample data prediction : ",knn.predict(text_data)

### test on entire data with accuracy
knn.fit(train_data,train_class)
test_class = knn.predict(train_data)
print "k = 5, entire data accuracy : ",metrics.accuracy_score(train_class,test_class)

## training and testing with cross validation
train_data,test_data,train_class,test_class = train_test_split(iris.data,iris.target, test_size =0.4, random_state=4)
knn.fit(train_data,train_class)
pred_class = knn.predict(test_data)
print "k = 5, cross validation accuracy : ",metrics.accuracy_score(test_class,pred_class)

