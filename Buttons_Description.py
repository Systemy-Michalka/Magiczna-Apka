from tkinter import *


def init_describe_button_gui(frame):
    # tytuł sekcji
    var = StringVar()
    title = Label(frame, text="Button Descriptions", font=font.Font(size=20))
    title.grid(column=0, row=0)
    screen = Label(frame, text="", font=font.Font(size=20))
    screen.grid(column=0, row=1)
    title3 = Label(frame, textvariable=var, font=font.Font(size=20))
    title3.grid(column=0, row=2)
    
    var.set("Description")


    def describe_button1():
        var.set("1: Uruchom przeglądarkę WWW")

    def describe_button2():
        var.set("2: Edytor tekstu Vi")

    def describe_button3():
        var.set("3: Uruchom program mc")

    def describe_button4():
        var.set("4: Uruchom terminal")

    def describe_button5():
        var.set("5: Uruchom kalendarz")

    def describe_button6():
        var.set("6: Uruchom skrypt1")

    def describe_button7():
        var.set("7: Uruchom skrypt2")
    
    def describe_button8():
        var.set("8: Uruchom skrypt3")

    #creating buttons
    Button1 = Button(frame, text="1", command = describe_button1)
    Button2 = Button(frame, text="2", command = describe_button2)
    Button3 = Button(frame, text="3", command = describe_button3)
    Button4 = Button(frame, text="4", command = describe_button4)
    Button5 = Button(frame, text="5", command = describe_button5)
    Button6 = Button(frame, text="6", command = describe_button6)
    Button7 = Button(frame, text="7", command = describe_button7)
    Button8 = Button(frame, text="8", command = describe_button8)

    #placeing buttons
    Button1.place(x=0, y=40)
    Button2.place(x=20, y=40)
    Button3.place(x=40, y=40)
    Button4.place(x=60, y=40)
    Button5.place(x=80, y=40)
    Button6.place(x=100, y=40)
    Button7.place(x=120, y=40)
    Button8.place(x=140, y=40)
    
