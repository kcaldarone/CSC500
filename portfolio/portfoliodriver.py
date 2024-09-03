'''
Name: Kori Caldarone
Assignment: Week 4 Portfolio Milestone
Professor: Professor Schwartz
Date: 9/3/2024
'''
#Part 1
#making the class
class ItemToPurchase:
    def __init__(self,item_name,item_price,item_quantity):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
#initializing attributes
item_name = "None"
item_price = 0
item_quantity = 0
#creating the method
def print_item_cost(item):
    print(str(item.item_name) + " " + str(item.item_quantity) + " @ $" + str(item.item_price) + " = $" + str(item.item_quantity * item.item_price) + "\n")

#Part 2
#making Item 1 and Item 2
Item1 = ItemToPurchase(str(input("Enter the item name: \n")), int(input("Enter the item price: \n")), int(input("Enter the item quantity:\n")))
Item2 = ItemToPurchase(str(input("Enter the item name: \n")), int(input("Enter the item price: \n")), int(input("Enter the item quantity:\n")))

#Part 3
print("TOTAL COST:\n")
print_item_cost(Item1)
print_item_cost(Item2)
#adding totals together and printing it
print("Total: $" + str((Item1.item_price*Item1.item_quantity) + (Item2.item_price*Item2.item_quantity)))