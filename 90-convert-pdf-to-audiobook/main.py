import PyPDF3
import pyttsx3
from tkinter import *

file = 'lorem.pdf'

window = Tk()
window.geometry("750x450")
text = Text(window, width=80, height=30)
text.pack(pady=20)
  
book = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(file)
pdf_page = pdfReader.getPage(0)
content = pdf_page.extractText()

text.insert(1.0,content)
  
#speak = pyttsx3.init()
#speak.say(content)
#speak.runAndWait()

window.mainloop()
