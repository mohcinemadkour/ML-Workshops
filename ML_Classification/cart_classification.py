from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.cross_validation import train_test_split

# Decision Tree Classifier
cart = DecisionTreeClassifier()

# Loading data
iris = load_iris()
train_data = iris.data
train_class = iris.target

### test on sample data
cart.fit(train_data,train_class)
text_data = [[3, 5, 4, 2], [5, 4, 3, 2]]
print " sample data prediction : ",cart.predict(text_data)

### test on entire data with accuracy
cart.fit(train_data,train_class)
test_class = cart.predict(train_data)
print " entire data accuracy : ",metrics.accuracy_score(train_class,test_class)

## training and testing with cross validation
train_data,test_data,train_class,test_class = train_test_split(iris.data,iris.target, test_size =0.8, random_state=4)
cart.fit(train_data,train_class)
pred_class = cart.predict(test_data)
print " cross validation accuracy : ",metrics.accuracy_score(test_class,pred_class)

