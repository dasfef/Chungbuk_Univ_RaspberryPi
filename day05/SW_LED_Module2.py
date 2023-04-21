from time import sleep
import gpiozero

led1 = gpiozero.LED(17)
led2 = gpiozero.LED(27)
sw1 = gpiozero.Button(3)
sw2 = gpiozero.Button(4)

while True :
    if sw1.is_pressed:
        led1.off()
    else :
        led1.on()
        print("Sw1 Pressed")
        
    if sw2.is_pressed:
        led2.off()
    else:
        led2.on()
        print("Sw2 Pressed")
            