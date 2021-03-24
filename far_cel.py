#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:36:36 2021

@author: sajinijoby
"""

# python program for temperature in degree celsius and convert into degree Farenheit.
# change this value into degree farenheit

celsius = 37.5
#calculate farenheit
farenheit = (celsius * 1.8) + 32
print(farenheit)

#python program for convert farenheit to celsius
fareheit =98
#calculate celsius
celsius = (farenheit - 32) * 5 / 9
print(celsius)

while True:
   cel = input('what is the degree in celsius')
   far = (float(cel) * 1.8) + 32
   print(far)
   
   far = input('what is the degree in farenheit')
   cel = (float(far) - 32) * 5 / 9
   print(cel)
   break
