import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

from sklearn.neighbors import KNeighborsClassifier

X,y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, random_state=48)
x_train, x_test, y_train, y_test = tts(X,y, test_size=0.2, random_state=42)

k = 3
knn_classifier = KNeighborsClassifier(n_neighbors=k)
knn_classifier.fit(x_train,y_train)

#Utilize the model to predict data
y_pred = knn_classifier.predict(x_test)

acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc*100:.2f}%")

import matplotlib.pyplot as plt
plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train)
plt.show()