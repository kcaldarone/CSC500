'''
Name: Kori Caldarone
Assignment: Week 6 Critical Thinking
Professor: Professor Schwartz
Date: 9/23/2024
'''

course_number = input("Enter a course number:\n")

course_numbers = ["CSC101", "CSC102", "CSC103", "NET110", "COM241"]
room_numbers = [3004, 4501, 6755, 1244, 1411]
instructors = ["Haynes", "Alvarado", "Rich", "Burke", "Lee"]
meeting_times = ["8:00 am", "9:00 am", "10:00 am", "11:00 am", "1:00 pm"]

def print_dicts():
    room_dict = {}
    instructor_dict = {}
    meeting_dict = {}
    i = 0
    while i < len(course_numbers):
        room_dict[course_numbers[i]] = room_numbers[i]
        instructor_dict[course_numbers[i]] = instructors[i]
        meeting_dict[course_numbers[i]] = meeting_times[i]
        if course_number == course_numbers[i]:
            print("Course Number: " + course_numbers[i])
            print("Room Number: " + str(room_dict[course_number]))
            print("Instructor Name: Professor " + instructor_dict[course_number])
            print("Meeting Time: " + meeting_dict[course_number])
        i = i + 1
        
print_dicts()
