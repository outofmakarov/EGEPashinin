#33

'''def f(x,y):

    if x == y: return 1
    if x > y: return 0
    if x % 2 == 0:
        return f(x*1.5,y) + f(x+1,y)
    if x % 2 == 1:
        return f(x+1,y)

print(f(2,22))'''

#ans:44

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
    x = int(x,2)
    y = int(y,2)
    if x == y: return 1
    if x > y: return 0
    return f(bin(x+1)[2:],bin(y)[2:]) + f(bin(x)[2:]+"0",bin(y)[2:]) + f(bin(x)[2:]+"1",bin(y)[2:])

print(f("101","101110"))'''

#ans:254


#119
'''arr = set([])
def f(x,c):
    if c == 8:
        if 1000 <= x <= 1024:
            arr.add(x)
        return 0
    return f(x+1,c+1) + f(x+5,c+1) + f(x*3,c+1)

f(1,0)
print(len(arr))'''

#148
'''arr = []
def f(x,y):
    if y == 13:
        arr.append(x)
        return 0
    return f(x+3,y+1) + f(x*2 + 1,y+1)

f(2,0)
print(len(set(arr)))'''

#ans: 973

#152

'''def f(x,y,c1,c2):
    if x == y and (c1 == 1 or c2 == 1): return 1
    if x > y: return 0

    if x == 17: c1=1
    if x == 23: c2=1

    return f(x+1,y,c1,c2) + f(x+2,y,c1,c2)

print(f(11, 29,0,0))'''

#ans: 3861


#208

'''def f(x,y):
    if x == y: return 1
    if x < y: return 0

    return f(x-2,y) + f(x//2,y)

print(f(28,10) * f(10,1))'''

#ans: 36

#266

'''def f(x,y):
    if x == y: return 1
    if x < y or x == 9 or x == 16: return 0
    return f(x-1,y) + f(x-2,y) + f(x//3,y)

print(f(19,3))'''

#ans: 180


#327

'''def f(x,y):
    if x == y: return 1
    if x < y: return 0
    return f(x-2,y) + f(x//2,y)

print(f(32,8) * f(8,1))'''

#ans: 42

