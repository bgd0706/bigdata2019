import pandas as pd
from statsmodels.formula.api import ols

print("전체 데이터를 Test data로 활용하여 정답률을 구한다.")
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar +' \
              'sulphates + total_sulfur_dioxide + volatile_acidity'
lm = ols(my_formula, data=wine).fit()

dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]

new_observations = wine.loc[wine.index, independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]

count = 0
for idx in range(len(wine.index)) :
    if wine['quality'][idx] == y_predicted_rounded[idx] :
        count += 1

print( (count / len(wine)) * 100)

print("고정변수를 조합해서 정답률을 올려본다. -> 최적의 공식을 찾아낸다.")