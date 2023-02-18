from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
from io import BytesIO

def uploadImg():
    # read the image
    filename = filedialog.askopenfilename(initialdir =  "/", title = "Select an Image", filetype = (("jpeg files","*.jpg"),("PNG  files","*.png")))
    image = Image.open(filename)
    # resize the image using resize() method        
    resize_image = image.resize((640, 400))

    show_img = ImageTk.PhotoImage(resize_image)
    # show the resized image
    img.config(image=show_img)
    img.image = show_img

    # save the image data into var_photo
    outfile = BytesIO()
    resize_image.save(outfile, "PNG")
    var_image.set(outfile.getvalue())            

# create window
window = Tk()
window.title('Image Watermarking Desktop App')

# set window size
window.geometry("660x470")

var_image = Variable()  # use Variable() to store image

#Create an Image Object from an Image
im = Image.open('dog.jpg')
im = im.resize((640, 400)) # Resize the image using resize() method
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

img_frame = LabelFrame(window, text="")
img_frame.place(x = margin, y = 40 + margin * 2, width = width, height = height)

# create the image inside img_frame
img = Label(img_frame)
img.pack()

if var_image.get():
    # render watermarked image
    render = ImageTk.PhotoImage(data=var_image.get())
    img.config(image = render)
    img.image = render

btn_upload_img = Button(text = "Upload Image", command = uploadImg).place(x = margin, y = margin, width = 150, height = 40)
#btn_save = Button( text="Save", bg="green", command=add).place(x=200, y=330, width= 150 , height=40)


window.mainloop()