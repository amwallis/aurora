import webiopi
import datetime

GPIO = webiopi.GPIO

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    #GPIO.setFunction(LIGHT, GPIO.OUT)


# loop function is repeatedly called by WebIOPi 
def loop():

    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.LOW)