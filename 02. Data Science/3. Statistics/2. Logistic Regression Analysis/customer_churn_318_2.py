# 목적 : 변수별 서로 다른 통계량 구하기
import numpy as np
import pandas as pd

# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]
 # 빅데이터 분석을 위한 데이터 보정

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.) # 원본은 그대로 유지하고 'churn01'열이 생김.
print(churn.groupby(['churn01']).agg({'day_charge' : ['mean', 'std'], 'eve_charge' : ['mean', 'std'], 'night_charge' : ['mean', 'std'],
                                      'intl_charge' : ['mean', 'std'], 'account_length' : ['count', 'min', 'max'],
                                      'custserv_calls' : ['count', 'min', 'max']}))
