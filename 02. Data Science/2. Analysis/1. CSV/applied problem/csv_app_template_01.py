import csv
import math

def get_csv_row_instance(primary_key):
    Row_instance=[]
    for row in data :
        if primary_key == str(row[0]) :
            for r in row :
                Row_instance.append(r)
    return Row_instance

def get_csv_col_instance(col_name):
    col_instance=[]
    header = data[0]
    my_col_index = []
    for index_value in range(len(header)) :
        if header[index_value] == col_name :
            my_col_index.append(index_value)
            break # 1개만 받으므로
    count = 0
    for column in data :
        count += 1
        if count == 1 : continue
        for index_value in my_col_index :
            col_instance.append(column[index_value])
    return col_instance

def Convert_Type(col_instance):
    for col in range(len(col_instance)) :
        col_instance[col] = int(col_instance[col])
    return col_instance

def My_Sum(data_list):
    My_Sum=0
    for data in data_list :
        My_Sum += data
    return My_Sum

def My_Average(data_list):
    My_Average = My_Sum(data_list) / len(data_list)
    return My_Average

def My_Max(data_list):
    My_Max=max(data_list)
    return My_Max

def My_Min(data_list):
    My_Min = min(data_list)
    return My_Min

def My_Deviation(data_list): # 편차 : 표본값 - 평균
    avg = My_Average(data_list)
    for col in data_list :
        print("%s %s" %(col, col-avg))

def My_Variance(data_list):#분산
    var_sum = 0
    avg = My_Average(data_list)
    for col in data_list :
        var_sum +=(col-avg)**2
    My_Variance = var_sum / len(data_list)
    return My_Variance

def My_Standard_Deviation(data_list):# 표준편차
    var = My_Variance(data_list)
    Standard_Deviation= math.sqrt(var)
    return Standard_Deviation

def My_Ascendant(data_list):#오름차순
    data_list.sort()
    data_list = map(int, data_list)
    for i in data_list :
        print(i, end=' ')

def My_Descendant(data_list):#내림차순
    data_list.sort(reverse=True)
    data_list = map(int, data_list)
    for i in data_list:
        print(i, end=' ')

def print_row(row_instance):
    print(" ".join(row_instance))

def print_col(col_instance):
    print("\n".join(col_instance))
    pass

with open('Demographic_Statistics_By_Zip_Code.csv',newline='') as infile:
    data=list(csv.reader(infile))

# menu 처리
print("CSV Handle 연습예제")
while True:
    print("0. 종료 1. 행 2. 열 3. 총합 4. 평균 5. 최대값 6. 최소값 7. 편차 8. 분산 9. 표준편차 10. 오름차순 정렬 11. 내림차순 정렬")
    menu_input = int(input("메뉴를 선택하세요: "))
    if menu_input == 1 :
        primary_key = input("Primary Key를 입력하세요: ")
        print_row(get_csv_row_instance(primary_key))
    elif menu_input == 2 :
        access_key = input("Access Key를 입력하세요: ")
        print_col(get_csv_col_instance(access_key))
    elif menu_input == 3 :
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        print_col(col)
        sum = My_Sum(Convert_Type(col))
        print("총합: %s" %sum)
    elif menu_input == 4 :
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        print_col(col)
        avg = My_Average(Convert_Type(col))
        print("평균값: %s" %avg)
    elif menu_input == 5 : # 최대값
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        print_col(col)
        max_ = My_Max(Convert_Type(col))
        print("최대값: %s" % max_)
    elif menu_input == 6 :
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        print_col(col)
        min_ = My_Min(Convert_Type(col))
        print("최대값: %s" % min_)
    elif menu_input == 7 : # 편차
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        print_col(col)
        print("편차 공식 : 표본값 - 평균")
        print("표본 편차")
        dev = My_Deviation(Convert_Type(col))
    elif menu_input == 8 : # 분산
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        print_col(col)
        var = My_Variance(Convert_Type(col))
        print("분산(Variance) 공식: ∑(표본-평균)**/표본수")
        print("분산: %s" %var)
    elif menu_input == 9 : # 표준편차 : 분산의 제곱근
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        print_col(col)
        stan_dev = My_Standard_Deviation(Convert_Type(col))
        print("표준편차(Standard Deviation) 공식: √분산")
        print("표준편차: %s" % stan_dev)
    elif menu_input == 10 :
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        My_Ascendant(Convert_Type(col))
    elif menu_input == 11 :
        access_key = input("Access Key를 입력하세요: ")
        col = get_csv_col_instance(access_key)
        My_Descendant(Convert_Type(col))