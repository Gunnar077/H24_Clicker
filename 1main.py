from machine import Pin,PWM , SoftI2C
from time import ticks_ms,sleep_ms
from I2C_LCD import I2cLcd

i2c = SoftI2C(scl=Pin(1), sda=Pin(2), freq=400000)
lcd = I2cLcd(i2c, 39, 2, 16)
passiveBuzzer = PWM(Pin(4), freq=40000)
takki_a= Pin(9, Pin.IN, Pin.PULL_UP)
takki_b= Pin(10, Pin.IN, Pin.PULL_UP)
takki_c= Pin(11, Pin.IN, Pin.PULL_UP)
takki_d= Pin(12, Pin.IN, Pin.PULL_UP)
summa_a =0
summa_b =0
summa_c =0
summa_d =0
led_blatt= Pin(5, Pin.OUT)
led_graent=Pin(6, Pin.OUT)
led_gult= Pin(7, Pin.OUT)
led_rautt= Pin(15, Pin.OUT)

led_blatt.value(1)
led_graent.value(1)
led_gult.value(1)
led_rautt.value(1)

leikur_upphafstimi=ticks_ms()
leikur_bidtimi=5000
# leikur=True
def lag():
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
    
takki_a_sidast = 1
takki_b_sidast = 1
takki_c_sidast = 1
takki_d_sidast = 1

while True:
    lcd.move_to(0, 0)
    lcd.putstr("Game")
    lcd.move_to(0, 1)
    lcd.putstr("Start")
#     passiveBuzzer.init()          
#     passiveBuzzer.duty(512)
    
 
    if takki_a.value () ==0 and takki_a_sidast == 1:
        summa_a=summa_a + 1
        print("summa_a =",summa_a)
#         while takki_a.value() == 0:
#             print("blár")
#             pass
    takki_a_sidast = takki_a.value()
    
    if takki_b.value () ==0 and takki_b_sidast == 1:
        summa_b=summa_b + 1
        print("summa_b =",summa_b)
#         while takki_b.value() == 0:
#             print("grænn")
#             pass
    takki_b_sidast = takki_b.value()
        
        
    if takki_c.value () ==0 and takki_c_sidast == 1:
        summa_c=summa_c + 1
        print("summa_c =",summa_c)
#         while takki_c.value() == 0:
#             print("gulur")
#             pass
    takki_c_sidast = takki_c.value()
       
        
        
    if takki_d.value () ==0 and takki_d_sidast == 1:
        summa_d=summa_d + 1
        print("summa_d =",summa_d)
#         while takki_d.value() == 0:
#             print("rauður")
#             pass
    takki_d_sidast = takki_d.value()
    timi_nuna=ticks_ms()

    if timi_nuna - leikur_upphafstimi > leikur_bidtimi:
        print(f"leik lokið: {timi_nuna} - {leikur_upphafstimi} = {timi_nuna - leikur_upphafstimi}")
#         leikur=False
        
        print(summa_a, summa_b, summa_c, summa_d)

        if summa_a>summa_b and summa_a>summa_c and summa_a>summa_d:
            print("Blar vinnur")
            led_rautt.value(1)
            lcd.move_to(0, 0)
            lcd.putstr("Blue")
            # Færi bendilinn í staf nr. 0 og línu nr. 1
            lcd.move_to(0, 1)
            lcd.putstr("Wins!")
#             lag()
#             sleep_ms(2000)
#             leikur=True
            
            
        
        if summa_b>summa_a and summa_b>summa_c and summa_b>summa_d:
            print("Græn vinnur")
            led_blatt.value(1)
            lcd.move_to(0, 0)
            lcd.putstr("Green")
            # Færi bendilinn í staf nr. 0 og línu nr. 1
            lcd.move_to(0, 1)
            lcd.putstr("Wins!")
#             lag()
#             sleep_ms (21)
        if summa_c>summa_a and summa_c>summa_b and summa_c>summa_d:
            print("Gulur vinnur")
            led_graent.value(1)
            lcd.move_to(0, 0)
            lcd.putstr("Yellow")
            # Færi bendilinn í staf nr. 0 og línu nr. 1
            lcd.move_to(0, 1)
            lcd.putstr("Wins!")
#             lag()
            
        if summa_d>summa_a and summa_d>summa_c and summa_d>summa_b:
            print("Rauður vinnur")
            led_gult.value(1)
            lcd.move_to(0, 0)
            lcd.putstr(" Red")
            #Færi bendilinn í staf nr. 0 og línu nr. 1
            lcd.move_to(0, 1)
            lcd.putstr("Wins!")
            
        if summa_a==summa_b and summa_a==summa_c and summa_a==summa_d and summa_b==summa_c and summa_b==summa_d and summa_c==summa_d:
            print("Eingin vinnur")
            lcd.move_to(0, 0)
            lcd.putstr("Nobody")
            # Færi bendilinn í staf nr. 0 og línu nr. 1
            lcd.move_to(0, 1)
            lcd.putstr("Wins...")
        lag()
        summa_a =0
        summa_b =0
        summa_c =0
        summa_d =0
        lcd.move_to(0, 0)
        lcd.putstr("New Game      ")
        lcd.move_to(0, 1)
        lcd.putstr("                ")
        sleep_ms(2000)
        lcd.move_to(0, 0)
        lcd.putstr("                ")
#         leikur = True
        leikur_upphafstimi = ticks_ms()

        
        
    
        


    
    
    


