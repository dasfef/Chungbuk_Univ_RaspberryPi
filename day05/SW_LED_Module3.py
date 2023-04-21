from time import sleep
import gpiozero

led1 = gpiozero.LED(17)
led2 = gpiozero.LED(27)
sw1 = gpiozero.Button(3)
sw2 = gpiozero.Button(4)

def Sw1_Pressed():
    led1.on()
    print("Sw1 Pressed")
    
def Sw2_Pressed():
    led2.on()
    print("Sw2 Pressed")

while True :
    if sw1.is_pressed:
        led1.off()
    else :
        Sw1_Pressed()
        
    if sw2.is_pressed:
        led2.off()
    else:
        Sw2_Pressed()
            
