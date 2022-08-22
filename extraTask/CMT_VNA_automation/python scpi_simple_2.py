# -*- coding: utf-8 -*-
"""
Created 5/21/2021

@author: CMT

OVERVIEW:
    This script allocates 2 traces of S11 and captures phase and log mag measurement
    data into arrays of numbers 
    
    The VNA software has to be running always when automating the VNA. The VNA software
    is the driver for the VNA

Before running the code:
    1. Make sure VNA software is running
    2. S2,S4VNA:
       Go to system -> Misc setup -> network remote settings -> turn on socket server
       R,TRVNA:
       Go to system -> network setup -> interface state (on)
    3. make sure socket server is 5025

Additional information:
    1. The SCPI programming manual is intalled with the VNA software. By default:
        C:\VNA\RVNA or TRVNA or S2VNA or S4VNA\Doc
        
    
"""

import pyvisa

rm = pyvisa.ResourceManager('@py') # use pyvisa-py as backend, must install pyvisa-py 
#rm = pyvisa.ResourceManager('C:/WINDOWS/system32/visa32.dll')  # use ni visa 32 bit as backend, must install NI VISA
#rm = pyvisa.ResourceManager('C:/WINDOWS/system32/visa64.dll')  # use ni visa 64 bit as backend, must install NI VISA

#Connect to a Socket on the local machine at 5025
try:
    CMT = rm.open_resource('TCPIP0::127.0.0.1::5025::SOCKET')
except:
    print("Failure to connect to VNA!")
    print("Check network settings")
#The VNA ends each line with this. Reads will time out without this
CMT.read_termination='\n'
#Set longer timeout period for slower sweeps
CMT.timeout = 10000


###########################################
###########################################
###### start sending commands here ########
###########################################
###########################################


#CMT.write('SYST:PRESET') #becarefull this remove cal data.
CMT.write('*RST')



''' set up the VNA '''
CMT.write('DISP:SPL 2') # allocate number of channel windows 
#CMT.write('DISP:UPD')



# for Ch1
CMT.write('SENS1:FREQ:STAR 9kHz')
CMT.write('SENS1:FREQ:STOP 100MHz')
CMT.write('SENS1:SWE:POIN 1001')
CMT.write('SENS1:SWE:TYPE LOG')

CMT.write('CALC1:PAR:COUN 2') # 2 Traces
CMT.write('DISP:WIND1:SPL 2') # allocate 2 trace windows 
CMT.write('DISP:WIND1:TRAC1:Y:AUTO') # Trace 1 auto scale
CMT.write('DISP:WIND1:TRAC2:Y:AUTO') # Trace 2 auto scale
CMT.write('CALC1:PAR1:DEF S11') #Choose S11 for trace 1
CMT.write('CALC1:PAR2:DEF S12') #Choose S21 for trace 2

CMT.write('CALC1:TRACE1:CONV OFF')
CMT.write('CALC1:TRACE2:CONV OFF')



# for Ch2
CMT.write('SENS2:FREQ:STAR 9kHz')
CMT.write('SENS2:FREQ:STOP 100MHz')
CMT.write('SENS2:SWE:POIN 1001')
CMT.write('SENS2:SWE:TYPE LOG')

CMT.write('CALC2:PAR:COUN 2') # 2 Traces
CMT.write('DISP:WIND2:SPL 2') # allocate 2 trace windows 
CMT.write('DISP:WIND2:TRAC1:Y:AUTO') # Trace 1 auto scale
CMT.write('DISP:WIND2:TRAC2:Y:AUTO') # Trace 2 auto scale
CMT.write('CALC2:PAR1:DEF S11') #Choose S11 for trace 1
CMT.write('CALC2:PAR2:DEF S12') #Choose S21 for trace 2

CMT.write('CALC2:TRACE1:CONV ON')
CMT.write('CALC2:TRACE2:CONV ON')