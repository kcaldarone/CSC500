'''
Name: Kori Caldarone
Assignment: Week 4 Portfolio Milestone
Professor: Professor Schwartz
Date: 9/3/2024
'''
#Part 1
#making the class
class ItemToPurchase:
    def __init__(self,item_name,item_price,item_quantity,item_description):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
#initializing attributes
item_name = "None"
item_price = 0
item_quantity = 0
#creating the method
def print_item_cost(item): #doesn't print for some reason
    print(item.item_name + " " + str(item.item_quantity) + " @ $" + str(item.item_price) + " = $" + str(item.item_quantity * item.item_price) + "\n")

#Part 2
#making Item 1 and Item 2

#COMMENTING THIS OUT SO IT DOESNT INTERFERE WITH WEEK 6 MATERIAL
'''
Item1 = ItemToPurchase(str(input("Enter the item name: \n")), int(input("Enter the item price: \n")), int(input("Enter the item quantity:\n")), str(input("Enter the item description:\n")))
Item2 = ItemToPurchase(str(input("Enter the item name: \n")), int(input("Enter the item price: \n")), int(input("Enter the item quantity:\n")), str(input("Enter the item description:\n")))

#Part 3
print("TOTAL COST:\n")
print_item_cost(Item1)
print_item_cost(Item2)
#adding totals together and printing it
print("Total: $" + str((Item1.item_price*Item1.item_quantity) + (Item2.item_price*Item2.item_quantity)))
'''
#WEEK 6 CHECK IN!
'''
Name: Kori Caldarone
Assignment: Week 6 Portfolio Milestone
Professor: Professor Schwartz
Date: 9/16/2024
'''
#Part 4
class ShoppingCart:
    def __init__(self,customer_name,current_date,cart_items):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
    
global customer_name, current_date, cart_items #making them global so they can reach the functs
customer_name = "none"
current_date = "January 1, 2020"
cart_items = []

def create_item(): #added this so the customer can describe the item they want
    return ItemToPurchase(str(input("Enter the item name: \n")), int(input("Enter the item price: \n")), int(input("Enter the item quantity:\n")), str(input("Enter the item description:\n")))

def add_item(item):
     cart_items.append(item)
     print(item.item_name + " has been added to the cart!")

def remove_item(item_name):
      matchCount = 0
      for item in cart_items:
        if item.item_name == item_name:
            cart_items.remove(item)
            matchCount = matchCount + 1
            print("We have removed " + item_name + " from your cart!")
      if matchCount < 1:
          print("Item not found in list. Nothing removed.")

def modify_item(item_name):
    matchCount = 0
    for item in cart_items:
        if item_name == item.item_name:
            if item.item_price == 0 and item.item_quantity == 0:
              print("This item is the base, can not be modified")
            else:
              item = ItemToPurchase(item.item_name,item.item_price, int(input("Enter the item quantity:\n")),item.item_description)
              print(item.item_name + " now has a quantity of " + str(item.item_quantity) + "!\n")
              matchCount = matchCount + 1
    if matchCount < 1:
        print("This item is not in this cart. Nothing modified")

def get_num_items_in_cart():
    count = 0
    for i in cart_items:
        count = count + i.item_quantity
    return count

def get_cost_of_cart():
    totalAmt = 0
    for i in cart_items:
        totalAmt = totalAmt + (i.item_price * i.item_quantity)
    print("Total: $" + str(totalAmt))

def print_total(cart):
    print(cart.customer_name + "'s Shopping Cart - " + cart.current_date)
    print("Number of Items: " + str(get_num_items_in_cart()))
    for i in cart.cart_items:
        print_item_cost(i)
        print("test")
    get_cost_of_cart() #reaches

def print_descriptions(cart):
    print(cart.customer_name + "'s Shopping Cart - " + cart.current_date + "\nItem Descriptions")
    for i in cart.cart_items:
        print(i.item_name + ": " + i.item_description + "\n")

#Part 5 - Menu
def print_menu(cart):
    hasNotQuit = True
    while hasNotQuit:
        action = input("MENU\n\nWelcome to the Stardust Superstore. How can I help you today?\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items descriptions\no - Output shopping cart\nq - Quit\n")
        if action == "q":
            print("Have a nice day!") #works! :D
            hasNotQuit = False
        elif action == "a":
            add_item(create_item()) #works! :D
        elif action == "r":
            remove_item(input("What item would you like to remove?\n")) #works! :D
        elif action == "c":
            modify_item(input("What item would you like to modify?\n")) #works! :D
        elif action == "i":
            print_descriptions(cart)  #doesn't work, working on it :(
        elif action == "o":
            output_cart(cart) #doesn't work, working on it :(
        else:
            print("This is not a valid option, please try again.\n") #works! :D

#Part 6 - Outputting Cart
def output_cart(cart):
    print("OUTPUT SHOPPING CART")
    print_total(cart)

def main():
    cart = ShoppingCart(input("Before we begin your shopping experience here at the Stardust Superstore, what is your name?\n"),input("And what is the current date?\n"),[])
    print_menu(cart)  
    #apple = ItemToPurchase("Apple",3,1,"apple") #was testing
    #print_item_cost(apple)
main()