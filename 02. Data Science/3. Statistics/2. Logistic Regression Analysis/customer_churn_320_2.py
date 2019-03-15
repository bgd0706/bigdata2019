# 목적 : 피벗테이블 만들기
import pandas as pd

# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]
 # 빅데이터 분석을 위한 데이터 보정

churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + churn['night_charge'] + churn['intl_charge']

print("Debug] churn.pivot_table(['total_charges'], index=['churn', 'custserv_calls']))")
print(churn.pivot_table(['total_charges'], index=['churn', 'custserv_calls']))

print("\n\nDebug] churn.pivot_table(['total_charges'], index=['churn'], columns=['custserv_calls']))")
print(churn.pivot_table(['total_charges'], index=['churn'], columns=['custserv_calls']))

print("\nDebug] churn.pivot_table(['total_charges'], index=['custserv_calls'], columns=['churn'], aggfunc='mean', fill_value='NaN', margins=True))")
print(churn.pivot_table(['total_charges'], index=['custserv_calls'], columns=['churn'], aggfunc='mean', fill_value='NaN', margins=True))
