'''
Name: Kori Caldarone
Assignment: Week 3 Critical Thinking
Professor: Professor Schwartz
Date: 8/23/2024
'''

#User inputs meal price
total = float(input("And how much does the customer owe for the meal?\n"))
print("Alright, the customer owes $"+ str(round(total,2)) + " for their meal tonight.")

#calculating 7% tax 
taxedTotal = round((total * 1.07), 2)
taxAmt = round((taxedTotal - total), 2)

#calculating 18% tip with taxed total as tip comes after tax is added
tippedTotal = round((taxedTotal * 1.18), 2)
tipAmt = round((tippedTotal - taxedTotal), 2)

print("With a sales tax rate of 7%, the amount plus tax would be taxed $" + str(taxAmt) + ", which would bring the total to $" + str(taxedTotal) + ".\n")
print("In addition to this, if you wish to leave an 18% tip for your waitress, that would be an additional $" + str(tipAmt) + ", bringing the customer's total to $" + str(tippedTotal) +".")

