from tkinter import *
import random
import math

timer = None

def start(event):
    global running
    global timer

    if not running:
        if not event.keycode in [16, 17, 18]:
            running = True
            reset_button.config(state="normal")
            timer = window.after(100, count, 0.1)

    if not label.cget('text').startswith(input_entry.get()):
        input_entry.config(fg="red")
    else:
        input_entry.config(fg="black")
    if input_entry.get() == label.cget('text'):
        running = False
        input_entry.config(fg="green")


def reset():
    global running
    running = False
    reset_button.config(state="disabled")
    speed_label.config(text="Speed: 0.00 CPS, 0.00 CPM, 0.00 WPS, 0.00 WPM")
    label.config(text=random.choice(text))
    input_entry.delete(0, END)


def count(counter):
    global running
    global timer

    cps = len(input_entry.get()) / counter
    cpm = cps * 60
    wps = len(input_entry.get().split(" ")) / counter
    wpm = wps * 60

    if running:
        speed_label.config(text=f"Speed: {cps:.2f} CPS, {cpm:.2f} CPM, {wps:.2f} WPS, {wpm:.2f} WPM")
        timer = window.after(100, count, counter + 0.1)

# create window
window = Tk()
window.title('Typing Speed Test')
window.geometry("800x600")

# adding the boolean to know that the app is started or not
running = False

text = open("text.txt", "r").read().split("\n")

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

# creating a reset button
reset_button = Button(frame, text="Reset", command=reset, font=("Helventica", 24))
reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
reset_button.config(state="disabled")

frame.pack(expand=True)

window.mainloop()