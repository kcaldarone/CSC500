'''
Name: Kori Caldarone
Assignment: Week 5 Critical Thinking Part 2
Professor: Professor Schwartz
Date: 9/11/2024
'''

booksPurchased = int(input("How many books have you bought this month? \n"))
if booksPurchased >= 8:
    print("You have earned 60 points!")
elif booksPurchased >= 6:
    print("You have earned 30 points!")
elif booksPurchased >= 4:
    print("You have earned 15 points!")
elif booksPurchased >= 2:
    print("You have earned 5 points!")
else:
    print("You sadly have not purchased enough books to earn any points...")