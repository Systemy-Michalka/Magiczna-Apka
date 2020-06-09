import os

import SystemVolume
from VolumeDisplay import set_volume_leds
from SystemUsageDisplay import update_cpu, update_memory, update_temperature


class Resolver:

    def on_message(self, key, message):
        key = str(key, "utf-8")
        message = str(message, "utf-8")

        if hasattr(self, key):
            getattr(self, key)(message)
        else:
            print(f"There is no {key} command")

    def zad1(self, message):
        os.system(f'amixer set Master {message}% > /dev/null')

    def zad2(self, message):
        set_volume_leds(int(message))

    def T(self, message):
        update_temperature(message)

    def M(self, message):
        update_memory(message)

    def C(self, message):
        update_cpu(message)

    def zad4(self, message):
        message = int(message)
        if message == 3:  # przeglądarka WWW
            os.system("firefox") # lub inna zainstalowana na danej maszynie
        elif message == 12:
            os.system("vi")
        elif message == 48:
            os.system("mc")  # na Fedorze konieczne instalowanie odpowiedniego pakietu
        elif message == 192:
            os.system("gnome-terminal")
        elif message == 15:
                os.system("cal")
        elif message == 60:
            os.system("bash script1.sh") # wybrane polecenie/skrypt w terminalu
        elif message == 240:
            os.system("bash script2.sh") # wybrane polecenie/skrypt w terminalu
        elif message == 195:
            os.system("bash script3.sh") # wybrane polecenie/skrypt w terminalu
        pass

    

    def zad5(self, message):
        pass

    def zad6(self, message):
        pass
