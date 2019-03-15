# 목적 : intl_plan과 vmail_plan 열에 대한 이진형 지시변수를 만들고 churn 열과 병합하여 새로운 데이터 프레임을 생성하기
import numpy as np
import pandas as pd

# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]
 # 빅데이터 분석을 위한 데이터 보정

intl_dummies = pd.get_dummies(churn['intl_plan'], prefix='intl_plan')
vmail_dummies = pd.get_dummies(churn['vmail_plan'], prefix='vmail_plan')
churn_with_dummies = churn[['churn']].join([intl_dummies, vmail_dummies])
print(churn_with_dummies.head())