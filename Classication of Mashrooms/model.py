from keras.layers import Dense
from keras.models import Sequential
import keras.utils
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

# seed weights
np.random.seed(3)

# import dataset
data = pd.read_csv('agaricus-lepiota.csv', delimiter=',')

# encode labels as integers so the can be one-hot-encoded which takes int matrix
le = preprocessing.LabelEncoder()
data = data.apply(le.fit_transform)

# one-hot-encode string data (now type int)
ohe = preprocessing.OneHotEncoder(sparse=False)
data = ohe.fit_transform(data)

X = data[:, 1:23]
Y = data[:, 0:1]

# split into test and train set
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.2, random_state=5)

# create model
model = Sequential()
model.add(Dense(1, input_dim=22,  activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=1000, batch_size=25)
