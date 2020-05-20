from tkinter import *
from tkinter import font

import VolumeDisplay
import SystemUsageDisplay

window = Tk()
window.title("Host")

frames = []

for row in range(6):
    frame = Frame(window)
    frame.grid(column=0, row=row, padx=20, pady=20)
    frame.update()
    frames.append(frame)

# zadanie 1
label1 = Label(frames[0], text="Zadanie 1", font=font.Font(size=20))
label1.grid(column=0, row=0)

# zadanie 2
VolumeDisplay.init_gui(frames[1])

# zadanie 3
label3 = Label(frames[2], text="Zadanie 3", font=font.Font(size=20))
label3.grid(column=0, row=0)

# zadanie 4
label4 = Label(frames[3], text="Zadanie 4", font=font.Font(size=20))
label4.grid(column=0, row=0)

# zadanie 5
SystemUsageDisplay.init_gui(frames[4])

# zadanie 6
label6 = Label(frames[5], text="Zadanie 6", font=font.Font(size=20))
label6.grid(column=0, row=0)

window.mainloop()
