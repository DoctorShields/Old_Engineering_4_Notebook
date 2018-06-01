# Engineering_4_Notebook
Run Script on Startup

Make a launcher script
<pre>
#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/Python
sudo python thingToBeLaunched.py
cd /
</pre>
Change permissions
<pre>
chmod 755 launcher.sh
</pre>
Edit crontab
<pre>
sudo crontab -e
</pre>
Add this line to the end
<pre>
@reboot sh /home/pi/launcher.sh >/home/pi/logs/cronlog 2>&1
</pre>
Notice, that will dump errors into your logs directory.  Make sure you have a logs directory.
