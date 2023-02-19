from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
from io import BytesIO

width, height, margin = 640, 400, 10

def uploadImg():
    # read the image
    filename = filedialog.askopenfilename(initialdir =  "/", title = "Select an Image", filetype = (("jpeg files","*.jpg"),("PNG  files","*.png")))
    if filename:
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
        outfile.seek(0)
        byteImg = outfile.read()
        var_image.set(byteImg)            

        btn_set_watermark.config(state="normal")

def setWatermark():
    if var_image.get():
        im = Image.open(BytesIO(var_image.get()))

        draw = ImageDraw.Draw(im)
        width, height = im.size

        text = 'sample watermark'
        font = ImageFont.truetype('arial.ttf', 36)
        textwidth, textheight = draw.textsize(text, font)

        # calculate the x,y coordinates of the text
        x = width - textwidth - margin
        y = height - textheight - margin

        # draw watermark in the bottom right corner
        draw.text((x, y), text, font=font)

        # render the watermarked image
        render = ImageTk.PhotoImage(im)

        # show the watermarked image
        img.config(image=render)
        img.image = render


# create window
window = Tk()
window.title('Image Watermarking Desktop App')

# set window size
window.geometry("660x470")

var_image = Variable()  # use Variable() to store image
var_watermark = Variable()  # use Variable() to store watermark text

img_frame = LabelFrame(window, text="")
img_frame.place(x = margin, y = 40 + margin * 2, width = width, height = height)

# create the image inside img_frame
img = Label(img_frame)
img.pack()

btn_upload_img = Button(text = "Upload Image", command = uploadImg).place(x = margin, y = margin, width = 150, height = 40)

btn_set_watermark = Button(text="Set Watermark", command = setWatermark)
btn_set_watermark.place(x = 150 + margin * 2, y = margin, width = 150 , height = 40)
btn_set_watermark.config(state="disabled")


window.mainloop()