count = 1;
for i in range(11, 10001) :
    i = str(i)
    for j in range(len(i)) :
        if i[j] == '8' : count+=1
print(count)

print(str(list(range(1, 2001))).count('8'))