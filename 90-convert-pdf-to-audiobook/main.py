import PyPDF3
import pyttsx3
import pygame
from tkinter import *

file = 'lorem.pdf'
current_page_num = 0
width, height, margin = 640, 400, 10
is_play, is_pause = False, False

pygame.mixer.init()
speak = pyttsx3.init()

def render_page(num, total):
    global current_page_num
    if (num < 0 or num == total):
        return
    else:
        current_page_num = num
    pdf_page = pdfReader.getPage(num)
    content = pdf_page.extractText()

    text.delete(1.0,END)
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

def play():
    global is_play, engine
    if is_play:
        pygame.mixer.music.stop()
        is_play = False
        btn_play.config(text="    Play    ")
        btn_pause.config(text="    Pause    ", state="disabled")
    else:
        outfile = "temp.wav"
        speak.save_to_file(text.get('1.0', END), outfile)
        speak.runAndWait()
        pygame.mixer.music.load(outfile)
        pygame.mixer.music.play()
        is_play = True
        btn_play.config(text="    Stop    ")
        btn_pause.config(state="normal")

def pause():
    global is_pause
    if is_pause:
        pygame.mixer.music.unpause()
        is_pause = False
        btn_pause.config(text="    Pause    ")
    else:
        pygame.mixer.music.pause()
        is_pause = True
        btn_pause.config(text="   Unpause   ")


book = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(file)
pdf_pages = pdfReader.getNumPages()

window = Tk()
window.geometry("750x450")

fm = Frame(window)
btn_prev_page = Button(fm, text = " < Prev Page ", command = lambda: render_page(current_page_num - 1, pdf_pages))
btn_prev_page.pack(side=LEFT, fill=X, expand=NO)
btn_next_page = Button(fm, text = " Next Page > ", command = lambda: render_page(current_page_num + 1, pdf_pages))
btn_next_page.pack(side=LEFT, fill=X, expand=NO)
label = Label(fm, text= f"{current_page_num+1}/{pdf_pages}", font= ('Helvetica', 12))
label.pack(side=LEFT, fill=X, expand=YES)

btn_play = Button(fm, text = "    Play    ", command = play)
btn_play.pack(side=LEFT, fill=X, expand=NO)
btn_pause = Button(fm, text = "    Pause    ", command = pause)
btn_pause.pack(side=LEFT, fill=X, expand=NO)
fm.pack(pady=20, fill=BOTH, expand=YES)

#btn_prev_page = Button(text = " < Prev Page", command = lambda: render_page(current_page_num - 1, pdf_pages))
#btn_prev_page.place(x = margin, y = margin, width = 100, height = 40)
#btn_next_page = Button(text = " Next Page > ", command = lambda: render_page(current_page_num + 1, pdf_pages))
#btn_next_page.place(x = margin + 100, y = margin, width = 100, height = 40)

#label= Label(window, text= f"{current_page_num+1}/{pdf_pages}", font= ('Helvetica', 12))
#label.pack(pady=20)

#btn_play = Button(text = "Play", command = play)
#btn_play.place(x = 750 - margin - 200, y = margin, width = 100, height = 40)
#btn_pause = Button(text = "Pause", command = pause)
#btn_pause.place(x = 750 - margin - 100, y = margin, width = 100, height = 40)
#btn_pause.config(state="disabled")


v=Scrollbar(window, orient='vertical')
v.pack(side=RIGHT, fill='y')

text = Text(window, y = 40 + margin * 2, width=80, height=30, yscrollcommand=v.set)
v.config(command=text.yview)
text.pack(expand=True, fill=BOTH)
  

render_page(0, pdf_pages)

window.mainloop()
