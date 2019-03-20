import pandas as pd
from statsmodels.formula.api import ols
import itertools
import operator
import numpy as np

def more_exe(a, b, c, d, e, f, g, h, i) :
    count_five = 0
    count_ten = 0
    count_twenty = 0

    print("고정변수를 조합해서 정답률을 올려본다222. -> 최적의 공식을 찾아낸다.")
    house = pd.read_csv('Housing.csv', sep=',', header=0)
    house.columns = house.columns.str.replace(' ', '_')
    house['driveway01'] = np.where(house['driveway'] == 'yes', 1, 0)
    house['recroom01'] = np.where(house['recroom'] == 'yes', 1, 0)
    house['fullbase01'] = np.where(house['fullbase'] == 'yes', 1, 0)
    house['gashw01'] = np.where(house['gashw'] == 'yes', 1, 0)
    house['airco01'] = np.where(house['airco'] == 'yes', 1, 0)
    house['prefarea01'] = np.where(house['prefarea'] == 'yes', 1, 0)

    for idx in range(len(house.index)) :
        y_pre = a + house["lotsize"][idx]*b + house["bathrms"][idx]*c + house["stories"][idx]*d + house["driveway01"][idx]*e \
                + house["recroom01"][idx]*f + house["gashw01"][idx]*g + house["airco01"][idx]*h + house["prefarea01"][idx]*i
        if house['-20%Delta'][idx] <= y_pre <= house['+20%Delta'][idx]:
            count_twenty += 1
        if house['-10%Delta'][idx] <= y_pre <= house['+10%Delta'][idx]:
            count_ten += 1
        if house['-5%Delta'][idx] <= y_pre <= house['+5%Delta'][idx]:
            count_five += 1
    answer_five = count_five / len(house) * 100
    answer_ten = count_ten / len(house) * 100
    answer_twenty = count_twenty / len(house) * 100
    print(answer_five)
    print(answer_ten)
    print(answer_twenty)

def main () :
    print("고정변수를 조합해서 정답률을 올려본다. -> 최적의 공식을 찾아낸다.")
    house = pd.read_csv('Housing_except.csv', sep=',', header=0)
    house.columns = house.columns.str.replace(' ', '_')

    house['driveway01'] = np.where(house['driveway'] == 'yes', 1, 0)
    house['recroom01'] = np.where(house['recroom'] == 'yes', 1, 0)
    house['fullbase01'] = np.where(house['fullbase'] == 'yes', 1, 0)
    house['gashw01'] = np.where(house['gashw'] == 'yes', 1, 0)
    house['airco01'] = np.where(house['airco'] == 'yes', 1, 0)
    house['prefarea01'] = np.where(house['prefarea'] == 'yes', 1, 0)
    v_list = ['lotsize', 'bedrooms', 'bathrms', 'stories', 'driveway01', 'recroom01', 'fullbase01', 'gashw01',
              'airco01', 'garagepl', 'prefarea01']

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
            if b_list == ['lotsize', 'bathrms', 'stories', 'driveway01', 'recroom01', 'gashw01', 'airco01', 'prefarea01'] :
                a = lm.params["Intercept"]
                b = lm.params["lotsize"]
                c = lm.params["bathrms"]
                d = lm.params["stories"]
                e = lm.params["driveway01"]
                f = lm.params["recroom01"]
                g = lm.params["gashw01"]
                h = lm.params["airco01"]
                i = lm.params["prefarea01"]
                more_exe(a, b, c, d, e, f, g, h, i)

main()