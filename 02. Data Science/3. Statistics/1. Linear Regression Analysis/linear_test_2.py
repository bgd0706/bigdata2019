import pandas as pd
from statsmodels.formula.api import ols
import itertools
import operator

print("고정변수를 조합해서 정답률을 올려본다. -> 최적의 공식을 찾아낸다.")
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

v_list = ['alcohol', 'chlorides', 'citric_acid', 'density', 'fixed_acidity', 'free_sulfur_dioxide', 'pH', 'residual_sugar',
        'sulphates', 'total_sulfur_dioxide', 'volatile_acidity']
answer_dict = {}

for c_len in range(1, len(v_list)+1) :
    a_list =list(map(','.join, itertools.combinations(v_list, c_len)))
    for a_len in range(len(a_list)) :
        b_list = a_list[a_len].split(',') # 조합
        my_formula = 'quality ~ '
        for idx in range(len(b_list)):
            if idx != len(b_list) - 1:
                    my_formula = my_formula + b_list[idx] + ' + '
            else:
                    my_formula = my_formula + b_list[idx]
        lm = ols(my_formula,data=wine).fit()

        independent_variables = wine[b_list]
        new_observations = wine.loc[wine.index, independent_variables.columns]
        y_predicted = lm.predict(new_observations)
        y_predicted_rounded = [round(score) for score in y_predicted]

        count = 0
        for idx in range(len(wine.index)) :
            if wine['quality'][idx] == y_predicted_rounded[idx] :
                count += 1
        answer_dict[(',').join(b_list)] = count / len(wine) * 100

sortedList = sorted(answer_dict.items(), key=operator.itemgetter(1), reverse=True)
print(sortedList[0])