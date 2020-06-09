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
        pass

    def zad5(self, message):
        pass

    def zad6(self, message):
        pass
