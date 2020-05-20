import threading

import serial


class SerialPort(threading.Thread):

    def __init__(self, port, baudrate=9600, timeout=1):
        print("Startuje")
        super().__init__()
        self.port = serial.Serial(port, baudrate=baudrate, timeout=timeout)

    def run(self):
        thread = threading.Thread(target=self.read())
        thread.start()
        thread.join()

    def open(self):
        try:
            self.port.open()
        except:
            pass

    def close(self):
        self.port.close()

    def write(self, data):
        print("write")
        self.port.write(data)

    def read(self):
        while True:
            data = self.port.read(size=8)
            if len(data) > 0:
                """
                Tutaj trzeba napisać jakiegoś resolvera albo zwykłe nawet if/else, który dla danego klucza będzie wykonywał 
                konkretną operację 
                """
                print(f'Odczytane: {data}')
