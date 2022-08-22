# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:32:27 2020

@author: Patrick.l
"""

import pyvisa    #PyVisa is required along with NIVisa
import subprocess
import time 

# Concept:
# The complete calibration process is:
# 1) select cal kit definition
# 2) physically connect the cal kit standards and measure the standards
# 3) select calibration type (full 1 port cal, full 2 port cal, response open cal, response short cal, etc.)
# 4) apply calibration

# When automating standards' measurements, the subclass of each standard must be selected first 
# (this is done using SCPI command "SENS:CORR:COLL:SUBC <number>"). 
# If subclass is not selected, the last selected subclass is used

# connect to VNA software
rm = pyvisa.ResourceManager('@py')  # uses pyvisa-py
#rm = pyvisa.ResourceManager('C:/WINDOWS/system32/visa32.dll')  # uses ni visa 32 bit
#rm = pyvisa.ResourceManager('C:/WINDOWS/system32/visa64.dll')  # uses ni visa 64 bit

#Connect to a Socket on the local machine at 5025
#Use the IP address of a remote machine to connect to it instead
try:
    CMT = rm.open_resource('TCPIP0::127.0.0.1::5025::SOCKET')
except:
    print("Failure to connect to VNA!")
    print("Check network settings")
#The VNA ends each line with this. Reads will time out without this
CMT.read_termination='\n'
#Set a really long timeout period for slow sweeps
CMT.timeout = 10000

###########################################
###########################################
###### send SCPI commands here ############
###########################################
###########################################

#CMT.query('*RST')

# Set Channel and display
#CMT.write('CALC1:PAR:COUN 3') # 3 Traces
#CMT.write('DISP:WIND1:SPL 6') # allocate 3 traces on 1 Horizontal and 2 vertical window
CMT.write('CALC1:PAR:COUN 4') # 4 Traces
CMT.write('DISP:WIND1:SPL 8') # allocate 4 traces on window
#CMT.write('DISP:WIND1:TRAC1:Y:AUTO') # Trace 1 auto scale
CMT.write('DISP:WIND1:TRAC2:Y:PDIV 20') # Trace 2 Scale Value
CMT.write('DISP:WIND1:TRAC2:Y:RLEV -60') # Trace 2 Ref Value
CMT.write('DISP:WIND1:TRAC3:Y:PDIV 20') # Trace 3 Scale Value
CMT.write('DISP:WIND1:TRAC3:Y:RLEV -60') # Trace 3 Ref Value
CMT.write('DISP:WIND1:TRAC4:Y:PDIV 20') # Trace 4 Scale Value
CMT.write('DISP:WIND1:TRAC4:Y:RLEV -60') # Trace 4 Ref Value

CMT.write('CALC1:PAR1:DEF S11') # Choose S11 for trace 1
CMT.write('CALC1:TRAC1:FORM SLOG') # Smith Log
CMT.write('CALC1:PAR2:DEF S11') # Choose S11 for trace 2
CMT.write('CALC1:TRAC2:FORM MLOG') # Mag Log
CMT.write('CALC1:PAR3:DEF S21') # Choose S21 for trace 3
CMT.write('CALC1:TRAC3:FORM MLOG') # Mag Log
CMT.write('CALC1:PAR4:DEF S22') # Choose S22 for trace 4
CMT.write('CALC1:TRAC4:FORM MLOG') # Mag Log

CMT.query("*OPC?")

#To recorver from Conversion function
CMT.write('CALC1:TRACE1:CONV OFF')
CMT.write('CALC1:TRACE2:CONV OFF')
CMT.write('CALC1:TRACE3:CONV OFF')
CMT.query("*OPC?")
print("Display&Channel setting done!\n")

CMT.write('SENS1:FREQ:STAR 20kHz') # min start frq of ACM is 20Hz
CMT.write('SENS1:FREQ:STOP 6GHz') # max stop frq of ACM is 6GHz
CMT.write('SENS1:SWE:POIN 401') # default 201
CMT.write('SENS1:SWE:TYPE LOG')
CMT.query("*OPC?")
print("Frequency setting done!\n")

# AutoCal Procedure
print("Make sure connected ACM6000T")

CMT.write('TRIG:SOUR INIT')
CMT.query("*OPC?")

# Cal Charaterization
CMT.write('SENS:CORR:COLL:ECAL:UCH CHAR0') #CHAR0 is Factory value, 0 to 3
CMT.query("*OPC?")

# AutoCal Orientation
CMT.write('SENS:CORR:COLL:ECAL:ORI:STAT')
CMT.query("*OPC?")
CMT.write('SENS:CORR:COLL:ECAL:ORI:EXEC')
CMT.query("*OPC?")
CMT.write('SENS:CORR:COLL:ECAL:ORI:PATH')
CMT.query("*OPC?")

# Unknown Thru, when you use personal through
CMT.write('SENS:CORR:COLL:ECAL:UTHR:STAT 1')
CMT.query("*OPC?")

# Display Chracterization Info
#CMT.write('SENS:CORR:COLL:ECAL:INF?')

# Two port calibration
CMT.write("SENS1:CORR:COLL:ECAL:SOLT2") # 2-port AutoCal for ch1
CMT.query("*OPC?")
#CMT.write("SENS2:CORR:COLL:ECAL:SOLT2") # 2-port AutoCal for ch2
#CMT.query("*OPC?") # make sure the measurement is completed
print("2-port AutoCal is completed")

'''
# Confidence check to verify calibration
CMT.write('SENS:CORR:COLL:ECAL:UCH CHAR0')
CMT.write('SENS:CORR:COLL:ECAL:CCH')
'''

CMT.write('TRIG:SOUR INIT')
CMT.query("*OPC?")
CMT.write('INIT:CONT:ALL 1')
CMT.query("*OPC?")

