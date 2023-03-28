import PyPDF3
import pyttsx3
from tkinter import *

file = 'lorem.pdf'
current_page_num = 0
width, height, margin = 640, 400, 10

def render_page(num, total):
    global current_page_num
    if (num < 0 or num == total):
        return
    else:
        current_page_num = num
    pdf_page = pdfReader.getPage(num)
    content = pdf_page.extractText()

    text.delete(1.0,"end")
    text.insert(1.0,content)
    label.config(text=f"{num+1}/{pdf_pages}")

    if(num == 0 and num == total - 1):
        btn_prev_page.config(state="disabled")
        btn_next_page.config(state="disabled")
    elif(num == 0):
        btn_prev_page.config(state="disabled")
        btn_next_page.config(state="normal")
    elif(num == total - 1):
        btn_prev_page.config(state="normal")
        btn_next_page.config(state="disabled")
    else:
        btn_prev_page.config(state="normal")
        btn_next_page.config(state="normal")


book = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(file)
pdf_pages = pdfReader.getNumPages()

window = Tk()
window.geometry("750x450")

btn_prev_page = Button(text = " < Prev Page", command = lambda: render_page(current_page_num - 1, pdf_pages))
btn_prev_page.place(x = margin, y = margin, width = 100, height = 40)
btn_next_page = Button(text = " Next Page > ", command = lambda: render_page(current_page_num + 1, pdf_pages))
btn_next_page.place(x = margin + 100, y = margin, width = 100, height = 40)

label= Label(window, text= f"{current_page_num+1}/{pdf_pages}", font= ('Helvetica', 12))
label.pack(pady=20)

v=Scrollbar(window, orient='vertical')
v.pack(side=RIGHT, fill='y')

text = Text(window, y = 40 + margin * 2, width=80, height=30, yscrollcommand=v.set)
v.config(command=text.yview)
text.pack(expand=True, fill=BOTH)
  

render_page(0, pdf_pages)

#speak = pyttsx3.init()
#speak.say(content)
#speak.runAndWait()

window.mainloop()
