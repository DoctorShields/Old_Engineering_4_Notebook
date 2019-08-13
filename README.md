# Engineering_4_Notebook
## Run Script on Startup

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

asdhfasdfhas;ldfj wel;fnsdalf;nksd
asfnsd fsdaklfj asdfklj asd;flkje
e
sdfksadfsd
