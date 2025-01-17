import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load datasets
df1 = pd.read_csv('news.csv')
df2 = pd.read_csv('IFND.csv', encoding='latin1')
df3 = pd.read_csv('news_dataset.csv', encoding='latin1')

# Initialize the Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify=Y, random_state=2)
#separating the data and label
X = news_dataset['text'].values
Y = news_dataset['label'].values

# Fit the model
model.fit(X_train, Y_train)

# Accuracy score on the training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)
print('Accuracy score of the training data : ', training_data_accuracy)

# Accuracy score on the test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, X_test_prediction)
print('Accuracy score of the test data : ', test_data_accuracy)

# Prediction for a new sample
X_new = X_test[3].reshape(1, -1)  # Reshape for a single sample
prediction = model.predict(X_new)
print(prediction)

if prediction[0] == 0:
    print('The news is Real')
else:
    print('The news is Fake')

# Check actual label
print(Y_test[3])
