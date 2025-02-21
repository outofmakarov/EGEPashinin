#23
'''def f(n):
    num = set()
    for d in range(1,int(n**0.5)+1):
        if n % d == 0:
            if d % 2 != 0:
                num.add(d)
            if (n // d) % 2 != 0:
                num.add(n//d)
    return sorted(num,reverse=True)

for i in range(190061,190081):
    y = f(i)

    if len(y) == 4:

        print(y)'''
# ans:
# [190061, 6131, 31, 1]
# [11879, 1697, 7, 1]
# [190067, 2677, 71, 1]
# [23759, 1033, 23, 1]
# [190073, 14621, 13, 1]
# [95039, 13577, 7, 1]
# [190079, 2837, 67, 1]

#34

'''def f(n):
    num = set()
    for d in range(1,int(n//2) + 1):
        if n % d == 0:
            num.add(d)
            num.add(n//d)
    return sorted(num)

maxD = []
for i in range(586132,586431):
    y = len(f(i))
    maxD.append(y)

maxN = []
for j in range(586132,586431):
    y = len(f(j))
    maxDel = max(maxD)

    if y == maxDel:
        maxN.append(j)

minRes = min(maxN)
lenMinR = len(f(minRes))
p = f(minRes)
maxDminR = [p[-1], p[-2]]

maxRes = max(maxN)
lenMaxR = len(f(maxRes))
p = f(maxRes)
maxDmaxR = [p[-1], p[-2]]

print(lenMinR, maxDminR)
print(lenMaxR, maxDmaxR)'''

#ans:
#80 586224 293112
#80 586320 293160

#64

'''def f(n):
    num = set()
    for d in range(1,int(n//2)+1):
        if n % d == 0:
            num.add(d)
            num.add(n//d)

    return sorted(num)

res = []
for i in range(2532000,2532161):
    y = f(i)
    if len(y) == 2 and i % 10 == 7:
        res.append(i)

for j in range(0,len(res)):
    print(res[j], j + 1)'''

#ans:
# 2532007 1
# 2532067 2
# 2532107 3
# 2532137 4
# 2532157 5

#68

'''def check(n):
    sN = str(n)
    if int(sN[0]) % 2 != 0 and int(sN[1]) % 2 != 0 and int(sN[2]) % 2 == 0 and int(sN[3]) % 2 == 0 and int(sN[4]) % 2 == 0:
        if n % 7 != 0 and n % 9 != 0 and n % 13 != 0:
            return n

res = []
for i in range(57888,74556):
    y = check(i)
    if y != None:
        res.append(y)

print(len(res), max(res) - min(res))'''

#ans: 262 14888

'''def f(n):
    num = set()
    for d in range(2,int(n**0.5)+1):
        if n % d == 0:
            num.add(d)
            num.add(n//d)
    num.add(1)
    return sorted(num)

c = 0
for i in range(2,30001):
    y = f(i)

    if i > sum(y):
        c+=1
print(c)'''

#ans: 22567

#79
'''num = [True]*3577001
num[0] = False
num[1] = False

for i in range(2,3577001):
    if num[i] == True:
        for j in range(i+i, 3577001, i):
            num[j] = False

c = num.count(True)

print(c)'''
#ans: 255203

#93

def check(n):
    sN = str(n)
    if len(sN) == 4:
        if int(sN[0]) % 2 != 0 and int(sN[1]) % 2 != 0 and int(sN[2]) % 2 != 0 and int(sN[3]) % 2 != 0:
            return True
    if len(sN) == 5:
        if int(sN[0]) % 2 != 0 and int(sN[1]) % 2 != 0 and int(sN[2]) % 2 != 0 and int(sN[3]) % 2 != 0 and int(sN[4]) % 2 != 0:
            return True
    return False

res = []
c= 0
for i in range(1686,13277):
    y = check(i)
    if y == True:
        c += sum(map(int,str(i)))

print(c)

#ans: 13950

#103


#108

#127








