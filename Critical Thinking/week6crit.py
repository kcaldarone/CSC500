'''
Name: Kori Caldarone
Assignment: Week 6 Critical Thinking
Professor: Professor Schwartz
Date: 9/23/2024
'''
#getting user input
course_number = input("Enter a course number:\n")

#making arrays to make dictionaries
course_numbers = ["CSC101", "CSC102", "CSC103", "NET110", "COM241"]
room_numbers = [3004, 4501, 6755, 1244, 1411]
instructors = ["Haynes", "Alvarado", "Rich", "Burke", "Lee"]
meeting_times = ["8:00 am", "9:00 am", "10:00 am", "11:00 am", "1:00 pm"]

def print_dicts():
    #making blank dictionaries to add to
    room_dict = {}
    instructor_dict = {}
    meeting_dict = {}
    i = 0       #making count variable
    matchFound = False   #making matchFound bool to make sure there is a match in course names
    while i < len(course_numbers):
        room_dict[course_numbers[i]] = room_numbers[i]
        instructor_dict[course_numbers[i]] = instructors[i]
        meeting_dict[course_numbers[i]] = meeting_times[i]
        if course_number == course_numbers[i]:   #checking if the course number submitted from the user is the same one we are on
            print("Course Number: " + course_numbers[i])
            print("Room Number: " + str(room_dict[course_number]))
            print("Instructor Name: Professor " + instructor_dict[course_number])
            print("Meeting Time: " + meeting_dict[course_number])
            matchFound = True
        i = i + 1
    if matchFound == False:   #checking matchFound bool to make sure there is at least one match
        print("Course number " + course_number + " not found in our database, please try again.")   
        
print_dicts()

