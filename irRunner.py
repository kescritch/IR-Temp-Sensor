from board import *
from adafruit_bus_device.i2c_device import I2CDevice

from pandas import DataFrame

#use $env:BLINKA_FT232H=1 for env

#Constants
# for mlx sensor
ADDRESS = 0x5a
TOBJ = 0x07
AMB = 0x06

# creating I2C
i2c = I2C()
i2c_dev = I2CDevice(i2c, ADDRESS)
buff = bytearray(2)

check = False



def objTemp(buff): #Getting object temperature 

  buff[0] = (TOBJ)
  i2c_dev.write_then_readinto(buff, buff, out_end=1)
  return(temp_c(buff))

def ambTemp(buff):#Getting ambient temperature 

  buff[0] = (AMB)
  i2c_dev.write_then_readinto(buff, buff, out_end=1)
  return(temp_c(buff))

def temp_c(data): #Converting output to C 

  value = data[1] << 8 | data[0]
  temp = ((value*.02) - 273.15)
  return temp

def printer(): #Returns the temps as a string
    print ((round(objTemp(buff),2),(round(ambTemp(buff),2))))


  
  
     

