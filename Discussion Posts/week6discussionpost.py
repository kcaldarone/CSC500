#Week 6 Discussion Post - Lists and Dictionaries

#Lists - Insert
names = []
names.insert(0,"Caleb") # ["Caleb"]

#Lists - Insert (Alternate Method (Append))
names.append("Melissa") # ["Caleb", "Melissa"]

#Lists - Insert (Alternate Method (Extend))
moreNames = ["Kayla", "James", "Corey"] 
names.extend(moreNames) # ["Caleb", "Melissa", "Kayla", "James", "Corey"]

#Lists - Update
names[0] = "Kaleb" # ["Kaleb", "Melissa", "Kayla", "James", "Corey"]

#Lists - Remove
names.remove("Corey") # ["Kaleb", "Melissa", "Kayla", "James"]

#Lists - Remove (Alternate Method (Popping))
names.pop(0) # ["Melissa", "Kayla", "James"]

#Lists - Remove (Alternate Method (Clearing))
names.clear() # []

#Making dictionary
grades = {'Aaliyah': 87, 'Jennifer': 99, 'Robert': 82, 'Jeremy': 85, 'Hannah': 67}

#Dictionaries - Insert  
grades["Jasmine"] = 100 # {'Aaliyah': 87, 'Jennifer': 99, 'Robert': 78, 'Jeremy': 85, 'Hannah': 67, 'Jasmine': 100}

#Dictionaries - Update
grades["Aaliyah"] = 90 # {'Aaliyah': 90, 'Jennifer': 99, 'Robert': 78, 'Jeremy': 85, 'Hannah': 67, 'Jasmine': 100}
grades["Jennifer"] = 95 # {'Aaliyah': 90, 'Jennifer': 95, 'Robert': 78, 'Jeremy': 85, 'Hannah': 67, 'Jasmine': 100}
grades["Robert"] = 73 # {'Aaliyah': 90, 'Jennifer': 95, 'Robert': 73, 'Jeremy': 85, 'Hannah': 67, 'Jasmine': 100}
grades["Jeremy"] = 88 # {'Aaliyah': 90, 'Jennifer': 95, 'Robert': 73, 'Jeremy': 88, 'Hannah': 67, 'Jasmine': 100}
grades["Hannah"] = 71 # {'Aaliyah': 90, 'Jennifer': 95, 'Robert': 73, 'Jeremy': 88, 'Hannah': 71, 'Jasmine': 100}
grades["Jasmine"] = 97 # {'Aaliyah': 90, 'Jennifer': 95, 'Robert': 73, 'Jeremy': 88, 'Hannah': 71, 'Jasmine': 97}

#Dictionaries - Remove
del grades["Robert"] # {'Aaliyah': 90, 'Jennifer': 95, 'Jeremy': 88, 'Hannah': 71, 'Jasmine': 97}

#Dictionaries - Remove (Alternate Method (popping))
grades.pop('Hannah') # {'Aaliyah': 90, 'Jennifer': 95, 'Jeremy': 88, 'Jasmine': 97}

#Dictionaries - Remove (Alternate Method (clearing))
grades.clear() # {}