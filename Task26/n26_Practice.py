#26.5

a = open("task26.5_26.txt")
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

print(cP)
