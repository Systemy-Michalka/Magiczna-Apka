import sys
import getopt
import alsaaudio

def show_mixer():
    mixer = alsaaudio.Mixer("Master")
    volumes = mixer.getvolume()
    return volumes[0]

if __name__ == '__main__':
    show_mixer();
