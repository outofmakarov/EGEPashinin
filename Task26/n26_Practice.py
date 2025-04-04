#26.5

'''a = open("task26.5_26.txt")
n = int(a.readline())

num = []
num2 = set()
for s in a:
    num.append(int(s))
    num2.add(int(s))
    #s = int(s)
    #if s % 2 == 0:
    #    num.append(s)
cP = 0
for i in range(0,len(num)):
    for j in range(i+1,len(num)):
        if num[i] % 2 ==0 and num[j] % 2 == 0:
            aver = (num[i] + num[j]) // 2
            if aver in num2:
                cP+=1

print(cP)'''

#ans: 15

#26.6
'''a = open('task26.6_26.txt')
num = [int(i) for i in a]
num.sort()


averN = []
for i in range(0,len(num)):
    for j in range(i+1, len(num)):
        averN.append((num[i] +num[j]) / 2)

averN.sort()

k = 0
ck = 0
c = 0

for n in averN:

    while k < len(num) and num[k] < n:
        k+=1

    if k % 100 == 0 and k != 0:
        ck = k
        c+=1


print(c,ck)'''
 #ans: 4885 900

#26.10
'''a = open('task26.10_26.txt')
nID = int(a.readline())
sMo = int(nID * 0.25)

sBad = []
sCool = []

for line in a:
    num = [int(i) for i in line.split()]
    sID = num[0]
    sPo = num[1:]
    if 2 in sPo:
        if sPo.count(2) > 2:
            sBad.append((sID,sum(sPo)))
    else:
        sPo = sum(num[1:])
        sCool.append((sID,sPo))

sCool.sort(key= lambda x: (-x[1],x[0]))
sLucky = sCool[sMo-1]

sBad.sort(key= lambda x: (-x[1],x[0]))
sUnLuck = sBad[0]

print(sLucky[0],sUnLuck[0])

#ans: 52326 635


#26.8
a = open("task26.8_26.txt")
data = a.readline()

d = {}
d[1634515200] = 0
d[1634515200+60*60*24*7] = 0


for line in a:
    time = [int(i) for i in line.split()]
    timeS = time[0]
    timeE = time[1]

    if timeE == 0:
        timeE = 99999999999999999999999999999999

    if timeS in d:
        d[timeS] +=1
    else:
        d[timeS] =1

    if timeE in d:
        d[timeE] -=1
    else:
        d[timeE] = -1

actPr = 0
actMax = 0
t1 = 0
duration = 0
durationTotal = 0
for t in sorted(d.keys()):
    actPr += d[t]

    if  1634515200 <= t <= 1634515200+60*60*24*7:
        if actPr > actMax:
            actMax = actPr
            duration = 0

        elif actPr == actMax:
            duration += t - t1
            
        t1 = t

print(actMax,duration)

#ans: 7768 20'''




