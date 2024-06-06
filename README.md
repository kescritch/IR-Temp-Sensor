# MLX90614 Temperature Sensor with Adafruit FT232H

## Overview:

This program uses the MLX90614 infrared temperature sensor and Adafruit FT232H to measure ambient and object temperatures via I2C. It displays real-time data on a GUI and logs the data to an Excel file.

## Features:
- Ambient & Object Temperature Measurement: Using the MLX90614 sensor.
- Real-Time Graphing: Displays data on a GUI.
- Data Logging: Saves data to an Excel file.

## Installation:
1. Set up hardware: Connect MLX90614 to FT232H via I2C (SCL and SDA), then connect FT232H to the computer.
2. Create virtual environment
3. Download requirements using `pip install -r requirements.txt`

## Code Structure
- main.py: Main script for initialization.
- irRunner.py: Handles I2C communication with the MLX90614 sensor.
- uiRunner.py: Manages the GUI, data collection, and Excel logging. 
