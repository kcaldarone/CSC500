'''
Name: Kori Caldarone
Assignment: Week 3 Critical Thinking Part 1
Professor: Professor Schwartz
Date: 8/23/2024
'''
#User inputs food price
total = float(input("And how much does the customer owe for the meal?\n"))
print("Alright, the customer owes $"+ str(total) + " for their meal tonight.")

#calculating 7% tax 
taxedTotal = total * 1.07
taxAmt = taxedTotal - total

#calculating 18% tip with taxed total as tip comes after tax is added
tippedTotal = taxedTotal * 1.18
tipAmt = tippedTotal - taxedTotal

print("With a sales tax rate of 7%, the amount plus tax would be taxed $" + str(taxAmt) + ", which would bring the total to $" + str(taxedTotal) + ".\n")
print("In addition to this, if you wish to leave an 18% tip for your waitress, that would be an additional $" + str(tipAmt) + ", bringing the customers total to $" + str(tippedTotal))

