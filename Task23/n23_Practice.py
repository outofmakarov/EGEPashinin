#23.3
def f(x,y):
    if x == y:
        return 1
    if x > y or x == 11 or x == 12:
        return 0

    return  f(x+1,y) + f(x+2,y) + f(x*1.5,y)

print(f(2,10) * f(10,22))
#ans: 124

#23.4
'''def f1(x,y, c):
    if x == y and c == 8: return 1
    if x > y: return 0

    return f1(x+1,y, c+1) + f1(x*2,y, c+1) + f1(x*3,y,c+1)

print(f1(1,34,0))'''

#ans: 21

#23.5
'''def f2(x,y,c):
    if x == y and c <= 2: return 1
    if x > y: return 0
    return f2(x+1,y,c) + f2(x*2,y,c+1) + f2(x*3,y,c+1)

print(f2(1,100,0))'''

#
'''def f(x,y,c):
    if x == y: return 1
    if x > y: return 0
    if c == "+1":
        return f(x*2,y,"*2")
    if c == "*2":
        return f(x + 1, y, "+1")

    return f(x+1,y,"+1") + f(x*2,y,"*2")

print(f(1,16,0))'''

#23.6
def null(n):
    binN = bin(n)[2:]
    binN = "1" + "0"* (len(binN)-1)
    return binN

def f(x,y):
    x = int(x,2)
    y = int(y,2)

    if x == y:
        return 1
    if x < y: return 0

    t = null(x)
    if bin(x)[2:] == t: return f(bin(x-1)[2:],bin(y)[2:])

    return f(bin(x-1)[2:],bin(y)[2:]) + f(null(x),bin(y)[2:])


print(f("1100","100"))

#ans:20

