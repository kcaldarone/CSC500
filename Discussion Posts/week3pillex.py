#IRL Example 1 - Pill Tracker
meds = ['Adderall XR', 'Lexapro', 'Aripiprazole', 'Haloperidol']
dosage = [30,10,2,5]
pillAmt = [1,3,1,1]
count, pillCount, dosageCount = 0

while count < 4:
    if pillAmt[count] == 1:
        print("You have taken " + str(pillAmt[count]) + " " + str(dosage[count]) + "mg pill of " + meds[count] + ". \n")
    else:
        print("You have taken " + str(pillAmt[count]) + " " + str(dosage[count]) + "mg pills of " + meds[count] + ". \n")
    #adding to all counts
    dosageCount = dosageCount + dosage[count]
    pillCount = pillCount + pillAmt[count]
    count = count + 1
    print("You have taken a total of " + str(pillCount) + " pills, totaling " + str(dosageCount) + "mg of medications. \n")

