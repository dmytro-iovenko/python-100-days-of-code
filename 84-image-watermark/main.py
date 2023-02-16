from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Image Watermarking Desktop App")

#Create an Image Object from an Image
load = Image.open('dog.jpg')
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render
img.place(x=0, y=0)

window.mainloop()