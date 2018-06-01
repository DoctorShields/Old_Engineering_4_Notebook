# Get accel data and IP address and put it on a little OLED
# By Dr. Shields

import time
import socket
import os
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# reset pin for OLED
RST = 24

# create OLED and accelerometer objects
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
lsm303 = Adafruit_LSM303.LSM303()

# temp until i'm online
ipaddr = "---.---.---.---"

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# First define some constants to allow easy resizing of shapes.
padding = 0
top = padding
x = padding

# Load default font.  
font = ImageFont.load_default()
# font = ImageFont.truetype('AldotheApache.ttf', 15)
lineSpacing = 12

while True:
    # black rectangle
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((x, top), 'Accel data:', font=font, fill=255)
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_z, mag_y = mag
    # x
    draw.text((x, top+lineSpacing), 'X: ', font=font, fill=255)
    draw.text((x+20, top+lineSpacing), str(round(accel_x/107.,3)), font=font, fill=255)
    # y
    draw.text((x, top+lineSpacing*2), 'Y: ', font=font, fill=255)
    draw.text((x+20, top+lineSpacing*2), str(round(accel_y/107.,3)), font=font, fill=255)
    # z
    draw.text((x, top+lineSpacing*3), 'Z: ', font=font, fill=255)
    draw.text((x+20, top+lineSpacing*3), str(round(accel_z/107.,3)), font=font, fill=255)
    # IP
    gw = os.popen("ip -4 route show default").read().split()
    # make sure i'm online
    if(len(gw) > 0):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((gw[2], 0))
        ipaddr = s.getsockname()[0]
        
    draw.text((x, top+lineSpacing*4), 'IP: ', font=font, fill=255)
    draw.text((x+20, top+lineSpacing*4), ipaddr, font=font, fill=255)
    time.sleep(1)
    # Display image.
    disp.image(image)
    disp.display()

