from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
from io import BytesIO

#Create an Image Object from an Image
im = Image.open('dog.jpg')
width, height = im.size

draw = ImageDraw.Draw(im)
text = 'sample watermark'

font = ImageFont.truetype('arial.ttf', 36)
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 10
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)

# save watermarked image
byte_io = BytesIO()
im.save(byte_io, 'PNG')

# create window
window = Tk()
window.title('Image Watermarking Desktop App')

# set window size
window.geometry("%sx%s" % (width, height))

# render watermarked image
render = ImageTk.PhotoImage(Image.open(byte_io))
img = Label(image=render)
img.image = render
img.place(x=0, y=0)

window.mainloop()