from time import sleep
import gpiozero

led1 = gpiozero.LED(17)
led2 = gpiozero.LED(27)

while True:
    led1.on()
    led2.off()
    
    sleep(0.1)
    led1.off()
    led2.on()
    
    sleep(0.1)