import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24

# Note you can change the I2C address by passing an i2c_address parameter like:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
lsm303 = Adafruit_LSM303.LSM303()

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

# Load default font.  
# font = ImageFont.load_default()
font = ImageFont.truetype('AldotheApache.ttf', 15)
lineSpacing = 9
while True:
    # black rectangle
    draw.rectangle((0,0,width,height), outline=0, fill=0)
   
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_z, mag_y = mag
    # x
    draw.text((0, (height-lineSpacing)/2), 'X:', fill=255)
    draw.text((12, (height-lineSpacing)/2), str(round(accel_y/108.,1)), fill=255)
    # y
    draw.text((width/2-14, height-lineSpacing), 'Y:', fill=255)
    draw.text((width/2+12-14, height-lineSpacing), str(round(accel_x/108.,1)), fill=255)
    #a: -9.8   0   9.8
    #x:  0     64   128
    #Y:  0     32   64
    x=128-(accel_y/108.+9.8)/19.6*128
    y=64-(accel_x/108.+9.8)/19.6*64 
    draw.ellipse((x-5, y-5, x+5, y+5), outline=255, fill=0)
    time.sleep(.5)
    # Display image.
    disp.image(image)
    disp.display()
