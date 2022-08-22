# -*- coding: utf-8 -*-
"""
Created on 10/1/2020

OVERVIEW:
    This script takes one S11 measurement every 10 minutes and save the data in .csv
    files under the same directory as this script lies.
    
    The VNA software has to be running always when automating the VNA. The VNA software
    is the driver for the VNA

Before running the code:
    1. Make sure S2VNA software is running
    2. Go to system -> Misc setup -> network remote settings -> turn on socket server
    3. make sure socket server is 5025

Additional information:
    1. The SCPI programming manual is intalled with the VNA software. By default:
        C:\VNA\S2VNA\Doc\
    
"""

import pyvisa    #PyVisa is required along with NIVisa
from time import sleep
import os 


rm = pyvisa.ResourceManager('@py')
#Connect to a Socket on the local machine at 5025
#Use the IP address of a remote machine to connect to it instead
try:
    CMT = rm.open_resource('TCPIP0::localhost::5025::SOCKET')
except:
    print("Failure to connect to VNA!")
    print("Check network settings")
#The VNA ends each line with this. Reads will time out without this
CMT.read_termination='\n'
#Set a really long timeout period for slow sweeps
CMT.timeout = 10000


###########################################
###########################################
######try stuff here#######################
###########################################
###########################################


# Set Channel and display
#CMT.write('CALC1:PAR:COUN 3') # 3 Traces
#CMT.write('DISP:WIND1:SPL 6') # allocate 3 traces on 1 Horizontal and 2 vertical window
CMT.write('CALC1:PAR:COUN 4') # 4 Traces
CMT.write('DISP:WIND1:SPL 8') # allocate 4 traces on window
#CMT.write('DISP:WIND1:TRAC1:Y:AUTO') # Trace 1 auto scale
CMT.write('DISP:WIND1:TRAC1:Y:PDIV 10') # Trace 2 Scale Value
CMT.write('DISP:WIND1:TRAC1:Y:RLEV -40') # Trace 2 Ref Value
CMT.write('DISP:WIND1:TRAC2:Y:PDIV 10') # Trace 2 Scale Value
CMT.write('DISP:WIND1:TRAC2:Y:RLEV -40') # Trace 2 Ref Value
CMT.write('DISP:WIND1:TRAC3:Y:PDIV 10') # Trace 3 Scale Value
CMT.write('DISP:WIND1:TRAC3:Y:RLEV -40') # Trace 3 Ref Value
CMT.write('DISP:WIND1:TRAC4:Y:PDIV 10') # Trace 4 Scale Value
CMT.write('DISP:WIND1:TRAC4:Y:RLEV -40') # Trace 4 Ref Value

CMT.write('CALC1:PAR1:DEF S11') # Choose S11 for trace 1
CMT.write('CALC1:TRAC1:FORM MLOG') # Mag Log
#CMT.write('CALC1:TRAC1:FORM SLOG') # Smith Log
CMT.write('CALC1:PAR2:DEF S12') # Choose S21 for trace 2
CMT.write('CALC1:TRAC2:FORM MLOG') # Mag Log
CMT.write('CALC1:PAR3:DEF S21') # Choose S11 for trace 3
CMT.write('CALC1:TRAC3:FORM MLOG') # Mag Log
CMT.write('CALC1:PAR4:DEF S22') # Choose S21 for trace 4
CMT.write('CALC1:TRAC4:FORM MLOG') # Mag Log

CMT.query("*OPC?")

'''
#To recorver from Conversion function
# ON for S-parameter Conversino to Z
CMT.write('CALC1:TRACE1:CONV OFF')
CMT.write('CALC1:TRACE2:CONV OFF')
CMT.write('CALC1:TRACE3:CONV OFF') 
CMT.write('CALC1:TRACE4:CONV OFF')
CMT.query("*OPC?")
'''
print("\nDisplay&Channel setting done!\n")

CMT.write('SENS1:FREQ:STAR 0kHz') # min start frq of ACM is 20Hz
CMT.write('SENS1:FREQ:STOP 0.1GHz') # max stop frq of ACM is 6GHz
CMT.write('SENS1:SWE:POIN 501') # default 201
CMT.write('SENS1:SWE:TYPE LOG')
CMT.query("*OPC?")
print("Frequency setting done!\n")


####### Start Measurement Setup ########

CMT.write("TRIG:SOUR BUS\n")
CMT.query("*OPC?\n")

# get the directory where this python script is located, the csv file will be saved in the same folder
file_path = os.path.dirname(os.path.realpath(__file__))
for i in range(2): # Change repeat count
    CMT.write("TRIG:SING\n")
    CMT.query("*OPC?\n")
    CMT.write('DISP:WIND:ACT') # Select an window
    #CMT.write('CALC:PAR:SEL') # Select a trace
    command = 'MMEM:STOR:FDAT ' + '"' + file_path + '/data' + '{}'.format(i) + '.csv"' + '\n'
    CMT.write(command)
    print('data' + '{}'.format(i)+'.csv has been generated.')
    sleep(1)   # seconds, change waiting time
 
CMT.write("TRIG:SOUR INT\n")
print('\nMeasurement Completed!!!')


