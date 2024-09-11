#For Loop Example - Names
names = ["Adam","Bailey","Caspian","Daelynn","Echo","Florance"]
for name in names:
    print(name)

#While Loop Example - Counting 1 to 10
count = 0
while count < 10:
    count = count + 1
    print(count)


#While Loop Example #2 - Clear Exit Condition
while True: #making an infinite loop
    userInput = input("Type 'STOP' to stop the loop")
    userInput = userInput.upper
    if userInput == 'STOP':
        break

import itertools
arr = [1,2,3,4,5]
for i in itertools.cycle(arr):
    print(i)