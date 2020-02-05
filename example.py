#!/usr/bin/python3
#
# Example for using the class for the SEEED Grove 16x2 Black on Yellow display, sku 104020113
# License GPL2
#
# connect the display to he Raspberry Pi:
#   J1     Raspberry Pi
#   ---    -------------------
#   GND -> Ground,       pin 6
#   VCC -> 3.3V,         pin 1
#   SDA -> GPIO 2 (SDA), pin 3
#   SCL -> GPIO 3 (SCL), pin 5
#
# 2020-02-04 v0.1  - First version


import seeed_display
import time


###############  Main progam ###################
myDisplay = seeed_display.sku104020113()
# display_init()

#              "0123456789012345"
myDisplay.print('Raspberry Pi')

# go to the second line
myDisplay.setCursor(0,1)
#              "0123456789012345"
myDisplay.print('display')

myDisplay.setCursor(2,1)
myDisplay.blink()

time.sleep(5)
myDisplay.cursor()

time.sleep(3)
myDisplay.noBlink()

time.sleep(3)
myDisplay.noCursor()

myDisplay.rightToLeft()
myDisplay.setCursor(10,1)
myDisplay.print('xyz')

time.sleep(3)
myDisplay.leftToRight()
myDisplay.setCursor(10,1)
myDisplay.print('abc')

# end
