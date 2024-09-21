'''
Name: Kori Caldarone
Assignment: Week 3 Critical Thinking Part 2
Professor: Professor Schwartz
Date: 8/23/2024
'''
currentHour = 13
hourCount = 0
isAlarmRinging = False

while isAlarmRinging == False:
    hourCount = hourCount + 1
    currentHour = currentHour + 1
    if hourCount == 50:
        print("The alarm has rung! It has been " + str(hourCount) + " hours since the alarm was set and it is now " + str(currentHour) + ":00.")
        isAlarmRinging = True
    else:
        if currentHour == 24:
            currentHour = 0
        print("It is currently " + str(currentHour) + ":00. \n It has been "+ str(hourCount) + " hours since the alarm has been set. \n This leaves " + str(50-hourCount) + " hours to go.")
