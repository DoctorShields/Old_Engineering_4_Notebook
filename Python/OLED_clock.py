import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24

# Note you can change the I2C address by passing an i2c_address parameter like:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

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

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php

# Write two lines of text.
# draw.text((x, top),    'ABCDEFGHIJKLMNOPQRSTUVW',  font=font, fill=255)
# draw.text((x, top+10), '01234567890abcdefghijkl', font=font, fill=255)
# draw.text((x, top+20), 'Here is some data:', font=font, fill=255)
secs = 30
mins = 59
hrs = 16
while mins < 120:
    # black rectangle
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    font = ImageFont.load_default()
    draw.text((x, top), 'I made a clock!', font=font, fill=255)
    font = ImageFont.truetype('AldotheApache.ttf', 40)
    if secs < 10:
        secStr = '0'+str(secs)
    else:
        secStr = str(secs)
    if mins < 10:
        minStr = '0'+str(mins)
    else:
        minStr = str(mins)
    if hrs < 10:
        hrStr = '0'+str(hrs)
    else:
        hrStr = str(hrs)
    timeStr = hrStr + ':' + minStr + ':' + secStr
    # the time
    draw.text((x, top+20), timeStr, font=font, fill=255)
    secs += 1
    if secs == 60:
        secs = 0
        mins += 1
    if mins == 60:
        mins = 0
        hrs += 1
    time.sleep(1)
    # Display image.
    disp.image(image)
    disp.display()
