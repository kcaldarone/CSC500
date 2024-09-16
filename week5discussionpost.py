'''
#AND OPERATORS
drinks = ["Tea", "Coffee", "Orange Juice", "Water", "Wine", "Beer", "Vodka"]
x = 0 #make count
print("All drinks with 5-10 letters:")
while x < len(drinks):
    if(len(drinks[x]) >= 5 and len(drinks[x]) <= 10):
        print(drinks[x])
    x = x + 1

print("\n")

#OR OPERATORS
#planets = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
#i = -1 #making count 
#print("All planets that start with the letter S or are 5 letters long:")
#while i < len(planets):
   #i = i + 1
   #if(planets[i][0] == "S" or len(planets[i]) == 5):
       #print(planets[i])
    
#AND OPERATORS - DRINK SCENARIO EXTENDED
class Drink: 
    def __init__(self, name, color, brand, servingSize, alcoholPercentage, caffeineAmount, sugarAmount):
        self.name = name
        self.color = color
        self.brand = brand
        self.servingSize = servingSize #in fl oz
        self.alcoholPercentage = alcoholPercentage
        self.caffeineAmount = caffeineAmount
        self.sugarAmount = sugarAmount

drinks = ["Tea", "Coffee", "Orange Juice", "Water", "Wine", "Beer", "Vodka"]
beverages = []
beverages[0] = Drink("Black Tea", "Brown", "BIGELOW", 8, 0, 47, 0)
beverages[1] = Drink("Coffee", "Brown", "Folgers", 12, 0 ,160, 0)
beverages[2] = Drink("Orange Juice", "Orange", "Simply Beverages", 8, 0, 0, 23)
beverages[3] = Drink("Distilled Water", "Clear", "Dasani", 16.9, 0, 0, 0)
beverages[4] = Drink("Red Wine", "Crimson", "Penfolds", 5, 14.5, 0, 1)
beverages[5] = Drink("Beer", "Tan", "Bud Light", 25, 4.2, 0, 0)
beverages[6] = Drink("Vodka", "Clear", "Smirnoff", 1.5, 50, 0, 0)

count = 0
print("Beverages with Alcohol and Sugar")
while count < len(beverages):
    if(beverages[count].alcholPercentage > 0 and beverages[count].sugarAmount > 0):
        print(beverages[count].name)
    count = count + 1
'''

print("Beverages with Alcohol and Sugar")
print("Red Wine")