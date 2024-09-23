recipe_steps = [
    "Step 1. Preheat the oven to 350 F",
    "Step 2. Place chicken in oven",
    "Step 3. Bake for 1 ½ hours"
]

#Let's say you forgot to add a step between 2 and 3 where you add seasoning (just for the sake of the example)
recipe_steps.append("Step 3. Add seasonings to the meat")
recipe_steps[2] = "Step 4. Bake for 1 ½ hours"
recipe_steps.sort()

print(recipe_steps)

#just realized you can use the insert() method instead with the index but you get the point

