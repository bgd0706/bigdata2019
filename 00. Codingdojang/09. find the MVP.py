import math

a = []
b = []
for i in range(0, 5) :
    a.append(i)
    a[i] = input().split('/')
for i in range(0, 5) :
    b.append(i)
    b[i] = input().split('/')

a_list = list(map(lambda x:(int(x[0])*2 + int(x[2])*1)/int(x[1]), a))
b_list = list(map(lambda x:(int(x[0])*2 + int(x[2])*1)/int(x[1]), b))
a_max = float(max(list(map(lambda x:(int(x[0])*2 + int(x[2])*1)/int(x[1]), a))))
b_max = float(max(list(map(lambda x:(int(x[0])*2 + int(x[2])*1)/int(x[1]), b))))

if (a_max > b_max) :
    print("max : a%s " % (a_list.index(a_max) + 1))
else :
    print("max : b%s " % (b_list.index(b_max) + 1))

