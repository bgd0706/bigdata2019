# full 조합이 아닌
import pandas as pd
from sklearn import svm, metrics
import itertools
import operator

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

wine_label = wine.loc[:, "quality"]

# v_list = ['alcohol', 'chlorides', 'citric_acid', 'density', 'fixed_acidity', 'free_sulfur_dioxide', 'pH', 'residual_sugar',
#         'sulphates', 'total_sulfur_dioxide', 'volatile_acidity']
# v_list = ['alcohol','citric_acid','density','free_sulfur_dioxide','sulphates','total_sulfur_dioxide','volatile_acidity'] # 머신러닝 안했을 때 최고의 조합
v_list = ['alcohol', 'fixed_acidity', 'free_sulfur_dioxide', 'residual_sugar','total_sulfur_dioxide']
wine_data = wine.loc[:, v_list]

clf = svm.SVC(gamma='auto')
clf.fit(wine_data,wine_label)
pre = clf.predict(wine_data)

ac_score = metrics.accuracy_score(wine_label, pre)
print(ac_score*100,'%')