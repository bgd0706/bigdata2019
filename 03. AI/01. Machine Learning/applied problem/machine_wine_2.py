import pandas as pd
from sklearn import svm, metrics
import itertools
import operator

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

wine_label = wine.loc[:, "quality"]

v_list = ['alcohol', 'chlorides', 'citric_acid', 'density', 'fixed_acidity', 'free_sulfur_dioxide', 'pH', 'residual_sugar',
        'sulphates', 'total_sulfur_dioxide', 'volatile_acidity']

anwser_dict = {}
total_count = 0
for c_len in range(1, len(v_list)+1) :
    a_list =list(map(','.join, itertools.combinations(v_list, c_len)))
    for a_len in range(len(a_list)) :
        b_list = a_list[a_len].split(',')
        wine_data = wine.loc[:, b_list]
        clf = svm.SVC(gamma='auto')
        clf.fit(wine_data, wine_label)
        pre = clf.predict(wine_data)
        ac_score = metrics.accuracy_score(wine_label, pre)
        anwser_dict[(',').join(b_list)]=ac_score
        print(total_count)
        total_count += 1

sortedList = sorted(anwser_dict.items(),  key=operator.itemgetter(1), reverse=True)
print(sortedList[0])