#
# class for using the SEEED Grove 16x2 Black on Yellow display, sku 104020113
# License GPL2
#
# Not implemented all the Arduino calls, but the most used:
#   begin, write, print, setCursor, leftToRight, RightToLeft, cursor, noCursor, blink, NoBlink
#
# 2020-02-03 v0.1  - First version
# 2020-02-04 v0.2  - Some cleanup


import smbus
import time

# the defaults for i2c bus 1 with the SEEED display
DEVICE_BUS        = 1
DEVICE_ADDR       = 0x3e

### define display control char
# send a control command to the display
DISPLAY_CTRL      = 0x80
# send a character to the display
DISPLAY_CHAR      = 0x40
## define display constants
DISPLAY_CLR       = 0x01
# set direction and scroll or not
DISPLAY_IS        = 0x04
LEFT2RIGHT        = 0x02
## display on/off control
DISPLAY_CMD       = 0x08
BLINK_ON          = 0x01
CURSOR_ON         = 0x02
DISPLAY_ON        = 0x04
## display function set
DISPLAY_FNC       = 0x20
D5X11_DOTS        = 0x04
TWO_LINES         = 0x08
## set the address for the cursor
DISPLAY_LOC       = 0x80
# Line length or this display
NEXT_LINE         = 0x40


class sku104020113:
  # the SEEED Grove 16x2 Black on Yellow display
  def __init__(self, bus = DEVICE_BUS, addr = DEVICE_ADDR):
    self.__bus               = smbus.SMBus(bus)
    self.__addr              = addr

    # the variabeles for the state of some propperties
    self.__display_flg_is    = 0x00
    self.__display_flg_cmd   = 0x00
    self.__display_flg_fnc   = 0x00

    # init the display 
    self.begin()
  

  def begin(self):
    # set the display function, 5*8, 2 line mode
    self.__display_flg_fnc = TWO_LINES
    self.__bus.write_byte_data(self.__addr, DISPLAY_CTRL, DISPLAY_FNC | self.__display_flg_fnc)
    time.sleep(0.001)
  
    # set the display on/off, no cursor, no blinking
    self.__display_flg_cmd = DISPLAY_ON
    self.__bus.write_byte_data(self.__addr, DISPLAY_CTRL, DISPLAY_CMD | self.__display_flg_cmd)
    time.sleep(0.001)
  
    # clear the display
    self.__bus.write_byte_data(self.__addr, DISPLAY_CTRL, DISPLAY_CLR)
    time.sleep(0.002)
    
    # entry mode set
    # set direction and shift
    self.__display_flg_is = LEFT2RIGHT
    self.__bus.write_byte_data(self.__addr, DISPLAY_CTRL, DISPLAY_IS | self.__display_flg_is)
  

  def setCursor(self, col, row):
    # set the cursor at a specific location
    position = col + NEXT_LINE * row
    self.__bus.write_byte_data(self.__addr, DISPLAY_CTRL, DISPLAY_LOC | position)
 
 
  def blink(self):
    # set the current character to blink
    self.__display_flg_cmd   |=  BLINK_ON
    self.__bus.write_byte_data(self.__addr, DISPLAY_CTRL, DISPLAY_CMD | self.__display_flg_cmd)

  def noBlink(self):
    # stop the current character to blink
    self.__display_flg_cmd   &= ~BLINK_ON
    self.__bus.write_byte_data(self.__addr, DISPLAY_CTRL, DISPLAY_CMD | self.__display_flg_cmd)

 
  def cursor(self):
    # set the underline for the current character
    self.__display_flg_cmd   |=  CURSOR_ON
    self.__bus.write_byte_data(self.__addr, DISPLAY_CTRL, DISPLAY_CMD | self.__display_flg_cmd)

  def noCursor(self):
    # remove the underline from the current character
    self.__display_flg_cmd   &= ~CURSOR_ON
    self.__bus.write_byte_data(self.__addr, DISPLAY_CTRL, DISPLAY_CMD | self.__display_flg_cmd)

 
  def leftToRight(self):
    # Move the cursor from left to right for the next character
    self.__display_flg_is    |=  LEFT2RIGHT
    self.__bus.write_byte_data(self.__addr, DISPLAY_CTRL, DISPLAY_IS  | self.__display_flg_is)

  def rightToLeft(self):
    # Move the cursor from right to left for the next character
    self.__display_flg_is    &= ~LEFT2RIGHT
    self.__bus.write_byte_data(self.__addr, DISPLAY_CTRL, DISPLAY_IS  | self.__display_flg_is)


  def write(self, character):
    # dislay the specified character
    self.__bus.write_byte_data(DEVICE_ADDR, DISPLAY_CHAR, ord(character))
     
  def print(self, text):
    # dislay the specified text
    for character in text[0:]:
      self.__bus.write_byte_data(DEVICE_ADDR, DISPLAY_CHAR, ord(character))
     
# end
