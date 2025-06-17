from fastmcp import FastMCP # This is the MCP Library
import pyfirmata2 # This is the library to control arduino with python 


# Here we are saying this is the arduino 
Arduino = pyfirmata2.Arduino('/dev/cu.usbmodem212201') # This is my COM port. Change to your COM port


ArduinoMCP = FastMCP('Arduino Servers')


# LED pin definitions
WHITE_LED_PIN = 12
RED_LED_PIN = 11

# @ArduinoMCP.tool is a python decorator which is wrapping our functions to be exposed to the MCP Client (Claude Desktop) 
@ArduinoMCP.tool
def white_led_ON():
    '''Turns on white LED in the Arduino'''
    Arduino.digital[WHITE_LED_PIN].write(1)
    return 'White LED ON'

@ArduinoMCP.tool
def red_led_ON():
    '''Turns on red LED in the Arduino'''
    Arduino.digital[RED_LED_PIN].write(1)
    return 'Red LED ON'

@ArduinoMCP.tool
def led_OFF():
    '''Turns off all LEDs in the Arduino'''
    Arduino.digital[RED_LED_PIN].write(0)
    Arduino.digital[WHITE_LED_PIN].write(0)
    return 'All LEDs OFF'


if __name__ == "__main__":
    ArduinoMCP.run() #Lets run our MCP server :)
  