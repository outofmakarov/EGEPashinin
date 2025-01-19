'''d = {
    10: [4, [5,6]]
}'''

'''for line in open("input.txt"):
    pId,t,deps = line.split("\t")
    pId = int(pId)
    t = int(t)
    deps = list(map(int,deps.split(";")))
    d[pId] = [t,deps]

def totalTime(pId):
    if pId == 0:
        return 0
    t, deps = d[pId]
    t + max([totalTime(dep)for dep in deps])


for pId in d:
    print(totalTime(pId))

print(max([totalTime(pId) for pId in d]))'''

'''
# ? = time

from functools import cache
d = {}

for line in open('C:\\Users\\Василий Макаров\\Desktop\\EGEPashinin\\Task22\\input1.txt'):
    pid, t, deps = line.split("\t")
    pid = int(pid)
    t = int(t)
    deps = list(map(int, deps.split(';')))
    d[pid] = [t, deps]

@cache
def totalTime(pid):
    if pid == 0:
        return 0
    t, deps = d[pid]
    t += max([totalTime(dep) for dep in deps])
    return t


print(max([totalTime(pid) for pid in d]))'''


