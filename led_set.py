#!/usr/bin/env python
import RPi.GPIO as GPIO
import argparse

# TODO: DEBUG
import time

__author__ = 'https://github.com/fejao'

# Set the default inputs
DEFAULT_GPIO = 18
DEFAULT_LED = 'off'

# Set GPIO number for the LED's colors
GPIO_YELLOW = 17
GPIO_BLUE = 18
GPIO_RED = 22
GPIO_GREEN = 23

def ledOn(gpioNum):
    '''
    Set's the GPIO number to the *high* mode

    Parameters
    ----------
    gpioNum : int
    Number of the GPIO

    Returns
    -------
    None
    '''
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(gpioNum,GPIO.OUT)
    GPIO.output(gpioNum, GPIO.HIGH)

def ledOff(gpioNum):
    '''
    Set's the GPIO number to the *low* mode

    Parameters
    ----------
    gpioNum : int
    Number of the GPIO

    Returns
    -------
    None
    '''
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(gpioNum,GPIO.OUT)
    GPIO.output(gpioNum, GPIO.LOW)

def __main__(args):

    if args.color_name is None:
        gpio = args.gpio_num
    else:
        if args.verbose:
            print('LED color: %s' % args.color_name)

        if args.color_name == 'blue':
            gpio = GPIO_BLUE
        elif args.color_name == 'green':
            gpio = GPIO_GREEN
        elif args.color_name == 'red':
            gpio = GPIO_RED
        elif args.color_name == 'yellow':
            gpio = GPIO_YELLOW
        else:
            print('Color not found, using color blue')

    if args.set_led == 'on':
        ledOn(gpio)
        if args.verbose:
            print('LED GPIO %d on' % gpio)
    elif args.set_led == 'off':
        ledOff(gpio)
        if args.verbose:
            print('LED GPIO %d off' % gpio)

parser = argparse.ArgumentParser(description='This is script to turn on or off LEDs from RaspberryPi GPIO.')
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument('-s','--set-led', help="Set the LED ('on', 'off'), default: %s" % DEFAULT_LED, default=DEFAULT_LED)
parser.add_argument('-g','--gpio-num', help='Number for the GPIO input, default: %s' % DEFAULT_GPIO, type=int, default=DEFAULT_GPIO)
parser.add_argument('-c','--color-name', help="Color name: 'blue', 'green', 'red' and 'yellow'")
args = parser.parse_args()

# RUN
__main__(args)