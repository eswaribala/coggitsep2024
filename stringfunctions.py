# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 14:23:18 2018

@author: Balasubramaniam
"""
courseName="python";
#first letter converted to upper case
print(courseName.capitalize());
#center the string with filler
print(courseName.center(len(courseName)+20,'*'));
#left justification
print(courseName.ljust(len(courseName)+20,'*'));
#right justification
amount="43856874"
print(amount.rjust(len(amount)+20,'*'));

#encoding and decoding with base 64 conversion
import base64;
seqNo=567;

pnrNo=base64.b64encode(str(seqNo).encode(encoding='utf-8',
                       errors='strict'));
for _ in pnrNo[0:]:
    print(chr(int(_)),end="");
#decoding
originalData=base64.b64decode(pnrNo.decode(encoding='utf-8',
                       errors='strict'));
print("\n");                                           
for _ in originalData[0:]:
    print(chr(int(_)),end="");



                                        









