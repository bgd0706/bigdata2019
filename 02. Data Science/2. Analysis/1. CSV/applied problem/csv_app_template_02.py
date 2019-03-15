import csv
import pandas as pd
import math

data_frame = pd.read_csv("Demographic_Statistics_By_Zip_Code.csv")

def get_csv_row_instance(primary_key):
    Row_instance = data_frame.loc[data_frame['JURISDICTION NAME'].astype(str) == primary_key]
    return Row_instance

def get_csv_col_instance(col_name):
    col_instance = data_frame[col_name].astype(int)
    return col_instance

def My_Sum(data_list):
    My_Sum = data_list.sum()
    return My_Sum

def My_Average(data_list):
    My_Average = data_list.mean()
    return My_Average

def My_Max(data_list):
    My_Max= data_list.max()
    return My_Max

def My_Min(data_list):
    My_Min = data_list.min()
    return My_Min

def My_Deviation(data_list): # 편차 : 표본값 - 평균
    avg = data_list.mean()
    for col in data_list :
        print("%s %s" %(col, col-avg))

def My_Variance(data_list):#분산
    My_Variance = data_list.var()
    return My_Variance

def My_Standard_Deviation(data_list):# 표준편차
    Standard_Deviation = data_list.std()
    return Standard_Deviation

def My_Ascendant(data_list):#오름차순
    data_list.sort()
    print(data_list)
    data_list = map(int, data_list)
    for i in data_list :
        print(i, end=' ')

def My_Descendant(data_list):#내림차순
    data_list.sort(reverse=True)
    data_list = map(int, data_list)
    for i in data_list:
        print(i, end=' ')

def print_row(row_instance):
    print(row_instance)

def print_col(col_instance):
    print(col_instance)

# menu 처리
print("CSV Handle 연습예제 pandas")
while True:
    print("0. 종료 1. 행 2. 열 3. 총합 4. 평균 5. 최대값 6. 최소값 7. 편차 8. 분산 9. 표준편차 10. 오름차순 정렬 11. 내림차순 정렬")
    menu_input = int(input("메뉴를 선택하세요: "))
    if menu_input == 1 :
        primary_number = input("Primary Key를 입력하세요: ")
        print_row(get_csv_row_instance(primary_number))
    elif menu_input == 2 :
        access_key = input("Access Key를 입력하세요: ")
        print_col(get_csv_col_instance(access_key))
    elif menu_input == 3 :
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        print_col(col)
        sum = My_Sum(col)
        print("총합: %s" %sum)
    elif menu_input == 4 :
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        print_col(col)
        avg = My_Average(col)
        print("평균값: %s" %avg)
    elif menu_input == 5 : # 최대값
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        print_col(col)
        max_ = My_Max(col)
        print("최대값: %s" % max_)
    elif menu_input == 6 :
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        print_col(col)
        min_ = My_Min(col)
        print("최대값: %s" % min_)
    elif menu_input == 7 : # 편차
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        print_col(col)
        print("편차 공식 : 표본값 - 평균")
        print("표본 편차")
        dev = My_Deviation(col)
    elif menu_input == 8 : # 분산
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        print_col(col)
        var = My_Variance(col)
        print("분산(Variance) 공식: ∑(표본-평균)**/표본수")
        print("분산: %s" %var)
    elif menu_input == 9 : # 표준편차 : 분산의 제곱근
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        print_col(col)
        stan_dev = My_Standard_Deviation(col)
        print("표준편차(Standard Deviation) 공식: √분산")
        print("표준편차: %s" % stan_dev)
    elif menu_input == 10 : # 오름차순
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        My_Ascendant(col)
    elif menu_input == 11 : # 내림차순
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        My_Descendant(col)

