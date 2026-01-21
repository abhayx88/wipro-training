# Define the Student class
class Student:
    # Constructor to initialize attributes
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Method to display student details
    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("-------------------------")


# Create objects of the Student class
student1 = Student("Abhay Gupta", 101)
student2 = Student("Rahul Sharma", 102)

# Display details of students
student1.display_details()
student2.display_details()
