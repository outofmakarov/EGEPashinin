#27


'''a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\dz-24-data\\k7b-1.txt")
a = a.read()


c=0
c1 = 0
for i in range(0,len(a)):
    if a[i] == "E" and  a[i+1] == "A" and a[i+2] == "B":
        c+=1
        if c > c1:
            c1 = c
    else:
        c=0
print(c1)'''

#35
'''a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\dz-24-data\\k7c-3.txt")
a = a.read()

c=0
c1 = 0
for i in range(0,len(a)-2):
    if (a[i+1] in "BDE" and
            (a[i+2] in "ACD" and a[i+2] != a[i+1])
            and a[i] == a[i+2]):

        c+=1
        if c > c1:
            c1 = c
    else:
        c=0
print(c1)'''

#40
#a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\dz-24-data\\k7-m2.txt")
#a = a.read()

'''a = "ABCCAACCCC"
c=0
c1 = 0
n = 0
for i in range(0,len(a)):
    if a[i] == "C":
        c+=1
        if c > c1:
            c1 = c
    if a[i-1] in "AB":
        n+=1
    else:
        c=0
print(c1,n)

#ans: 3

#47

#a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\dz-24-data\\k7-m21.txt")
#a = a.read()

a = "ABCCAACCCC"
c=0
c1 = 0
n = 0
for i in range(0,len(a)):
    if a[i] == "C":
        c+=1
        if c > c1:
            c1 = c
    if a[i-1] in "AB":
        n+=1
    else:
        c=0
print(c1,n)

#57

a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\dz-24-data\\24-s1.txt")
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
print(c1)'''

#138


a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\dz-24-data\\24-s1.txt")
a = a.readlines()

c=0
for i in a:
    if i.count("K") > i.count("U"):
            c+=1

print(c)

#ans: 470

#141


a = open("C:\\Users\Василий Макаров\\Desktop\\EGEPashinin\\Task24\\dz-24-data\\24-s1.txt")
a = a.readlines()

c=0
c1 = 0

for i in range(0,len(a)-2):
    if a[i] == "F" and a[i+2] == "O" and a[i+1] in "QWERTYUIOPASDFGHJKLZXCVBNM":
        c+=1

print(c1)

