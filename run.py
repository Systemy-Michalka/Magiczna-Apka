import re
import shutil
import subprocess
import sys
import threading
import time


"""
Odpalamy ten program i wpisujemy numery wirtualnych portów(każdemu wyświetlają się inne)

Na przyszłość pasuje zmienić sposób odpalania tych aplikacji oraz ustawić porty z socata na sztywno, mi się nie udało
"""
socat_proc = subprocess.Popen("socat -d -d pty,raw,echo=0,b9600 pty,raw,echo=0,b9600",
                              shell=True, stderr=subprocess.PIPE)

# scan output for 2 ptys
ptylist = []
for line in socat_proc.stderr:
    line = line.decode().strip()
    print(line)
    pty = re.search(r"N PTY is (.+)", line)
    if pty:
        ptylist.append(pty.group(1))
        if len(ptylist) == 2:
            break


print("PTY list: ", ptylist)

time.sleep(0.5)
subprocess.Popen("python Server.py " + ptylist[0], shell=True)
subprocess.Popen("python Gui.py " + ptylist[1], shell=True)
