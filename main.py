from machine import Pin, PWM
from time import sleep_ms
from random import randint

bid = randint (1000, 3000)

rautt = Pin(10, Pin.IN, Pin.PULL_UP)
blatt = Pin(11, Pin.IN, Pin.PULL_UP)
graennt = Pin(12, Pin.IN, Pin.PULL_UP)
gult = Pin(13, Pin.IN, Pin.PULL_UP)

rautt_ljos = Pin(15, Pin.OUT)
blatt_ljos = Pin(16, Pin.OUT)
graennt_ljos = Pin(17, Pin.OUT)
gult_ljos = Pin(18, Pin.OUT)

hatalari_passive = PWM(Pin(14), freq=20000)
            
def slokkva_allt():
    rautt_ljos.value(0)
    blatt_ljos.value(0)
    graennt_ljos.value(0)
    gult_ljos.value(0) 
    
def kveikja_allt():
    rautt_ljos.value(1)
    blatt_ljos.value(1)
    graennt_ljos.value(1)
    gult_ljos.value(1)
#sleep_ms (bid)


slokkva_allt()

hatalari_passive.duty(512)
    
hatalari_passive.freq(1397)
sleep_ms (214)
hatalari_passive.freq(1046)
sleep_ms (214)
hatalari_passive.freq(100000)
sleep_ms (214)
sleep_ms (214)

hatalari_passive.freq(1760)
sleep_ms (214)
hatalari_passive.freq(1046)
sleep_ms (214)
hatalari_passive.freq(100000)
sleep_ms (214)
sleep_ms (214)

hatalari_passive.freq(1397)
sleep_ms (214)
hatalari_passive.freq(1046)
sleep_ms (214)

hatalari_passive.freq(2093)
sleep_ms (214)
sleep_ms (214)

hatalari_passive.freq(100000)
sleep_ms (21)

hatalari_passive.freq(1397)
sleep_ms (214)
hatalari_passive.freq(1046)
sleep_ms (214)
hatalari_passive.freq(100000)
sleep_ms (214)
sleep_ms (214)

hatalari_passive.freq(1760)
sleep_ms (214)
hatalari_passive.freq(1046)
sleep_ms (214)
hatalari_passive.freq(100000)
sleep_ms (214)
sleep_ms (214)
hatalari_passive.freq(1397)
sleep_ms (214)
hatalari_passive.freq(1046)
sleep_ms (214)

hatalari_passive.freq(2093)
sleep_ms (214)
sleep_ms (214)

hatalari_passive.freq(100000)
sleep_ms (21)
hatalari_passive.freq(1397)
sleep_ms (214)
hatalari_passive.freq(1046)
sleep_ms (214)
hatalari_passive.freq(100000)
sleep_ms (214)
sleep_ms (214)

hatalari_passive.freq(1760)
sleep_ms (214)
hatalari_passive.freq(1046)
sleep_ms (214)
hatalari_passive.freq(100000)
sleep_ms (214)
sleep_ms (214)
hatalari_passive.freq(1397)
sleep_ms (214)
hatalari_passive.freq(1046)
sleep_ms (214)

hatalari_passive.freq(2093)
sleep_ms (214)
sleep_ms (214)

hatalari_passive.freq(100000)
sleep_ms (21)
hatalari_passive.freq(1397)
sleep_ms (214)
hatalari_passive.freq(1046)
sleep_ms (214)
hatalari_passive.freq(100000)
sleep_ms (214)
sleep_ms (214)

hatalari_passive.freq(1760)
sleep_ms (214)
hatalari_passive.freq(1046)
sleep_ms (214)
hatalari_passive.freq(100000)
sleep_ms (214)
sleep_ms (214)
hatalari_passive.freq(1397)
sleep_ms (214)
hatalari_passive.freq(1046)
sleep_ms (214)

hatalari_passive.freq(2093)
sleep_ms (214)
sleep_ms (214)

hatalari_passive.freq(100000)
sleep_ms (21)




                      


                      

sleep_ms(bid)

kveikja_allt()

def check_winner():
    if not rautt.value():  
        rautt.value(1)  
        blatt.value(0)
        graennt.value(0)
        gult.value(0)
        return True
    elif not blatt.value():  
        blatt.value(1)  
        rautt.value(0)
        graennt.value(0)
        gult.value(0)
        return True
    elif not graennt.value():  
        graennt.value(1)  
        rautt.value(0)
        blatt.value(0)
        gult.value(0)
        return True
    elif not gult.value():  
        gult.value(1)  
        rautt.value(0)
        blatt.value(0)
        graennt.value(0)
        return True
    return False

while True:
    if check_winner():
        break  

    
