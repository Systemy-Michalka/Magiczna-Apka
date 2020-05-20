import subprocess
import time


"""
Odpalamy ten program i wpisujemy numery wirtualnych portów(każdemu wyświetlają się inne)

Na przyszłość pasuje zmienić sposób odpalania tych aplikacji oraz ustawić porty z socata na sztywno, mi się nie udało
"""
subprocess.Popen("socat -d -d pty,raw,echo=0,b9600 pty,raw,echo=0,b9600", shell=True)
time.sleep(0.05)
socket_number = input("Enter first socket: /dev/pts/")
subprocess.Popen("python Server.py " + socket_number, shell=True)
print("Host application started!")
socket_number = input("Enter second socket: /dev/pts/")
subprocess.Popen("python Gui.py " + socket_number, shell=True)
