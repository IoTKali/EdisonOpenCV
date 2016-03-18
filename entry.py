
import time
import pyupm_grove as grove

from Main import main

from motorx import servo



def checkButtonPulse(button):
    if (button.value() != 0):
        while True:
            if button.value() == 0:
                return True
    return False


myButton = grove.GroveButton(5)
while True:
    if checkButtonPulse(myButton):
        Main.main()
        
        time.delay(3)

        motorx.servo()
        break
