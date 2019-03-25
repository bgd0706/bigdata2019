# train_test split 하기
import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import numpy as np

house = pd.read_csv('Housing.csv', sep=',', header=0)
house.columns = house.columns.str.replace(' ', '_')

house['driveway01'] = np.where(house['driveway'] == 'yes', 1, 0)
house['recroom01'] = np.where(house['recroom'] == 'yes', 1, 0)
house['fullbase01'] = np.where(house['fullbase'] == 'yes', 1, 0)
house['gashw01'] = np.where(house['gashw'] == 'yes', 1, 0)
house['airco01'] = np.where(house['airco'] == 'yes', 1, 0)
house['prefarea01'] = np.where(house['prefarea'] == 'yes', 1, 0)

house_data = house[["lotsize", "bedrooms", "stories", "driveway01", "recroom01", "gashw01", "airco01", "prefarea01"]]
house_label = house["price"]

data_train, data_test, label_train, label_test = train_test_split(house_data, house_label)

clf = svm.SVC(gamma='auto')
clf.fit(data_train, label_train)
pre = clf.predict(data_test)

count_twenty = 0
for idx in range(len(data_test)) :
    if house_label[idx] - (house_label[idx]*0.2) <= pre[idx] <= house_label[idx] + (house_label[idx]*0.2) :
         count_twenty += 1

print( count_twenty / len(data_test) * 100)