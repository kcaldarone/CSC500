
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
planets = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
i = -1 #making count 
print("All planets that start with the letter S or are 5 letters long:")
while i < len(planets):
   i = i + 1
   if(planets[i][0] == "S" or len(planets[i]) == 5):
       print(planets[i])
    
