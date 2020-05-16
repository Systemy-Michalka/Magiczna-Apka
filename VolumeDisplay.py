# ilość ledów głośności
LEDS = 8

# maksymalny poziom głośności
MAX_VOLUME = 100

# ilość aktualnie zaświeconych ledów
current_leds = 0


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

    # na razie LEDy są wyświetlane w konsoli
    # todo zapalić LEDy w GUI
    for i in range(current_leds):
        print("☻", end="")
    for i in range(LEDS - current_leds):
        print("☺", end="")
    print()


def test():
    print("356 ", end=" ")
    set_volume_leds(356)

    print("66  ", end=" ")
    set_volume_leds(66)

    print("10  ", end=" ")
    set_volume_leds(10)

    print("10  ", end=" ")
    set_volume_leds(22)

    print("34  ", end=" ")
    set_volume_leds(34)

    print("100 ", end=" ")
    set_volume_leds(100)

    print("-123", end=" ")
    set_volume_leds(-123)
