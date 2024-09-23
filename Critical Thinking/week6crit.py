
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
            print("Room Number: " + str(room_numbers[i]))
            print("Instructor Name: Professor " + instructors[i])
            print("Meeting Time: " + meeting_times[i])
        i = i + 1
        
print_dicts()
'''
course_number = input("Enter a course number:\n")

room_dict = {"CSC101": 3004, "CSC102": 4501, "CSC103": 6755, "NET110": 1244, "COM241": 1411}
instructor_dict = {"CSC101": "Haynes", "CSC102": "Alvarado", "CSC103": "Rich", "NET110": "Burke", "COM241": "Lee"}
meeting_dict = {"CSC101": "8:00 am", "CSC102": "9:00 am", "CSC103": "Rich", "NET110": "Burke", "COM241": "Lee"}

for i, j in room_dict:
    if i == course_number:
        print("Course Number: " + i)
        print("Room Number: " + str(j))
        #print instructor
        #print meeting time

'''