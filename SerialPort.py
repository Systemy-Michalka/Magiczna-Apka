import threading
import time

import serial


class SerialPort(threading.Thread):

    def __init__(self, port, resolver, baudrate=9600, timeout=1, write_timeout=0.05):
        super().__init__()
        self.resolver = resolver
        self.port = serial.Serial(port, baudrate=baudrate, timeout=timeout, write_timeout=write_timeout)

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
        time.sleep(0.05)
        self.port.write(data)

    def read(self):
        while True:
            key = self.port.read(size=8)
            if len(key) > 0:

                while True:
                    data = self.port.read(size=8)
                    if len(data) > 0:
                        break

                self.resolver.on_message(key, data)
                print(f'Odczytane: {data}')
