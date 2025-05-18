'''p = [i for i in range(17,47)]
q = [i for i in range(22,58)]
res = []

for a_down in range(17,58):
    for a_up in range(a_down+1,58):
        ok = True
        a = [i for i in range(a_down,a_up+1)]
        for x in range(-300,300):
            if ((x in a) or (not((x in p)and (x in q)) or (x in a))) == False:
                ok = False
                break
        if ok:
            res.append(a_up-a_down)

print(min(res))'''

'''p = [i for i in range(55,81)]
q = [i for i in range(20,106)]
res = []



for a_down in range(20,106):
    for a_up in range(a_down+1,106):
        ok = True
        a = [i for i in range(a_down,a_up+1)]
        for x in range(-300,300):
            f = ((x not in q) or ( ((x in p) == (x in q)) or ((x in p) or (x in a)) ))
            if f == False:
                ok = False
                break
        if ok:
            res.append(a_up - a_down)

print(min(res))'''

'''for a in range(-300,300):
    ok = True
    for x in range(0,300):
        for y in range(0,300):
            f = ((not(y*y < a) or (y<16)) and (not(x <= 13) or (x*x < a)))
            if f == False:
                ok = False
                break
    if ok:
        print(a)'''

