from board import *
from adafruit_bus_device.i2c_device import I2CDevice

#use $env:BLINKA_FT232H=1 for env

#Constants
ADDRESS = 0x5a
TOBJ = 0x07
AMB = 0x06

# creating I2C device
i2c = I2C()
i2c_dev = I2CDevice(i2c, ADDRESS)

inputBuff = bytearray(2)
outputBuff = bytearray(2)

def objTemp(inputBuff,outputBuff):  #Getting object temperature 
  inputBuff[0] = (TOBJ)
  i2c_dev.write_then_readinto(inputBuff, outputBuff, out_end=1) #Sending command buffer 
  return(temp_c(outputBuff))

def ambTemp(inputBuff,outputBuff):  #Getting ambient temperature 
  inputBuff[0] = (AMB)
  i2c_dev.write_then_readinto(inputBuff, outputBuff, out_end=1) #Sending command buffer 
  return(temp_c(outputBuff))

def temp_c(data): #Converting output to C 
  high = data[1]  #On this sensor low byte is first then high
  low = data[0]

  value = high << 8 | low   #Shifting high values over a byte then adding low byte

  temp = ((value*.02) - 273.15)   #Conversion from output to temperature from spec sheet 

  return temp

def printer():  #Returns the temps as a string
    return round(objTemp(inputBuff,outputBuff),2), round(ambTemp(inputBuff,outputBuff),2)

     

