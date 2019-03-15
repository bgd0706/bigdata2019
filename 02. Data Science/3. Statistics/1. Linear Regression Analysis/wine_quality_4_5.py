# 목적 : 선형회귀(Linear Regression) 분석
import pandas as pd
from statsmodels.formula.api import ols
# https://datascienceschool.net/view-notebook/58269d7f52bd49879965cdc4721da42d/ : statsmodels 패키지를 사용한 선형 회귀분석

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar +' \
              'sulphates + total_sulfur_dioxide + volatile_acidity'
lm = ols(my_formula, data=wine).fit()
# ols(y, X)
# fit() : 별도의 RegressionResults 클래스 객체로 출력하게 하는 메서드 -> 함수를 만들어주는 함수
print("< lm.summary() >")
print(lm.summary()) # summary() : 결과 리포트를 보여주는 메서드

print("="*80+"\n")
print("\nQuantities you can extract from the result:\n%s" %dir(lm))
print("\nCoefficients:\n%s" %lm.params)
print("\nCoefficient Std Errors:\n%s" %lm.bse)
print("\nAdj. R-squared:\n%.2f" %lm.rsquared_adj)
print("\nF-statistic: %.1f  P-value: %.2f" %(lm.fvalue, lm.f_pvalue))
print("\nNumber of obs: %d  Number of fitted values: %s" %(lm.nobs, len(lm.fittedvalues)))