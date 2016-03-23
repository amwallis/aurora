
#SETUP PYTHON PATH
import sys
import webiopi
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# GPIO = webiopi.GPIO

RED_PIN = 26
GRN_PIN = 19
BLU_PIN = 13

RED_PCT = 0
GREEN_PCT = 0
BLUE_PCT = 0

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GRN_PIN, GPIO.OUT)
GPIO.setup(BLU_PIN, GPIO.OUT)
pR = GPIO.PWM(RED_PIN, 70)
pG = GPIO.PWM(GRN_PIN, 70)
pB = GPIO.PWM(BLU_PIN, 70)

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    # GPIO.setFunction(RED_PIN, GPIO.OUT)
    # GPIO.setFunction(GRN_PIN, GPIO.OUT)
    # GPIO.setFunction(BLU_PIN, GPIO.OUT
    
    pR.start(0)
    pG.start(0)
    pB.start(0)

# loop function is repeatedly called by WebIOPi 
def loop():

    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    pG.stop()
    pR.stop()
    pB.stop()
    GPIO.digitalWrite(RED_PIN, GPIO.LOW)
    GPIO.digitalWrite(GRN_PIN, GPIO.LOW)
    GPIO.digitalWrite(BLU_PIN, GPIO.LOW)

@webiopi.macro
def get_color(x, y):
    print(x)
    print(y)
   # r, g, b = rgb_im.getpixel((x, y))
    #print (r, g, b)

@webiopi.macro
def getLightValue():
    return "%d;%d;%d" % (RED_PCT, GREEN_PCT, BLUE_PCT)

@webiopi.macro
def setLightValue(red, green, blue):
    global RED_PCT, GREEN_PCT, BLUE_PCT
    RED_PCT = int(red)
    GREEN_PCT = int(green)
    BLUE_PCT = int(blue)
    print (red)
    print (green)
    print (blue)
    pR.ChangeDutyCycle(float(red))
    pG.ChangeDutyCycle(float(green))
    pB.ChangeDutyCycle(float(blue))
    return getLightValue()
