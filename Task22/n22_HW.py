d = {}
for line in open("C:\\Users\\Василий Макаров\\Desktop\\EGEPashinin\\Task22\\HW\\dz-22-data\\73.txt"):
    pId,t,deps = line.split("\t")
    pId = int(pId)
    t = int(t)
    deps = list(map(int,deps.split(";")))
    d[pId] = [t,deps]

def totalTime(pId):
    if pId == 0:
        return 0
    t, deps = d[pId]
    t = t + max([totalTime(dep)for dep in deps])
    return t


for pId in d:
    print(totalTime(pId))

print(max([totalTime(pId) for pId in d]))

#ans: 307
