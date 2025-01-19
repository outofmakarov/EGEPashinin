#24.1

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

a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\task24.4_24.txt")
a = a.read()

#a = "ACDFOFO"
a = (a.replace("C","S").replace("D","S").replace("F","S")
     .replace("A","G").replace("O","G").replace("SG","9"))
#print(a)
c=0
c1 = 0
for i in range(0,len(a)):
    if a[i] == "9":
        c+=1
        if c > c1:
            c1 = c
    else:
        c=0
print(c1)

#24.5

a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\task24.4_24.txt")
a = a.read()



