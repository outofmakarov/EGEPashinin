#13.4
'''from ipaddress import *

net = ip_network("192.168.32.160/255.255.255.240",False)
c = 0

for ip in net:
    strIP = bin(int(ip))[2::]
    if strIP.count("1") % 2 == 0:
        c+=1

print(c)'''
#13.5
'''from ipaddress import *

net = ip_network("202.75.38.176/255.255.255.240")

for ip in net:
    strIP = bin(int(ip))[2::]
    if "111" not in strIP and "000" not in strIP:
        print(ip,strIP)'''
from ipaddress import *



