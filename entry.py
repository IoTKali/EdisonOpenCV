import time
import sensors
import pyupm_grove as grove
import pyupm_servo as servo 
from Main import main
from sensors import checkButtonPulse

servoInput = servo.ES08A(6)
servoOutput = servo.ES08A(7)
buttonInput = grove.GroveButton(3)
buttonOutput = grove.GroveButton(2)
touch = ttp223.TTP223(8)
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
mqttc = mqtt.Client("zone_1")
mqttc.connect("10.43.28.194")
regSpaces = 15
avSpaces = regSpaces

def on_connect(client, userdata, flags, rc):
    client.subscribe("zone_1")

def on_message(client, userdata, message):
    available -= 1
    sensors.displayUpdate(display, avSpaces, regSpaces)

mqttc.on_connect = on_connect
mqttc.on_message = on_message

while(True):
    if sensors.doubleTouchPulse(touch):
        avSpaces +=1
        mqttc.publish("zone_1", "zone_2")
        sensors.displayUpdate(display, avSpaces, regSpaces)
        
    if __name__ == "__main__":
        if sensors.buttonPulse(buttonInput):
            main()
            time.sleep(3)
            sensors.spinServo(s
            avSpaces -= 1
            sensors.displayUpdate(display, avSpaces, regSpaces)
    if sensors.buttonPulse(buttonOutput):
        mqttc.publish("exit_1", "zone_1")
        avSpaces += 1
        sensors.displayUpdate(display, avSpaces, regSpaces)
