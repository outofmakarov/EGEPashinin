#33

'''def f(x,y):

    if x == y: return 1
    if x > y: return 0
    if x % 2 == 0:
        return f(x+1,y) + f(x*1.5,y)

print(f(2,22))'''

#34

'''def f(x,y):
    if x == y: return 1
    if x > y: return 0
    return f(x+1,y) + f(x*2,y) + f(x*2 + 1, y)

print(f(2,16))'''

#ans: 40

#49
'''def f(x,y):
    if x == y: return 1
    if x > y: return 0
    return f(x+2,y) + f(x+3,y) + f(x + (x-1), y)

print(f(2,11))'''

#ans: 17

#56

'''def f(x,y):
    if x == y: return 1
    if x > y or x == 28: return 0
    return f(x+1,y) + f(x*2,y)

print(f(2,10) * f(10,34))'''

#ans: 21

#105

'''def f(x,y,c):
    if x == y and c == 7: return 1
    if x > y: return 0
    return f(x+1,y,c+1) + f(x+3,y,c+1) + f(x*2,y,c+1)

print(f(2,25,0))'''

#ans:53


#132
'''def f(x,y):
    if int(x) == int(y): return 1
    if int(x) > int(y): return 0
    return f(x+1,y) +f(x+"0")'''

#119

'''def f(x,y):
    if x == y: return 1
    if x > y: return 0'''

#148

'''def f(x,y):
    if y == 0: return 0
    return f(x+3,y-1) + f(x*2 + 1,y-1)

print(f(2,13))'''

#152

'''def f(x, y):
    def f1(x1, p):
        if x1 > y:
            return 0
        if x1 == y:
            if (17 in p) + (23 in p) >= 1:
                return 1
            return 0

        return f1(x1 + 1, p + [x1 + 1]) + f1(x1 + 2, p + [x1 + 2])

    return f1(x, [x])


print(f(11, 29))'''

#ans: 3861


#208

'''def f(x,y):
    if x == y: return 1
    if x < y: return 0

    return f(x-2,y) + f(x//2,y)

print(f(28,10) * f(10,1))'''

#ans: 36

#266

def f(x,y):
    if x == y: return 1
    if x < y or x == 9 or x == 16: return 0
    return f(x-1,y) + f(x-2,y) + f(x//3,y)

print(f(19,3))

#ans: 180



#327

'''def f(x,y):
    if x == y: return 1
    if x < y: return 0
    return f(x-2,y) + f(x//2,y)

print(f(32,8) * f(8,1))'''

#ans: 42

