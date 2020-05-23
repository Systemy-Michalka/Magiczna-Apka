from SystemVolume import show_mixer
from tkinter import Label, font, Frame


# liczba ledów głośności
LEDS = 8

# maksymalny poziom głośności
MAX_VOLUME = 100

# ilość aktualnie zaświeconych ledów
current_leds = 0

# komponenty ledów
volume_leds = []

# kolory ledów
TURN_OFF_COLOR = "#696969"
TURN_ON_COLOR = "#0063c7"


def init_volume_display_gui(frame):
    # tytuł sekcji
    title = Label(frame, text="Volume", font=font.Font(size=20))
    title.grid(column=0, row=0)

    # kontener na ledy
    leds_frame = Frame(frame)
    leds_frame.grid(column=0, row=1)

    # tworzenie i ustawianie ledów
    for col in range(8):
        led = Label(leds_frame, text='', width=2, height=1, bg=TURN_OFF_COLOR)
        led.grid(column=col, row=1)
        volume_leds.append(led)
        leds_frame.grid_columnconfigure(col, minsize=40)

    # pierwsze wywołanie
    set_volume_leds(show_mixer())


def set_volume_leds(volume: int):
    """
    Oblicza ile LEDów powinno być zaświeconych. Jeśli liczba różni się od aktualnej, aktualizuje LEDy
    volume - Poziom głośności.
    """

    # sprawdzanie czy volume jest poprawną liczbą
    if volume > MAX_VOLUME:
        volume = MAX_VOLUME
    elif volume < 0:
        volume = 0

    # obliczanie ile ledów powinno się zapalić
    leds_on = round(LEDS * volume / MAX_VOLUME)

    # jeśli aktualna liczba ledów zmieniła się, zaaktualizuj ledy
    global current_leds
    if leds_on != current_leds:
        current_leds = leds_on
        update_leds()


def update_leds():
    """Aktualizuje LEDy. Zapala i gasi odpowiednie LEDy."""
    # zaświeć
    for i in range(current_leds):
        volume_leds[i].configure(background=TURN_ON_COLOR)

    # zgaś
    for i in range(current_leds, LEDS):
        volume_leds[i].configure(background=TURN_OFF_COLOR)
