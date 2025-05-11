#9.10
from collections import Counter
from itertools import count

'''a = open("n910")
data = []
c = 0
for line in a:
    line = line.split()
    line = [int(i) for i in line]

    #res = [line.count(line[0]),line.count(line[1]),line.count(line[2]),line.count(line[3]),line.count(line[4]),line.count(line[5])]
    counterLine = Counter(line)
    res = list(Counter(line).values())


    if res.count(1) == 4 and res.count(2) == 1:
        repSum = 0
        nonRepSum = 0
#       for i in range(len(res)):
#           if res[i] == 1:
#               nonRepSum += line[i]
#           if res[i] == 2:
#               repSum+= line[i]
        for key in counterLine:
            if counterLine[key] == 1:
                nonRepSum+=key
            else:
                repSum+= key*2
        if nonRepSum / 4 <= repSum:
            c+=1

print(c)'''

#ans: 2241

'''a = open("911")
c = 0

for line in a:
    line = line.split()
    line = [int(i) for i in line]

    res = [line.count(i) for i in line]

    if res.count(2) == 4 and res.count(1) == 3:
        repSum = 0
        allSum = sumAbc(line)

        for i in range(len(res)):
            if res[i] == 2:
                repSum += line[i]

        if repSum/4 < allSum / 7:
            c+=1
print(c)'''

#ans 83

#9.12
'''a = open("912")
c = 0

for line in a:
    line = line.split()
    line = [int(i) for i in line]
    res = [line.count(i) for i in line]

    if res.count(3) == 3 and res.count(1) == 3:
        repSum = 0
        nonRepSum = 0
        for i in range(len(line)):
            if res[i] == 3:
                repSum += line[i]
            else:
                nonRepSum += line[i]
        if repSum**2 > nonRepSum**2:
            c+=1
print(c)'''

#ans 273

a = open("91X")
c = 0

for line in a:
    line = line.split()
    line = [int(i) for i in line]
    res = [line.count(j) for j in line]

    if res.count(3) == 3 and res.count(1) == 3:
        repS = 0
        nonRepS = 0

        for i in range(len(line)):
            if res[i] == 3:
                repS += line[i]
            else:
                nonRepS += line[i]

        if repS**2 > nonRepS**2:
            c+=1

print(c)