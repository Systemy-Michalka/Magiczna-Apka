import threading
import time

from Resolver import Resolver
from SerialPort import SerialPort
import sys

from SystemVolume import show_mixer
from SystemUsage import show_host_data


def main():
    ser = SerialPort(sys.argv[1], Resolver(), timeout=0)
    ser.start()

    def ask_for_volume():
        threading.Timer(0.7, ask_for_volume).start()
        ser.write(b'zad2')
        ser.write(str(show_mixer()).encode())

    def ask_for_usage():
        threading.Timer(5.0, ask_for_usage).start()
        data = show_host_data()
        ser.write(b'C')
        ser.write(str(data['cpu']).encode())
        ser.write(b'T')
        ser.write(str(data['temperature']).encode())
        ser.write(b'M')
        ser.write(str(data['memory']).encode())

    ask_for_volume()
    ask_for_usage()


if __name__ == '__main__':
    main()
