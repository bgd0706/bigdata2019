import pandas as pd
from sklearn import svm, metrics
import itertools
import operator
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
import pandas as pd

csv = pd.read_csv('winequality-both.csv')
csv_data = csv[['alcohol' ,'fixed acidity','free sulfur dioxide','residual sugar','total sulfur dioxide']]
csv_label = csv['quality']

for i in range(10) :
    train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)

    clf = svm.SVC(gamma='auto')
    clf.fit(train_data, train_label)
    pre = clf.predict(test_data)

    ac_score = metrics.accuracy_score(test_label, pre)
    print(ac_score*100)
