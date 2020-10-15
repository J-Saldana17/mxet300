# L3_telemetry.py
# This program grabs data from the onboard sensors and log data in files
# for NodeRed access and integrate into a custom "flow".
# Access nodered at 192.168.8.1:1880 (by default, it's running on the Blue)

# Import Internal Programs
import L1_mpu as mpu
import L2_log as log
import L1_adc as adc
import L1_bmp as bmp

# Import External programs
import numpy as np
import time

# Run the main loop
while True:
    dcvoltage = adc.getDcJack()
    print("Voltage is:", dcvoltage)
    #log.uniqueFile(dcvoltage,"voltage.txt") ## use this function for the lab activity
    accel = mpu.getAccel()                          # call the function from within L1_mpu.py
    (xAccel) = accel[0]                             # x axis is stored in the first element
    (yAccel) = accel[1]                             # y axis is stored in the second element
    (zAccel) = accel[2]
    print("x axis:", xAccel, "y axis:", yAccel, "z axis", zAccel)     # print the two values
    axes = np.array([xAccel, yAccel, zAccel])               # store just 2 axes in an array
    print(axes)
    Temp = bmp.temp()
    Pres = bmp.pressure()
    Alt = bmp.altitude()
    print("temperature is:", Temp)
    print("altitude is:", Alt)
    print("pressure is:", Pres)
    log.uniqueFile(xAccel, "xAccel.txt")
    log.uniqueFile(yAccel, "yAccel.txt")
    log.uniqueFile(zAccel, "zAccel.txt")
    log.uniqueFile(dcvoltage, "volt.txt")
    log.uniqueFile(Temp, "temp.txt")
    log.uniqueFile(Alt, "Alt.txt")
    log.uniqueFile(Pres, "Pres.txt")
    
    # send the data to txt files for NodeRed to access.
    # log.uniqueFile(xAccel,"xAccel.txt")           # another way to log data for NodeRed access
    # log.uniqueFile(yAccel,"yAccel.txt")
    # log.tmpFile(xAccel,"xAccel.txt")              # another way to lof data for NodeRed access
    # log.tmpFile(yAccel,"yAccel.txt")
    time.sleep(0.2)
