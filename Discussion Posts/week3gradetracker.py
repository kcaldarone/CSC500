#IRL Example 2 - Grade Tracker
maxScore = [100,30,30,100]
results = [100,30,30,98]
grades = []
count = 0
while count < len(maxScore):
    grades[count] = results[count]/maxScore[count]
    gradeTotal = gradeTotal + grades[count]
    count = count + 1
print("Your current grade in the class is " + gradeTotal / len(grades) + "%.")




