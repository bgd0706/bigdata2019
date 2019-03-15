import pandas as pd
from statsmodels.formula.api import ols
import itertools

print("고정변수를 조합해서 정답률을 올려본다. -> 최적의 공식을 찾아낸다.")
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

v_list = ['alcohol', 'chlorides', 'citric_acid', 'density', 'fixed_acidity', 'free_sulfur_dioxide', 'pH', 'residual_sugar',
        'sulphates', 'total_sulfur_dioxide', 'volatile_acidity']
answer = []
answer_index = 1
for c_len in range(1, len(v_list)+1) :
        a_list =list(map(','.join, itertools.combinations(v_list, c_len)))
        for a_len in range(len(a_list)) :
            b_list = a_list[a_len].split(',') # 조합
            copy_list = ['alcohol', 'chlorides', 'citric_acid', 'density', 'fixed_acidity', 'free_sulfur_dioxide', 'pH',
                         'residual_sugar', 'sulphates', 'total_sulfur_dioxide', 'volatile_acidity']
            # print(b_list)
            for b in b_list:
                    if b in v_list:
                            copy_list.remove(b)
            # print(copy_list) # copy_list : v_list - 조합
            my_formula = 'quality ~ '
            for idx in range(len(b_list)):
                    if idx != len(b_list) - 1:
                            my_formula = my_formula + b_list[idx] + ' + '
                    else:
                            my_formula = my_formula + b_list[idx]
            print("%s. %s" %(answer_index, my_formula))
            answer_index+=1
            lm = ols(my_formula,data=wine).fit()
            independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'] + copy_list)]