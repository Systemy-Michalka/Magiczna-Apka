import threading
import time
from tkinter import *
from tkinter import font

from SystemUsageDisplay import init_system_usage_gui
from TakeActions import init_take_actions_gui
from VolumeDisplay import init_volume_display_gui
from Resolver import Resolver
from SerialPort import SerialPort

ser = SerialPort(sys.argv[1], Resolver(), timeout=0)
ser.start()


window = Tk()
window.title("Host")

frames = []

for row in range(6):
    frame = Frame(window)
    frame.grid(column=0, row=row, padx=20, pady=20)
    frame.update()
    frames.append(frame)


def get_scale(volume: str):
    ser.write(b'zad1')
    print(volume)
    ser.write(volume.encode())

# zadanie 1


scale1 = Scale(frames[0], orient=HORIZONTAL, command=get_scale)
scale1.set(80)
scale1.grid(column=0, row=0)

# zadanie 2
init_volume_display_gui(frames[1])

# zadanie 3
label3 = Label(frames[2], text="Zadanie 3", font=font.Font(size=20))
label3.grid(column=0, row=0)

# zadanie 4
init_take_actions_gui(frames[3])

# zadanie 5
init_system_usage_gui(frames[4])

# zadanie 6
label6 = Label(frames[5], text="Zadanie 6", font=font.Font(size=20))
label6.grid(column=0, row=0)

window.mainloop()

