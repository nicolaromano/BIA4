from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

digits = load_digits()

x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2)

# Train an SVM classifier
classifier = SVC()
classifier = classifier.fit(x_train, y_train)

# train_prediction = classifier.predict(x_train)
# print(confusion_matrix(y_train, train_prediction))


test_prediction = classifier.predict(x_test)
print(confusion_matrix(y_test, test_prediction))