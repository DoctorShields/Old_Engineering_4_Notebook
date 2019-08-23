# Engineering_4_Notebook
## Raspberry Pi
### Run Script on Startup

Make a launcher script
```
#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/Python
sudo python thingToBeLaunched.py
cd /
```
Change permissions

`chmod 755 launcher.sh`

Edit crontab

`sudo crontab -e`

Add this line to the end

`@reboot sh /home/pi/launcher.sh >/home/pi/logs/cronlog 2>&1`

Notice, that will dump errors into your logs directory.  Make sure you have a logs directory.

### Kill Flask App
```
ps aux | grep app.py
sudo kill <process number >
```
### Monitor Blinking Fix

`sudo nano /boot/config.txt`

Try

```
config_hdmi_boost=7
hdmi_mode=82
disable_overscan=1
```
### Keep Monitor On

`sudo nano /etc/lightdm/lightdm.conf`

In the `[Seat:*]` section

`xserver-command=X -s 0 dpms`

### Run Script on Startup
Make a launcher script

```
#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/bbt
sudo python bbt.py
cd /
```
Change permissions

`chmod 755 launcher.sh`

Edit crontab

`sudo crontab -e`

Add this line to the end

`@reboot sh /home/pi/launcher.sh >/home/pi/logs/cronlog 2>&1`

### What is my IP?
```
import time
import socket
import os
 
ipaddr = "---.---.---.---"
online = False
while not online:
    gw = os.popen("ip -4 route show default").read().split()
    if(len(gw) > 0):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((gw[2], 0))
        ipaddr = s.getsockname()[0]
        gateway = gw[2]
        host = socket.gethostname()
        online = True
    time.sleep(1)
print ("IP:", ipaddr, " GW:", gateway, " Host:", host)
```