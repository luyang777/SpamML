import os
import numpy as np
from collections import Counter
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.svm import SVC, NuSVC, LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from features import make_Dictionary,extract_features

##Create the dictionary
training_dir = 'Train'
dictionary = make_Dictionary(training_dir)

##vectors
##0 stands for a SPAM
traning = np.zeros(139)
traning[88:139] = 1
train_matrix = extract_features(training_dir,dictionary)

# NB classifier
model1 = MultinomialNB()
model2 = GaussianNB()
model1.fit(train_matrix,traning)
model2.fit(train_matrix,traning)

# Test the unseen mails for SPAM
test_dir = 'TESTING_RESULT'
test_matrix = extract_features(test_dir,dictionary)
test = np.zeros(202)
test[180:202] = 1
result1 = model1.predict(test_matrix)
result2 = model2.predict(test_matrix)

print("MultinomialNB | HAM | SPAM")
print(confusion_matrix(test,result1))
##Calculate the accuracy score
print(accuracy_score(test, result1))

print("GaussianNB | HAM | SPAM")
print(confusion_matrix(test,result2))
##Calculate the accuracy score
print(accuracy_score(test, result2))


