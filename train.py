from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import joblib

iris = datasets.load_iris()
X, y = iris.data, iris.target

clf = LogisticRegression(max_iter=200)
clf.fit(X, y)

joblib.dump(clf, 'iris_model.pkl')
