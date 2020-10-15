# Import Internal Programs
import L2_kinematics as kin   #import kinematics program in order to use getPdCurrent()
                              #and getMotion() functions
import L2_log as log          #imprt log program in order to use uniqueFile() function
import L2_heading as head

# Import External programs
import numpy as np
import time

def task():
    a = kin.getPdCurrent()  #function returns both phi-dot values from motor
    b = kin.getMotion()  #function returns x-dot and theta-dot values from motor
    axes=head.getXY()
    scaledaxes=head.scale(axes)
    h=head.getHeading(scaledaxes)
    hDegrees = round(h*180/np.pi, 2)
    print('Pdr and Pdl values are:')  #prints out values for Pdr and Pdl
    print(a)   
    print('motion values are:')  #prints out values for x-dot and theta-dot
    print(b)
    
    log.uniqueFile(a[0], "task2pdl.txt")  #use unique file to save pdl to a txt file
                                          #rather than a temporary folder that would be
                                          #created with tempFile
    log.uniqueFile(a[1], "task2pdr.txt")  #save unique file for pdr
    
    log.uniqueFile(b[0], "task2xDot.txt")  #save unique file for x-dot
    log.uniqueFile(b[1], "task2thetaDot.txt")  #save unique file for theta-dot
    log.uniqueFile(hDegrees, "heading.txt")

    
while True:  #run program continuously with sleep time of 0.2 seconds
    task()
    time.sleep(0.2)