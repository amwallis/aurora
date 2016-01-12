import webiopi
import datetime

GPIO = webiopi.GPIO

RED_PIN = 26
GRN_PIN = 19
BLU_PIN = 13

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    GPIO.setFunction(RED_PIN, GPIO.OUT)
    GPIO.setFunction(GRN_PIN, GPIO.OUT)
    GPIO.setFunction(BLU_PIN, GPIO.OUT)

# loop function is repeatedly called by WebIOPi 
def loop():

    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(RED_PIN, GPIO.LOW)
    GPIO.digitalWrite(GRN_PIN, GPIO.LOW)
    GPIO.digitalWrite(BLU_PIN, GPIO.LOW)

@webiopi.macro
def get_color(x, y):
    print ("hi")
    print(x)
    print(y)