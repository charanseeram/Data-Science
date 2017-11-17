# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:25:57 2017

@author: Saicharan.S
"""

#In python, strings can be stored in Double Quotes/Single Quotes
nameDQ = "Sreeni Jilla"
print(type(nameDQ))

nameSQ = 'Sreeni Jilla'
print(type(nameSQ))

#Access string content
name = 'Sreeni Jilla'
print(name[0])

#slicing
print(name[0:8])

#Modify string content
name[0] = 'A' #TypeError: 'str' object does not support item assignment, Replacing the content directly is NOT allowed in python, instead concatenate
name = name + 'xyz' #You can concatinate
print(name)

#Replace function
name = name.replace(name, name.upper())
print(name)

#instance: Check for instance comparision
isinstance(name, str) #True
isinstance(name, int) #False