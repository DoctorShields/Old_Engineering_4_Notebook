import time
import socket
import os

ipaddr = "---.---.---.---"
online = False

while not online:
    gw = os.popen("ip -4 route show default").read().split()
    if len(gw) > 0:
        print("Getting online...")
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((gw[2],0))
        ipaddr = s.getsockname()[0]
        gateway = gw[2]
        host = socket.gethostname()
        online = True
    time.sleep(1)
print("IP:", ipaddr, " GW:", gateway, " Host:", host)
