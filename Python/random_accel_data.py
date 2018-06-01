# just some fake data
# By Dr. Shields

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps
from random import randint
from math import floor
from time import sleep

# reset pin for OLED
RST = 24

# make the display
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Some vars
width = disp.width
height = disp.height
height2 = 50
lineSpacing = 13
leftSide = 15
lineBot = 52
xDivs = 12
dx = floor(width/xDivs)

# Create image; 1 = Bilevel, L = greyscale, RGB = true color
img1 = Image.new('1', (width, height))
img2 = Image.new('1', (height2, width))

# Create drawing objects on the images
draw1 = ImageDraw.Draw(img1)
draw2 = ImageDraw.Draw(img2)

# Load default font and write some text
font = ImageFont.load_default()

while True:
    # font = ImageFont.truetype('AldotheApache.ttf', 15)
    draw1.text((44,54), 'Time(s)', font=font, fill=255)
    draw2.text((0,0), 'a(m/s2)', font=font, fill=255)
    # rotate image2 and then paste onto image1
    rot2 = img2.rotate(90)
    img1.paste(rot2,(0,0,width,height2))
    draw1.line((leftSide,lineBot,width,lineBot),fill=255)
    draw1.line((leftSide,lineBot,leftSide,0),fill=255)
    arr = [0]*(xDivs+1)
    for i in range(0,xDivs):
        arr[i] = 30+randint(0,16)-8
    for i in range(0,(xDivs-1)):
        draw1.line((leftSide+dx*i,arr[i],leftSide+dx*(i+1),arr[i+1]),fill=255)
    disp.image(img1)
    disp.display()
    sleep(2)
