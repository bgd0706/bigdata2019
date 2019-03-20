import pandas as pd
from sklearn import svm, metrics
import itertools
import operator

wine = pd.read_csv('revised_wine.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

wine_label = wine.loc[:, "quality"]

v_list = ['alcohol', 'fixed_acidity', 'free_sulfur_dioxide', 'residual_sugar','total_sulfur_dioxide']

wine_data = wine.loc[:, v_list]
clf = svm.SVC(gamma='auto')
clf.fit(wine_data, wine_label)
pre = clf.predict(wine_data)
ac_score = metrics.accuracy_score(wine_label, pre)
print(ac_score)

