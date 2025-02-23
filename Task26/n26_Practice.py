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
a = open('task26.10_26.txt')
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







