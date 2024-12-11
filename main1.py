from machine import Pin,PWM , SoftI2C
from time import ticks_ms,sleep_ms
from I2c_LCD import I2cLcd

tkki_a = Pin(10, Pin.IN, Pin.PULL_UP)
takki_b = Pin(11, Pin.IN, Pin.PULL_UP)
takki_c = Pin(12, Pin.IN, Pin.PULL_UP)
takki_d = Pin(13, Pin.IN, Pin.PULL_UP)
passiveBuzzer = PWM(Pin(14))
i2c = SoftI2C(scl=Pin(13), sda=Pin(14), freq=400000)
lcd = I2cLcd(i2c, 0x3f, 2, 16)

summa_a =0
summa_b =0
summa_c =0
summa_d =0

led_rautt= Pin(15, Pin.OUT)
led_blatt=Pin(16, Pin.OUT)
led_graent= Pin(17, Pin.OUT)
led_gult= Pin(18, Pin.OUT)

led_rautt.value(0)
led_blatt.value(0)
led_graent.value(0)
led_gult.value(0)

leikur_upphafstimi=ticks_ms()
leikur_bidtimi=5000
leikur=True
while leikur==True:
    lcd.move_to(0, 0)
    lcd.putstr("Hallo")
    # Færi bendilinn í staf nr. 0 og línu nr. 1
    lcd.move_to(0, 1)
    lcd.putstr("Heimur")
    passiveBuzzer.deinit()  
    
    timi_nuna=ticks_ms()
 
    if takki_a.value () ==0:
        summa_a=summa_a + 1
        while takki_a.value() == 0:
            pass
   
    
    if takki_b.value () ==0:
        summa_b=summa_b + 1
        while takki_b.value() == 0:
            pass
       
        
        
    if takki_c.value () ==0:
        summa_c=summa_c + 1
        while takki_c.value() == 0:
            pass
       
        
        
    if takki_d.value () ==0:
        summa_d=summa_a + 1
        while takki_d.value() == 0:
            pass
        
    if timi_nuna - leikur_upphafstimi > leikur_bidtimi:
        leikur=False
                   
if summa_a>summa_b and summa_a>summa_c and summa_a>summa_d:
    print("Rauður vinnur")
    led_rautt.value(1)
    passiveBuzzer.init()          
    passiveBuzzer.duty(512)      
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1760)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)

    passiveBuzzer.freq(2093)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(100000)
    sleep_ms (21)

    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1760)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)

    passiveBuzzer.freq(2093)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(100000)
    sleep_ms (21)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1760)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)

    passiveBuzzer.freq(2093)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(100000)
    sleep_ms (21)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1760)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)

    passiveBuzzer.freq(2093)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(100000)
    sleep_ms (21)
   
    
    passiveBuzzer.duty(0)
    passiveBuzzer.deinit() 
    
if summa_b>summa_a and summa_b>summa_c and summa_b>summa_d:
    print("Blár vinnur")
    led_blatt.value(1)
    passiveBuzzer.init()          
    passiveBuzzer.duty(512)      
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1760)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)

    passiveBuzzer.freq(2093)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(100000)
    sleep_ms (21)

    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1760)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)

    passiveBuzzer.freq(2093)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(100000)
    sleep_ms (21)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1760)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)

    passiveBuzzer.freq(2093)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(100000)
    sleep_ms (21)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1760)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)

    passiveBuzzer.freq(2093)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(100000)
    sleep_ms (21)
if summa_c>summa_a and summa_c>summa_b and summa_c>summa_d:
    print("Grænn vinnur")
    led_graent.value(1)
    passiveBuzzer.init()          
    passiveBuzzer.duty(512)      
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1760)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)

    passiveBuzzer.freq(2093)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(100000)
    sleep_ms (21)

    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1760)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)

    passiveBuzzer.freq(2093)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(100000)
    sleep_ms (21)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1760)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(2093)
    
    sleep_ms (214)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (21)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)
    
    passiveBuzzer.freq(1760)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms(214)  
    passiveBuzzer.freq(2093)
    sleep_ms (214)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (21)
if summa_d>summa_a and summa_d>summa_c and summa_d>summa_b:
    print("Gulur vinnur")
    led_gult.value(1)
    passiveBuzzer.init()          
    passiveBuzzer.duty(512)      
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1760)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)

    passiveBuzzer.freq(2093)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(100000)
    sleep_ms (21)

    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1760)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)

    passiveBuzzer.freq(2093)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(100000)
    sleep_ms (21)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1760)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)

    passiveBuzzer.freq(2093)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(100000)
    sleep_ms (21)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(1760)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)
    passiveBuzzer.freq(100000)
    sleep_ms (214)
    sleep_ms (214)
    passiveBuzzer.freq(1397)
    sleep_ms (214)
    passiveBuzzer.freq(1046)
    sleep_ms (214)

    passiveBuzzer.freq(2093)
    sleep_ms (214)
    sleep_ms (214)

    passiveBuzzer.freq(100000)
    sleep_ms (21)
        
        
    
        