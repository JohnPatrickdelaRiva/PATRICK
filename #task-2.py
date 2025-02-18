class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old and I am studying {self.course}.")

student1 = Student("JV", 25, "CRIMINOLOGY")
student2 = Student("RONNEL", 31, "INFORMATION TECHNOLOGY")
student3 = Student("KENT", 29, "NURSING")

student1.introduce()
student2.introduce()
student3.introduce()