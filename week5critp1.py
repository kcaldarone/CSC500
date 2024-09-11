'''
Name: Kori Caldarone
Assignment: Week 5 Critical Thinking Part 1
Professor: Professor Schwartz
Date: 9/11/2024

Note for Professor Schwartz: I am challenging myself with this assignment by not letting myself hard code as it is one of my pitfalls 
in my programming. Let me know how what you think and where I can approve if you can! Thank you!
'''
import numpy as np 

years = int(input("How many years would you like to look over? \n"))
monthCount = 0
yearCount = 0
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#make 2d array to store rainfall amounts
rainArr = np.zeros((years, len(months)), dtype=float)
while yearCount < years:
    while monthCount <= 11:
        rainArr[yearCount, monthCount] = float(input("How many inches of rainfall was there in " + months[monthCount] + " in year " + str(yearCount+1) + "?\n"))
        monthCount = monthCount + 1
    yearCount = yearCount + 1
    monthCount = 0

#sum print statements
print("Total number of months: " + str(len(months)*years) + "\n")
print("Total inches of rainfall: " + str(np.sum(rainArr)) + "\n")
#month print statment loop
while monthCount <= 11:
    print("Average inches of rainfall in " + months[monthCount] + ": " + str(np.sum(rainArr[:, monthCount])))
    monthCount = monthCount + 1