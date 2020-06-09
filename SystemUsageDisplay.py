from SystemUsage import show_host_data
from tkinter import Label, font, Frame

dic = {"cpu": 0, "temperature": 0, "memory": 0}
result = {"result": "text"}
usage = []


def init_system_usage_gui(frame):
    # testowe wywołanie
    # todo usunąć testowe wywołanie

    set_data_usage(show_host_data())

    title = Label(frame, text="System usage", font=font.Font(size=20))
    title.grid(column=0, row=0)

    usage_frame = Frame(frame)
    usage_frame.grid(column=0, row=1)
    screen = Label(usage_frame, text=result['result'], font=10, width=40, height=2, bg="#0b8615")
    usage.append(screen)
    screen.grid(column=1, row=0)
    usage_frame.grid_columnconfigure(1, minsize=40)


def update_temperature(temp: int):
    dic.update(temperature=temp)
    for u in usage:
        u.configure(text=result['result'])
    update_display()


def update_memory(mem: int):
    dic.update(memory=mem)
    for u in usage:
        u.configure(text=result['result'])
    update_display()


def update_cpu(cpu: int):
    dic.update(cpu=cpu)
    for u in usage:
        u.configure(text=result['result'])
    update_display()


def update_display():
    set_data_usage(dic)


def set_data_usage(dic):
    text = "Cpu: "
    text += str(dic['cpu']) + "%"
    text += " Temperature: "
    text += str(dic['temperature']) + '\N{DEGREE SIGN}C'
    text += " Memory "
    text += str(dic['memory']) + "%"

    result.update(result=text)
