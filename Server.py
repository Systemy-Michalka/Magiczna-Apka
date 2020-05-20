from SerialPort import SerialPort
import sys


def main():

    ser = SerialPort(sys.argv[1], timeout=0)
    ser.start()


if __name__ == '__main__':
    main()
