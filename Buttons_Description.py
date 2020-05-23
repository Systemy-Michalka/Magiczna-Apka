#Robione bez dostępu do sprzętu (czyt. "niesprawdzone w praktyce")

from RPLCD import CharLCD
import requests
import time
import RPi.GPIO as GPIO

#display wired in 8 bit mode
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23])

Pin1 = 3
Pin2 = 5
Pin3 = 7
Pin4 = 8
Pin5 = 10
Pin6 = 11
Pin7 = 12
Pin8 = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(Pin1,GPIO.IN)
GPIO.setup(Pin2,GPIO.IN)
GPIO.setup(Pin3,GPIO.IN)
GPIO.setup(Pin4,GPIO.IN)
GPIO.setup(Pin5,GPIO.IN)
GPIO.setup(Pin6,GPIO.IN)
GPIO.setup(Pin7,GPIO.IN)
GPIO.setup(Pin8,GPIO.IN)


while True:
    if(GPIO.input(Pin1) == True):#S1 na ciśnięty ponad 1,1 s
        start = time.time()
        GPIO.wait_for_edge(Pin1, GPIO.FALLING)
        stop = time.time() - start
        if(stop >= 1.1):
            lcd.write_string("Uruchom przeglądarkę WWW")
            
    elif(GPIO.input(Pin2) == True):#S2 naciśnięty ponad 1,1 s
        start = time.time()
        GPIO.wait_for_edge(Pin2, GPIO.FALLING)
        stop = time.time() - start
        if(stop >= 1.1):
            lcd.write_string("Edytor tekstu Vi")
            
    elif(GPIO.input(Pin3) == True):#S3 naciśnięty ponad 1,1 s
        start = time.time()
        GPIO.wait_for_edge(Pin3, GPIO.FALLING)
        stop = time.time() - start
        if(stop >= 1.1):
            lcd.write_string("Uruchom program mc")
            
    elif(GPIO.input(Pin4) == True):#S4 naciśnięty ponad 1,1 s
        start = time.time()
        GPIO.wait_for_edge(Pin4, GPIO.FALLING)
        stop = time.time() - start
        if(stop >= 1.1):
            lcd.write_string("Uruchom terminal")
            
    elif(GPIO.input(Pin5) == True):#S5 naciśnięty ponad 1,1 s
        start = time.time()
        GPIO.wait_for_edge(Pin5, GPIO.FALLING)
        stop = time.time() - start
        if(stop >= 1.1):
            lcd.write_string("Uruchom kalendarz")
            
    elif(GPIO.input(Pin6) == True):#S6 naciśnięty ponad 1,1 s
        start = time.time()
        GPIO.wait_for_edge(Pin6, GPIO.FALLING)
        stop = time.time() - start
        if(stop >= 1.1):
            lcd.write_string("Uruchom wybrane polecenie/skrypt w terminalu")
            
    elif(GPIO.input(Pin7) == True):#S7 naciśnięty ponad 1,1 s
        start = time.time()
        GPIO.wait_for_edge(Pin7, GPIO.FALLING)
        stop = time.time() - start
        if(stop >= 1.1):
            lcd.write_string("Uruchom wybrane polecenie/skrypt w terminalu")
            
    elif(GPIO.input(Pin8) == True):#S8 naciśnięty ponad 1,1 s
        start = time.time()
        GPIO.wait_for_edge(Pin8, GPIO.FALLING)
        stop = time.time() - start
        if(stop >= 1.1):
            lcd.write_string("Uruchom wybrane polecenie/skrypt w terminalu")
            
