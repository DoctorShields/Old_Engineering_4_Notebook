from flask import Flask, render_template, request
import Adafruit_SSD1306

from PIL import Image, ImageDraw, ImageFont

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

font = ImageFont.truetype('AldotheApache.ttf', 15)
lineSpacing = 15

app = Flask(__name__)

@app.route('/')
def start_page():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def write_to_screen():
    text = request.form['thing']
    print('Your string is {0}'.format(text))
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((10, 10), text, font=font, fill=255)
    # Display image.
    disp.image(image)
    disp.display()
    return render_template('index.html')

@app.route('/input/<text>/')
def other(text):
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((10, 10), text, font=font, fill=255)
    # Display image.
    disp.image(image)
    disp.display()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
