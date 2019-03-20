import pandas as pd
from statsmodels.formula.api import ols
import itertools
import operator
import numpy as np

print("고정변수를 조합해서 정답률을 올려본다. -> 최적의 공식을 찾아낸다.")
house = pd.read_csv('Housing.csv', sep=',', header=0)
house.columns = house.columns.str.replace(' ', '_')

house['driveway01'] = np.where(house['driveway'] == 'yes', 1, 0)
house['recroom01'] = np.where(house['recroom'] == 'yes', 1, 0)
house['fullbase01'] = np.where(house['fullbase'] == 'yes', 1, 0)
house['gashw01'] = np.where(house['gashw'] == 'yes', 1, 0)
house['airco01'] = np.where(house['airco'] == 'yes', 1, 0)
house['prefarea01'] = np.where(house['prefarea'] == 'yes', 1, 0)
v_list = ['lotsize', 'bedrooms', 'bathrms', 'stories', 'driveway01', 'recroom01', 'fullbase01', 'gashw01',
          'airco01', 'garagepl', 'prefarea01']

answer_dict_five = {}
answer_dict_ten = {}
answer_dict_twenty = {}

for c_len in range(1, len(v_list)+1) :
    a_list =list(map(','.join, itertools.combinations(v_list, c_len)))
    for a_len in range(len(a_list)) :
        b_list = a_list[a_len].split(',') # 조합
        my_formula = 'price ~ '
        for idx in range(len(b_list)):
            if idx != len(b_list) - 1:
                    my_formula = my_formula + b_list[idx] + ' + '
            else:
                    my_formula = my_formula + b_list[idx]
        lm = ols(my_formula,data=house).fit()

        independent_variables = house[b_list]
        new_observations = house.loc[house.index, independent_variables.columns]
        y_predicted = lm.predict(new_observations)
        y_predicted_rounded = [round(score) for score in y_predicted]

        count_five = 0
        count_ten = 0
        count_twenty = 0
        for idx in range(len(house.index)) :
            if house['-20%Delta'][idx] <= y_predicted_rounded[idx] <= house['+20%Delta'][idx] :
                count_twenty += 1
            if house['-10%Delta'][idx] <= y_predicted_rounded[idx] <= house['+10%Delta'][idx] :
                count_ten += 1
            if house['-5%Delta'][idx] <= y_predicted_rounded[idx] <= house['+5%Delta'][idx] :
                count_five += 1

        answer_dict_five[(',').join(b_list)] = count_five / len(house) * 100
        answer_dict_ten[(',').join(b_list)] = count_ten / len(house) * 100
        answer_dict_twenty[(',').join(b_list)] = count_twenty / len(house) * 100

sortedList_five = sorted(answer_dict_five.items(), key=operator.itemgetter(1), reverse=True)
sortedList_ten = sorted(answer_dict_ten.items(), key=operator.itemgetter(1), reverse=True)
sortedList_twenty = sorted(answer_dict_twenty.items(), key=operator.itemgetter(1), reverse=True)

print(sortedList_five)
print(sortedList_ten)
print(sortedList_twenty)