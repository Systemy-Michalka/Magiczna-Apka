import psutil


def show_memory():
    virtual = psutil.virtual_memory()
    memoreUsed = int(virtual[2])
    return memoreUsed


def show_temperature():
    temperature = psutil.sensors_temperatures(fahrenheit=False)
    temp = int(temperature['acpitz'][0][1])
    return temp


def show_cpu():
    cpu = psutil.cpu_percent(interval=1)

    result = int(cpu)
    return result


def show_host_data():

    return {"cpu": show_cpu(), "temperature": show_temperature(), "memory": show_memory()}


if __name__ == '__main__':
    show_host_data()
