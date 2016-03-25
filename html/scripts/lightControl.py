
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

RAINBOW_CYCLE = False
RAINBOW_VALUES = [1,0,1]

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GRN_PIN, GPIO.OUT)
GPIO.setup(BLU_PIN, GPIO.OUT)
pR = GPIO.PWM(RED_PIN, 80)
pG = GPIO.PWM(GRN_PIN, 80)
pB = GPIO.PWM(BLU_PIN, 80)

# setup function is automatically called at WebIOPi startup
def setup():
    pR.start(0)
    pG.start(0)
    pB.start(0)

# loop function is repeatedly called by WebIOPi 
def loop():
    global RAINBOW_CYCLE
    if RAINBOW_CYCLE == False:
        # gives CPU some time before looping again
        webiopi.sleep(1)
    elif RAINBOW_CYCLE == True:
        rainbowStateMachine()
# destroy function is called at WebIOPi shutdown
def destroy():
    pG.stop()
    pR.stop()
    pB.stop()
    GPIO.cleanup()  

def rainbowStateMachine():
    global RED_PCT, GREEN_PCT, BLUE_PCT, RAINBOW_VALUES
    if RAINBOW_VALUES[0] == 1:
        if RED_PCT < 100:
            RED_PCT += 1
            pR.ChangeDutyCycle(RED_PCT)
    elif RAINBOW_VALUES[0] == 0:
        if RED_PCT > 0:
            RED_PCT -= 1
            pR.ChangeDutyCycle(RED_PCT)
    if RAINBOW_VALUES[1] == 1:
        if GREEN_PCT < 100:
            GREEN_PCT += 1
            pG.ChangeDutyCycle(GREEN_PCT)
    elif RAINBOW_VALUES[1] == 0:
        if GREEN_PCT > 0:
            GREEN_PCT -= 1
            pG.ChangeDutyCycle(GREEN_PCT)
    if RAINBOW_VALUES[2] == 1:
        if BLUE_PCT < 100:
            BLUE_PCT += 1
            pB.ChangeDutyCycle(BLUE_PCT)
    elif RAINBOW_VALUES[2] == 0:
        if BLUE_PCT > 0:
            BLUE_PCT -= 1
            pB.ChangeDutyCycle(BLUE_PCT)

    #color transition state machine
    #bring back blue (1,0,1)
    if RAINBOW_VALUES[0] == 1 and RAINBOW_VALUES[1] == 0 and RAINBOW_VALUES[2] == 1:
        if RED_PCT == 100 and GREEN_PCT == 0 and BLUE_PCT == 100:
            RAINBOW_VALUES = [0,0,1]
    #drop red (0,0,1)
    elif RAINBOW_VALUES[0] == 0 and RAINBOW_VALUES[1] == 0 and RAINBOW_VALUES[2] == 1:
        if RED_PCT == 0 and GREEN_PCT == 0 and BLUE_PCT == 100:
            RAINBOW_VALUES = [0,1,1]
    #bring in green (0,1,1)
    elif RAINBOW_VALUES[0] == 0 and RAINBOW_VALUES[1] == 1 and RAINBOW_VALUES[2] == 1:
        if RED_PCT == 0 and GREEN_PCT == 100 and BLUE_PCT == 100:
            RAINBOW_VALUES = [0,1,0]
    #drop blue (0,1,0)
    elif RAINBOW_VALUES[0] == 0 and RAINBOW_VALUES[1] == 1 and RAINBOW_VALUES[2] == 0:
        if RED_PCT == 0 and GREEN_PCT == 100 and BLUE_PCT == 0:
            RAINBOW_VALUES = [1,1,0]
    #bring in red (1,1,0)
    elif RAINBOW_VALUES[0] == 1 and RAINBOW_VALUES[1] == 1 and RAINBOW_VALUES[2] == 0:
        if RED_PCT == 100 and GREEN_PCT == 100 and BLUE_PCT == 0:
            RAINBOW_VALUES = [1,0,0]
    #drop green (1,0,0)
    elif RAINBOW_VALUES[0] == 1 and RAINBOW_VALUES[1] == 0 and RAINBOW_VALUES[2] == 0:
        if RED_PCT == 100 and GREEN_PCT == 0 and BLUE_PCT == 0:
            RAINBOW_VALUES = [1,0,1]

    #slow the transition
    time.sleep(0.02)

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
    
    #saves CPU by turning off pwm if duty cycle is 0
    if red == 0:
        pR.stop()
    elif RED_PCT == 0:
        pR.start(0)
    if green == 0:
        pG.stop()
    elif GREEN_PCT == 0:
        pG.start(0)
    if blue == 0:
        pB.stop()
    elif BLUE_PCT == 0:
        pB.start(0)

    #update global vars
    RED_PCT = int(red)
    GREEN_PCT = int(green)
    BLUE_PCT = int(blue)
    pR.ChangeDutyCycle(float(red))
    pG.ChangeDutyCycle(float(green))
    pB.ChangeDutyCycle(float(blue))
    return getLightValue()

@webiopi.macro
def rainbowCycle():
    global RAINBOW_CYCLE
    RAINBOW_CYCLE = not RAINBOW_CYCLE
