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

'''
#this makes error msg.
CMT.query('*RST')
CMT.query("*OPC?")
'''

# Set Channel and display
CMT.write('CALC1:PAR:COUN 3') # 3 Traces
CMT.write('DISP:WIND1:SPL 6') # allocate 3 trace on 1 Horizontal and 2 vertical windows
#CMT.write('DISP:WIND1:TRAC1:Y:AUTO') # Trace 1 auto scale
#CMT.write('DISP:WIND1:TRAC2:Y:AUTO') # Trace 2 auto scale
CMT.write('DISP:WIND1:TRAC2:Y:PDIV 20') # Trace 2 Scale Value
CMT.write('DISP:WIND1:TRAC2:Y:RLEV -50') # Trace 2 Ref Value

CMT.query("*OPC?")
CMT.write('DISP:WIND1:TRAC3:Y:AUTO') # Trace 3 auto scale
CMT.query("*OPC?")
CMT.write('CALC1:PAR1:DEF S11') # Choose S11 for trace 1
CMT.write('CALC1:TRAC1:FORM SLOG') # Smith Log
CMT.write('CALC1:PAR2:DEF S11') # Choose S11 for trace 2
CMT.write('CALC1:TRAC2:FORM MLOG') # Mag Log
CMT.write('CALC1:PAR3:DEF S21') # Choose S21 for trace 3
CMT.query("*OPC?")

CMT.write('CALC1:TRACE1:CONV OFF')
CMT.write('CALC1:TRACE2:CONV OFF')
CMT.write('CALC1:TRACE3:CONV OFF')
CMT.query("*OPC?")

CMT.write('SENS1:FREQ:STAR 20kHz')
CMT.write('SENS1:FREQ:STOP 6GHz')
CMT.write('SENS1:SWE:POIN 501')
CMT.write('SENS1:SWE:TYPE LOG')
CMT.query("*OPC?")


CMT.write('TRIG:SOUR INIT')
CMT.query("*OPC?")
#CMT.write('INIT1:CONT 1')
CMT.write('INIT:CONT:ALL 1')
CMT.query("*OPC?")

