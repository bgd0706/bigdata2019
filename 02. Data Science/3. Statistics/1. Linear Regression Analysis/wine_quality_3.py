# 목적 : 상관관계 분석
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt # Matplotlib : 파이썬에서 자료를 차트나 플롯으로 시각화하는 패키지

def take_sample(data_frame) :
    return data_frame.loc[np.random.choice(data_frame.index, replace=False, size=200)]
    # size가 200개로 리턴하되, 랜덤으로 200개 추출

# Read the data set into a pandas DataFrame
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

print("< 모든 변수 쌍 사이의 상관계수 구하기 >") # 참고 : https://gomguard.tistory.com/173?category=723424
print(wine.corr())

reds = wine.loc[wine['type'] == 'red', :] # type 칼럼명이 red인 행을 필터링
whites = wine.loc[wine['type'] == 'white', :] # type 칼럼명이 white인 행을 필터링
reds_sample = take_sample(wine.loc[wine['type']=='red', :])
whites_sample = take_sample(wine.loc[wine['type']=='white', :])
wine_sample = pd.concat([reds_sample, whites_sample]) # reds_sample, whites_sample을 합친다.
wine['in_sample'] = np.where(wine.index.isin(wine_sample.index), 1., 0.)
 # 배열을 사용한 데이터 처리
 # np.where(조건, x, y) : 조건이 참이면 x의 원소를, 거짓이면 y의 원소로 하는 벡터를 반환

print("\nprint: wine['in_sample']")
print(wine['in_sample'])
print("\nprint: pd.crosstab(wine.in_sample, wine.type, margins=True)")
print(pd.crosstab(wine.in_sample, wine.type, margins=True)) # 1번째 인자별로 그룹화하여 2번째 인자값들을 보여주는 것!

sns.set_style("dark") # 틱 스타일을 dark로 한다.
g = sns.pairplot(wine_sample, kind='reg', plot_kws={"ci":False, "x_jitter": 0.25, "y_jitter": 0.25},
                 hue='type', diag_kind='hist', diag_kws={"bins":10, "alpha":1.0}, palette=dict(red="red", white="white"),
                 markers=["o", "s"], vars=['quality', 'alcohol', 'residual_sugar'])
print("print: g")
print(g)
plt.suptitle('Histograms and Scatter Plots of Quality, Alcohol, and Residual Sugar', fontsize=14, horizontalalignment='center',
             verticalalignment='top', x=0.5, y=0.999)
plt.show()

# https://datascienceschool.net/view-notebook/4c2d5ff1caab4b21a708cc662137bc65/ : Seaborn 함수
# https://datascienceschool.net/view-notebook/d0b1637803754bb083b5722c9f2209d0/ : Matplotlib 소개