# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 12:15:54 2018

@author: Balasubramaniam
"""

#type conversions

#hex form conversion
memoryAddress=255;
hexData=hex(memoryAddress)
print(hexData);
print("Memory Address in hex form %X" %(memoryAddress));
#complex Number
real=56;
imaginary=45;
print(complex(real,imaginary));
#binary to decimal
print(int('10010',2));
#decimal to binary
print(bin(56));

from datetime import date;
#format the date
print(date.today().strftime("%d/%m/%Y"));

#multiple assignments
ipaddress=copyaddress='178.8.8.91';
print(ipaddress,'=>',copyaddress);








