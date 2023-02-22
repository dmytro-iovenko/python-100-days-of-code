from tkinter import *
import random

def start(event):
    global running
    if not running:
        if not event.keycode in [16, 17, 18]:
            running = True
    if not label.cget('text').startswith(input_entry.get()):
        input_entry.config(fg="red")
    else:
        input_entry.config(fg="black")
    if input_entry.get() == label.cget('text'):
        running = False
        input_entry.config(fg="green")

# create window
window = Tk()
window.title('Typing Speed Test')
window.geometry("800x600")

# adding the boolean to know that the app is started or not
counter = 0
running = False

text = "test text".split("\n")

frame = Frame(window)

# creating a label
label = Label(frame, text=random.choice(text), font=("Helventica", 18))
label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# creating a text box
input_entry = Entry(frame, width=40, font=("Helventica", 24))
input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

# adding the function to start automatically if the key is pressed
input_entry.bind("<KeyRelease>", start)

# creating a label for the timer
speed_label = Label(frame, text="Speed: 0.00 CPS, 0.00 CPM, 0.00 WPS, 0.00 WPM", font=("Helventica", 18))
speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

frame.pack(expand=True)

window.mainloop()