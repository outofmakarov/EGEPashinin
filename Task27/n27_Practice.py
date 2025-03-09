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

#ans:
#10738.21226546789 30730.076059078103
#37522.944615707165 51277.95880214987

#27.31
def dist(n,n1):
    x,y = n
    x1,y1 = n1

    l = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5

    return l

a = open("task27.31_27-А.txt")
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

for c in clS:
    print(len(c))
