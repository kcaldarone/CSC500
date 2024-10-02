#Week 8

#Class
class Character:
    def __init__ (self, firstName, middleName, lastName, age, genderIdentity, role):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.age = age
        self.genderIdentity = genderIdentity
        self.role = role
    def print_char(self):
        print(self.firstName + " " + self.middleName + " " + self.lastName + " is a " + str(self.age) + " year old " + self.genderIdentity + " with the role of " + self.role + ".")

#Instance of Class
skarlett = Character("Skarlett", "Amethyst", "Amansolis", 19, "Female", "Main Protagonist")

#Calling Method from Class
print(skarlett.print_char())


