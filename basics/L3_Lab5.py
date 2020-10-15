#L3_Lab5.py
# Team Number: 3
# Hardware TM: BeagleBone
# Software TM: Python, Cloud9
# Date: 10/1/20
# Code purpose: Find values for PDL, PDR, Xdot, Thetadot
#and compass direction

# Import Internal Programs
import L2_kinematics as kin   #import kinematics program in order to use getPdCurrent()
                              #and getMotion() functions
import L2_log as log          #imprt log program in order to use uniqueFile() function
import L2_heading as head     #import heading file in order to find compass direction

# Import External programs
import numpy as np
import time

def task():
    a = kin.getPdCurrent()  #function returns both phi-dot values from motor
    b = kin.getMotion()  #function returns x-dot and theta-dot values from motor
    axes=head.getXY()  #return an average heading value for x and y
    scaledaxes=head.scale(axes) #scale axes based on np array
    h=head.getHeading(scaledaxes) #returns a radian value for the heading
    hDegrees = round(h*180/np.pi, 2) #converts the heading value into degrees
    print('Pdr and Pdl values are:')  #prints out values for Pdr and Pdl
    print(a)   
    print('motion values are:')  #prints out values for x-dot and theta-dot
    print(b)
    print('heading is:') #print out the heading value in degrees
    print(hDegrees)
    
    log.uniqueFile(a[0], "task2pdl.txt")  #use unique file to save pdl to a txt file
                                          #rather than a temporary folder that would be
                                          #created with tempFile
    log.uniqueFile(a[1], "task2pdr.txt")  #save unique file for pdr
    
    log.uniqueFile(b[0], "task2xDot.txt")  #save unique file for x-dot
    log.uniqueFile(b[1], "task2thetaDot.txt")  #save unique file for theta-dot
    log.uniqueFile(hDegrees, "heading.txt") #save unique file for heading in degrees

    
while True:  #run program continuously with sleep time of 0.2 seconds
    task()
    time.sleep(0.2)