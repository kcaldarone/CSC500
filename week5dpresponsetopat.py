class House: 
    def __init__(self, town, state, address, type, squareFt, price, distance, bedroomCount, bathroomCount):
        self.address = address
        self.town = town
        self.state = state
        self.type = type
        self.squareFt = squareFt
        self.price = price #in USD
        self.distance = distance #in miles
        self.bedroomCount = bedroomCount
        self.bathroomCount = bathroomCount
    
homes = []
homes[0] = House("111 Heartslabyul Lane", "Nightraven", "NY", "Ranch", 1600, 500000, 10, 2, 2)
homes[1] = House("5392 Diamonsia Boulevard", "Nightraven", "NY", "Bungalow", 1500, 450000, 15, 3, 2)
homes[2] = House("667 Ignihyde Square", "Woeville", "NY", "House", 400000, 25, 3, 2)
homes[3] = House("4924 Savanaclaw Drive", "Meston", "PA", "Cape Cod", 1800, 400000, 200, 2, 2)
homes[4] = House("5032 Octaniville Circle", "Nightraven", "NY", "Craftsman", 2500, 550000, 10, 3, 3)
homes[5] = House("12942 Pomefiore Avenue", "Appleton", "PA", "Victorian", 3000, 600000, 250, 3, 3)
homes[6] = House("4342 Scarabia Way", "Nightraven", "NY", "Cottage", 1200, 350000, 5, 2, 2)
homes[7] = House("2442 Ramshackle Road", "Nightraven", "NY", "California Bungalow", 1600, 400000, 5, 2, 2)

#get desires of user
desiredSize = int(input("How many square feet would you like your future house to have?\n"))
desiredPrice = int(input("How much are you willing to spend for your future home?\n"))
desiredBathrooms = int(input("How many bathrooms do you want in your future house?\n"))
desiredBedrooms = int(input("How many bedrooms do you want in your future house?\n"))
desiredDistance = int(input("How many miles out from your current home would you like to live?\n"))
isOutOfState = bool(input("Are you willing to go out of state? True or False?\n"))

#finding houses for user
i = 0
if i < len(homes):
   if homes[i].squareFt >= desiredSize and homes[i].price <= desiredPrice and homes[i].distance <= desiredDistance and homes[i].bathroomCount == desiredBathrooms or homes[i].bedroomCount == desiredBedrooms:
        print("We have a lovely for you in " + homes[i].city + ", " + homes[i].state + "!\n It is a lovely "  + homes[i].type + " with the address of " + homes[i].address + "!\n It has " + homes[i].squareFt + " square feet of space, " + str(homes[i].bedrooomCount) + " bedrooms as well as " + str(homes[i].bathroomCount) + " bathrooms.\n Its total price comes to $" + str(homes[i].price) + "!")

