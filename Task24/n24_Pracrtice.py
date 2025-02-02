#24.1
from mimetypes import knownfiles

a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\task24.1_24.txt")
a = a.read()


c=0
c1 = 0
for i in range(0,len(a)):
    if a[i] == "C":
        c+=1
        if c > c1:
            c1 = c
    else:
        c=0
print(c1)

#24.2

a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\task24.2_24.txt")
a = a.read()

c=0
c1 = 0
for i in range(0,len(a)):
    if a[i] in "ABCD":
        c+=1
        if c > c1:
            c1 = c
    else:
        c=0
print(c1)

#24.3


a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\task24.3_24.txt")
a = a.read()

#a = "XYZZXYZ"

c=1
c1 = 0
for i in range(0,len(a)-1):
    if a[i] != a[i+1]:
        c+=1
        if c > c1:
            c1 = c
    else:
        c=1
print(c1)

#24.4

'''s = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\task24.4_24.txt")
s = s.readline()


s = (s.replace('O', 'A').replace('C', 'D').replace('F', 'D').replace('DA', '*')
     .replace('D', 'A'))
print(max([len(x) for x in s.split('A')]))
#a = a.replace("SG","*")

c=0
c1 = 0
for i in range(0,len(s)):
    if s[i] == "*":
        c+=1
        if c > c1:
            c1 = c
    else:
        c=0
print(c1)'''

#24.5

'''a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\task24.5_24.txt")
a = a.read()

numL = []
numN = []
c = 1
numL.append(a[0])
numN.append(c)

for i in range(1,len(a)):
    if a[i] != a[i-1]:
        numL.append(a[i])
        numN.append(1)
    else:
        numN[-1] +=1

maxL = 0
for i in range(0,len(numL)-2):
    if numL[i+2] > numL[i+1] > numL[i]:
        curL = numN[i] + numN[i+1] + numN[i+2]
        if curL > maxL:
            maxL = curL

print(maxL)'''

#24.6

'''a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\task24.6_24.txt")
a = a.read()

numT = []
for i in range(0,len(a)):
    if a[i] == "T":
        numT.append(i)


maxL = max(numT[100], len(a[numT[-100] +1:]))

for i in range(0,len(numT)-101):
    st = numT[i]
    end = numT[i+101]

    curL = end - st - 1

    if curL > maxL:
        maxL = curL


print(maxL, st,end)'''

#24.8

'''a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\task24.8_24.txt")
a = a.read()

d = {}
for i in range(0,len(a)-2):
    if a[i] == a[i+2]:
        if a[i+1] in d:
            d[a[i+1]] +=1
        else:
            d[a[i+1]] = 1

maxV = max(d.values())

for k in d:
    if d[k] == maxV:
        maxL = k

print(maxL, max(d.values()))

#24.9

from collections import Counter
a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\task24.9_24.txt")
x = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\task24.9_24.txt").read()
a = a.readlines()


def fMaxL(a):
    c = 1
    c1 = 1
    for i in range(0, len(a)-1):
        if a[i] == a[i+1]:
            c+=1
            if c > c1:
                c1 = c
        else:
            c = 1

    return c1

n = 1
nStr = ""
for s in a:
    if fMaxL(s) > n:
        n = fMaxL(s)
        nStr = s

c = Counter(nStr)
maxNStr = max(c.values())
numFL = []
for k in c:
    if c[k] == maxNStr:
        numFL.append(k)

numFL.sort()
x = x.count(numFL[0])
print(numFL[0],x)

#24.10
import re

a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\task24.10_24.txt")
a = a.read()
a = a.replace("*","-")
mx = 0
for m in re.findall("(([1-9][0-9]*)(-([1-9][0-9]*))*)", a):
    mx = max(mx,len(m[0]))
print(mx)'''

#24.12
a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\task24.12_24.txt")
a = a.read()

numAF = []
minL = 2**50
for i in range(0,len(a)-1):
    if a[i] == "A" and a[i+1] == "F":
        numAF.append(i)

for j in range(0,len(numAF)-200):
    st = numAF[j]
    f = numAF[j+200]
    l = f - st + 2
    if l < minL:
        minL = l
print(minL)







