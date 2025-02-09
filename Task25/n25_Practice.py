#25.1
from fnmatch import fnmatch
from itertools import product
'''for i in range(0,10**10,2023):
    if fnmatch(str(i), "1?2139*4"):
        print(i, i// 2023)'''

#25.2
'''nums = []
pat = "1?2139*4"

for i in range(10):
    newPat = pat.replace("?", str(i), 1)

    for lenN in range(1,6):
        for j in product("0123456789", repeat=lenN):
            numStr = newPat.replace("*", "".join(j), 1)
            num = int(numStr)

            if num % 103 == 0:
                nums.append(num)

print(len(nums), max(nums) // 103)'''

#25.3
def deli(n):
    num = set()
    d = 1
    while d**2 <= n:
        if n % d == 0:
            num.add(d)
            num.add(n//d)
        d+=1
    return num

'''resN = []
for x in range(int(10**4.5), 10**5):
    y = x**2
    c = sorted(deli(y))
    if len(c) == 45 and fnmatch(str(y), "1*2*7*04"):
        resN.append((y, c[-2]))
        if len(resN) == 5:
            print(resN)
            break'''

#ans: [(1027330704, 513665352), (1132457104, 566228552), (1242703504, 621351752), (1271065104, 635532552), (1328748304, 664374152)]

#25.6
'''resN = []
for x in range(700_000, 1_000_000):
    y = sorted(deli(x))
    m = str(y[1] + y[-2])

    if m[-1] == "8" and len(y) > 2:
        resN.append((x,m))

        if len(resN) == 5:
            print(resN)
            break'''

#25.7
'''resN = set()
for m in range(0,50):
    for n in range(0,50):
        if m % 2 == 0 and n % 2 == 1:
            if 2**m * 3**n in range(150_000_000,300_000_001):
               resN.add((2**m * 3**n, n+m))

print(resN)'''

#25.12

def check(n):
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            return False
        d += 1
    return True

num = [True]*10**7
num[0] = False
num[1] = False
c = 0
av = 0
for i in range(2,10**7):
    if num[i]:
        for j in range(i+i,10**7, i):
            num[j] = False

for i in range(3_000_000,10**7-2):
    if num[i] == num[i+2] and num[i] == True:
        c+=1
        av = (i + i+2) //2

print(c,av)














