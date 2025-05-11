a = open("17_21712.txt")

mIf = 0
data = [int(i) for i in a]
cRes = 0
sumUp = 0
mUp = 234567890777

for n in data:
    if n > 999 and (len(str(n)) == 4 and n % 10 == 6):
        if n < mUp:
            mUp = n


print(mUp)

for i in range(len(data)-2):
    a = data[i]
    b = data[i+1]
    c = data[i+2]

    sumAbc = a + b + c

    counter = 0

    for x in [a,b,c]:
        if len(str(abs(x))) == 4 and abs(x) % 10 == 6:
            counter+=1

    if counter == 1:
        if sumAbc <= mUp:
            cRes +=1
            if sumAbc > sumUp:
                sumUp = sumAbc

print(cRes, sumUp)

