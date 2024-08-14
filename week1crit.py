#Getting the numbers from the user
#checking if num1 is a number
num1 = int(input("What would you like your first number to be?\n"))
num2 = int(input("What would you like your second number to be?\n"))
mathFunct = input("What would you like to do with these two numbers out of the four options?\n - Add\n - Subtract\n - Multiply\n - Divide\n").lower()
print(mathFunct)

if mathFunct == "add": #Addition
    sum = num1 + num2
    print(str(num1) + " added to " + str(num2) + " equals " + str(sum))
elif mathFunct == "subtract": #Subtraction
    diff = num1 - num2
    print(str(num1) + " subtracted by " + str(num2) + " equals " + str(diff))
elif mathFunct == "multiply": #Multiplication
    mult = num1 * num2
    print(str(num1) + " multiplied by " + num2 + " equals " + mult)  
elif mathFunct == "divide": #Division
    div = num1/num2
    print(str(num1) + " divided by " + str(num2) + " equals " + str(div))     
else:
    print("What you put in was not an option. Please try again.")