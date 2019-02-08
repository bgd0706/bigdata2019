f = open("sample.txt", 'r')
lines = f.readlines()
f.close()

total = 0
for line in lines :
    score = int(line)
    total += score

average = total / lines.__len__()

f = open("result.txt", 'w')
f.write(str(average))
f.close()