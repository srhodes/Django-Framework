class Student:

        def __init__(self, name, marks):
            self.name = name
            self.marks = marks

        def get_number_of_marks(self):
            return len(self.marks)

student = Student("Ranga", [23, 45, 56, 75])
#number = Student.get_number_of_marks()
#print(f"Student[number_of_marks-{number}")
