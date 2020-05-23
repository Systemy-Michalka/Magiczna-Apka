import threading
import time

from Resolver import Resolver
from SerialPort import SerialPort
import sys

from SystemVolume import show_mixer


def main():

    ser = SerialPort(sys.argv[1], Resolver(), timeout=0)
    ser.start()

    def ask_for_volume():
        threading.Timer(1.0, ask_for_volume).start()
        ser.write(str(show_mixer()).encode())
        ser.write(b'zad2')

    ask_for_volume()


if __name__ == '__main__':
    main()
