import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

from sklearn.svm import SVC

x, y = datasets.make_classification(
    n_samples=1000, n_features=2, n_informative=2, n_redundant=0, random_state=42
)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=100
)

svm_classifier = SVC(kernel="linear")
svm_classifier.fit(x_train, y_train)
y_pred = svm_classifier.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)


classA = np.array([x_test[i] for i in range(len(x_test)) if y_pred[i] == 0])
classB = np.array([x_test[i] for i in range(len(x_test)) if y_pred[i] == 1])

plt.scatter(classA[:, 0], classA[:, 1])
plt.scatter(classB[:, 0], classB[:, 1])
plt.legend(["Class 0", "Class 1"], loc="upper right")
plt.show()
