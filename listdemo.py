# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:06:59 2018

@author: Balasubramaniam
"""

deviceList=['PC-1','178.16.19.1','VLAN',8080,True];

for _ in deviceList:
    if ((type(_) != str) and (type(_) != bool)) :
       print(_);
       
for _ in deviceList:
    if (type(_) is int) :
       print(_);
       
#dynamic list
import random;
randomList=[];
for _ in range(1,5):
    randomList.append(random.randint(1,400));
print (randomList);

#sort and print
randomList.sort();

print (randomList);

#reverse and print
randomList.reverse();

print (randomList);

productIdList=[4,5,6,7,8];
productList=["Tab","PC","Mobile","Book","Printer"];
#concat operation
print(productIdList+productList);

#repetition
print(productIdList*5);

product=[];
for (id,name) in zip(productIdList,productList):
    product.append(id);
    product.append(name);
    
print(product);

#join operation
print("->".join(productList));

#nested list

deviceArr=[['PC-1','178.16.19.1','VLAN',8080,True],
           ['PC-2','178.16.19.2','SWITCH',8090,True],
           ['PC-3','178.16.19.3','ROUTER',9080,False]]

for device in deviceArr:
    for elem in device:
         if (type(elem) is str):
             if(elem.find(".")>0):
                  print(elem);
          










      
       