from tkinter import *
import random

# create window
window = Tk()
window.title('Typing Speed Test')
window.geometry("800x600")

text = "test text".split("\n")

frame = Frame(window)

# creating a label
label = Label(frame, text=random.choice(text), font=("Helventica", 18))
label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# creating a text box
input_entry = Entry(frame, width=40, font=("Helventica", 24))
input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

# creating a label for the timer
speed_label = Label(frame, text="Speed: 0.00 CPS, 0.00 CPM, 0.00 WPS, 0.00 WPM", font=("Helventica", 18))
speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)


frame.pack(expand=True)

window.mainloop()