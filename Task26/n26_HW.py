#25

#ans: 27700 7896

#37

#ans: 5931 800

#46

'''a = open("26-46.txt")
data = a.readline()
num = [int(i) for i in a]

mTh = 0
mN = 34567890098
for i in range(len(num)):
    for j in range(i+1, len(num)):
        for k in range(j+1, len(num)):

            a = num[i]
            b = num[j]
            c = num[k]
            sum = a+b+c
            if sum % 3 == 0:
                aver = sum // 3
                if aver in num:
                    mTh+=1
                    if aver < mN:
                        mN = aver
print(mTh,mN)'''

#ans: 36 34495210

#49
'''a = open("26-49.txt")
data = a.readline()
num = [int(i) for i in a]
num.sort()
mid = num[len(num) // 2]

c = 0
mN = 0
for i in range(len(num)):
    for j in range(i+1, len(num)):
        a = num[i]
        b = num[j]
        sum = a + b

        if sum % 2 == 0:
            aver = sum / 2
            if aver < mid:
                c+=1
                if aver > mN:
                    mN = aver
print(c,mN)'''

# 3184429 56263918

#59


#90
a = open("26-90.txt")
data = a.readline()

num = [int(i) for i in a]

numSort = sorted(num)
expectedSum = 0


