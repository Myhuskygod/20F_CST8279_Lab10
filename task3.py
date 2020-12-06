import click
from gfxhat import backlight, lcd, fonts
from PIL import Image, ImageFont, ImageDraw


def generateDictionary():

    f = open('font3.txt','r')
    k_v_pair = []
    while True:
        line = f.readline()
        if line == "":
            break
        else:
            line = line.replace("\n","").split(",")
        value = line[0]
        key = line[1]
        k_v_pair.append((key,value))
    k_v_dict = dict(k_v_pair)
    return k_v_dict

chars = generateDictionary()


def clearScreen(lcd):
    lcd.clear()
    lcd.show()
def displayText(text,lcd,x,y):
    lcd.clear()
    backlight.set_all(120,120,120)
    backlight.show()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
            lcd.show()
            # pass

c = click.getchar()
print(c)
n = 0
for key in chars.keys():
    if key == c:
        clearScreen(lcd)
        print(chars[key])
        displayText(chars[key], lcd, 5, 20)
        n = 1
if n==0:
    msg = "The key you input isn't recorded in the dictionary."
    print(msg)
    clearScreen(lcd)
    displayText(msg, lcd, 5, 20)