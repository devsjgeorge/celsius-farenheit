#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:36:36 2021

@author: sajinijoby

This is a sample program to interactively convert C > F and F > C.

"""


print("Welcome to Temperature Convertor!")

while True:
   # print("Please choose, c - convert to celsius; f - convert to farenheit; q - quit")
   user_choice = input("Choose, c - convert to celsius; f - convert to farenheit; q - quit # ")
   if (user_choice == 'q'):
       break;
   elif (user_choice == 'c'):
       far = input('What is the degree in farenheit?: ')
       cel = round((float(far) - 32) * 5 / 9,2)
       print("Converted temperature is: "+str(cel)+" C")
   elif (user_choice == 'f'):
       cel = input('What is the degree in celsius?: ')
       far = round((float(cel) * 1.8) + 32,2)
       print("Converted temperature is: "+str(far)+" F")
   else :
       print("I dont understand your choice; Please try again!")
   
print("Thank you for using Temperature Converter")
   # break
