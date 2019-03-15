# 목적 : 그룹별 기술통계 구하기
import numpy as np
import pandas as pd

# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]
 # 빅데이터 분석을 위한 데이터 보정

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.) # 원본은 그대로 유지하고 'churn01'열이 생김.
print(churn.groupby(['churn'])[ # 행을 기준
    ['day_charge', 'eve_charge', 'night_charge', 'intl_charge', 'account_length', 'custserv_calls']].agg(['count','mean', 'std']))
    # 보고싶은 필드영역.agg(보고싶은 통계계)
pass