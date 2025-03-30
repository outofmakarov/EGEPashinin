#27.28

#1
'''def center(num):
    mS = 234567823456789
    mPos = 0
    for i in range(len(num)):
        x,y = num[i]
        sum = 0
        for j in range(len(num)):
            x1,y1 = num[j]
            l = ((x-x1)**2 + (y - y1)**2)**0.5
            sum+=l

        if sum < mS:
            mS = sum
            mPos = (x,y)

    return mPos



a = open("task27.28_27-А.txt")
skip = a.readline()
data = []

for line in a:
    line = line.replace(",",'.')
    num = line.split()
    num = list(map(float,num))
    a,b = num
    data.append((a,b))

cl1 = []
cl2 = []
for i in range(len(data)):
    x,y = data[i]
    if x < 1.111 and y < 3:
        cl1.append((x,y))
    else:
        cl2.append((x,y))

cent1 = center(cl1)
a,b = cent1

cent2 = center(cl2)
c,d = cent2

Px = ((a+c)/2)*10_000
Py = ((b+d)/2)*10_000

print(Px,Py)

#2

def center3(num):
    mSum = 12345678909876543
    pos = 0
    for i in range(len(num)):
        x,y = num[i]
        sum = 0
        for j in range(len(num)):
            x1,y1 = num[j]
            l = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
            sum+=l

        if sum < mSum:
            mSum = sum
            pos = (x,y)

    return pos


a = open("task27.28_27-Б.txt")
skip = a.readline()
data = []

cl1 = []
cl2 = []
cl3 = []

for line in a:
    line = line.replace(",",".")
    x,y = map(float, line.split())
    data.append((x,y))

    if y< 2.857:
        cl1.append((x,y))
    elif 2.857 < y < 7.143:
        cl2.append((x,y))
    else:
        cl3.append((x,y))

a,b = center3(cl1)
c,d = center3(cl2)
e,f = center3(cl3)

Px = ((a+c+e)/3) * 10_000
Py = ((b+d+f)/3) * 10_000

print(Px,Py)'''

from re import split

#ans:
#10738.21226546789 30730.076059078103
#37522.944615707165 51277.95880214987

#27.31
'''def center(num):
    sM = 2345678904876198756
    sPos = 0
    for x,y in num:
        sum = 0
        for x1,y1 in num:
            l = ((x - x1)**2 + (y-y1)**2)**0.5
            sum+=l

        if sum < sM:
            sPos = x,y
            sM = sum

    return sPos

def dist(n,n1):
    x,y = n
    x1,y1 = n1

    l = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5

    return l

a = open("task27.31_27-Б.txt")
data = []

for line in a:
    line = line.replace(',','.')
    x,y = list(map(float,line.split()))
    data.append((x,y))

clS = []
while data:
    cl1 = []
    q = [data.pop()]

    while q:
        p0 = q.pop()
        cl1.append(p0)

        for p in data:
            if dist(p0,p) < 0.6:
                q.append(p)
                data.remove(p)

    clS.append(cl1)


sumX = 0
sumY = 0
for c in clS[:3]:
    print(len(c))
    cent = center(c)
    sumX += cent[0]
    sumY += cent[1]
    print(center(c))

print(sumX * 100000 // 3,sumY * 100000 // 3)'''

#27.
'''def center(num):
    sM = 345678923456789
    sPos = 0
    for i in num:
        sum = 0
        x,y = i
        for j in num:
            x1,y1 = j
            l = ((y1-y)**2+(x-x1)**2)**0.5
            sum+=l

        if sum < sM:
            sM = sum
            sPos = x,y

    return sPos

def dist(n,n1):
    x,y = n
    x1,y1 = n1

    l = ((x - x1)**2 + (y - y1)**2)**0.5

    return l


a = open("task27.32_27-А.txt")
data = []

for line in a:
    line = line.replace(",",".")
    x,y = list(map(float,line.split()))
    data.append((x,y))

clS = []
while data:
    cl = []
    q = [data.pop()]
    while q:
        p0 = q.pop()
        cl.append(p0)

        for p in data:
            if dist(p0,p) < 0.3:
                q.append(p)
                data.remove(p)
    clS.append(cl)

cl1 = clS[0]
cl2 = clS[1] + clS[2]

cent1 = center(cl1)
cent2 = center(cl2)

xP = int((cent1[0] + cent2[0])/2 * 10000)
yP = int((cent1[1] + cent2[1])/2 * 10000)

print(xP,yP)'''
#ans 13138 60632
'''def center(num):
    sM = 234567898765432
    sPos = 0
    for x,y in num:
        sum = 0
        for x1,y1 in num:
            l = ((y1-y)**2+(x-x1)**2)**0.5
            sum+=l

        if sum < sM:
            sM = sum
            sPos = x,y
    return sPos

def dist(n,n1):
    x,y = n
    x1,y1 = n1

    l = ((y1 - y) ** 2 + (x - x1) ** 2) ** 0.5

    return l

a = open("task27.32_27-Б.txt")
data = []

for line in a:
    line = line.replace(',','.')
    x,y = list(map(float,line.split()))
    data.append((x,y))

clS = []

while data:
    cl = []
    q = [data.pop()]
    while q:
        p0 = q.pop()
        cl.append(p0)

        for p in data:
            if dist(p0,p) < 0.2:
                q.append(p)
                data.remove(p)

    clS.append(cl)

cl1 = clS[0] + clS[-1]
cl2 = clS[1]
cl3 = clS[2]
cl4 = clS[3] + clS[4]

clS = [cl1,cl2,cl3,cl4]
xP = 0
yP = 0
for c in clS:
    cent = center(c)
    xP += cent[0]
    yP += cent[1]

xP = int(xP/4 * 10000)
yP = int(yP/4 * 10000)

print(xP,yP)
'''
#ans: 19014 40843

#27,29

'''def social(n,data):
    x,y = n
    c = -1  # убираем себя, как соседа
    for x1,y1 in data:
        l = ((x-x1)**2 + (y-y1)**2)**0.5
        if l <= 0.1:
            c+=1

    return c >= 14

a = open("task27.29_27-A.txt")
data = []
for line in a:
    x,y = map(float, line.split())
    data.append((x,y))

cl = [
    [ [],[],[] ],
    [ [],[],[] ],
    [ [],[],[] ]
    ]

for x,y in data:
    cl[int(y)][int(x)].append((x,y))

for row in cl:
    for line in row:
        print(len(line), end=' ')
    print()
    #res = перевёрнутая таблица

cl1 = cl[1][1]
cl2 = cl[1][2]

cl12Soc = 0
for x,y in cl1 + cl2:
    if social((x,y),data):
        cl12Soc+=1

celCls = len(cl1) + len(cl2)
K = celCls - cl12Soc
print(cl12Soc,K)'''
#ans: 104 453

#27.30
a = open("task27.30_27-A.txt")
skip = a.readline()
data = set()
#4,5,8

for line in a:

    line = line.split(";")
    num = line[:]

    num.pop(4)  #-минЗП
    num.pop(4)  #-максЗП

    stat = True

    for x in num:
        if x == "":
            stat = False

    if stat == False:
        continue


    aver = 0
    minS = line[4]
    maxS = line[5]
    lang = line[8]



    if minS and maxS:
        minS = int(minS)
        maxS = int(maxS)
        if minS > maxS:
            continue
        aver = (maxS + minS)/2

    elif maxS:
        maxS = int(maxS)
        aver = maxS
    elif minS:
        minS = int(minS)
        aver = minS

    line.append(aver)
    line = tuple(line)  #переводим из массива в кортеж, т.к. кортеж имеет хэш, требуемый set

    data.add(line)

db = [
    [],
    [],
    [],
    [],
    []
]












