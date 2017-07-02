class Student:
    name = "Some Name"

    def praise(self):
        if self.name == "Jacinta":
            return "You're doing a great job, Jacinta!"
        elif self.name == "Michael":
            return "I really like your hair today, Michael!"
            # student = Student()
            # self.name = "Jacinta"


# from first_class import Student
student = Student()
student.name = "Jacinta"
print(student.praise())
