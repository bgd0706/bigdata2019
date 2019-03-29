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
    a_list =list(map(','.join, itertools.combinations(v_list, c_len))) # 독립(고정)변수의 최적의 조합 찾기 위해
    for a_len in range(len(a_list)) :
        b_list = a_list[a_len].split(',') # 조합
        my_formula = 'quality ~ ' # 종속변수
        for idx in range(len(b_list)):
            if idx != len(b_list) - 1:
                    my_formula = my_formula + b_list[idx] + ' + '
            else:
                    my_formula = my_formula + b_list[idx]
        lm = ols(my_formula,data=wine).fit() # 선형회귀함수 생성

        independent_variables = wine[b_list] # 독립(고정)변수를 각각의 조합 리스트로 설정
        new_observations = wine.loc[wine.index, independent_variables.columns] # 독립변수로 설정된 열 가지고오기
        y_predicted = lm.predict(new_observations) # 예측된 값 설정
        y_predicted_rounded = [round(score) for score in y_predicted]

        count = 0
        for idx in range(len(wine.index)) :
            if wine['quality'][idx] == y_predicted_rounded[idx] : # 실제 quality값과 예측값을 비교
                count += 1
        answer_dict[(',').join(b_list)] = count / len(wine) * 100

sortedList = sorted(answer_dict.items(), key=operator.itemgetter(1), reverse=True)
print(sortedList[0])