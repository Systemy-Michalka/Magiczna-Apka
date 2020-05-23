import os

import SystemVolume
from VolumeDisplay import set_volume_leds


class Resolver:

    def on_message(self, key, message):
        key = str(key, "utf-8")
        message = str(message, "utf-8")
        if hasattr(self, key):
            getattr(self, key)(message)
        else:
            print(f"There is no {key} command")

    def zad1(self, message):
        os.system(f'amixer set Master {message}%')

    def zad2(self, message):
        set_volume_leds(int(message))

    def zad3(self, message):
        pass

    def zad4(self, message):
        pass

    def zad5(self, message):
        pass

    def zad6(self, message):
        pass
