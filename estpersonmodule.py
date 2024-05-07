class Person:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def get_profile_info(self):
        return "Name: %s, Phone number: %s" %(self.name, self.phone_number)


class Student(Person):

    def __init__(self, course, *args, **kwargs):
        self.course = course
        self.classes = []
        super().__init__(*args, **kwargs)

    def enrol(self, module):
        self.classes.append(module)


class StaffMember(Person):

    def __init__(self, *args, **kwargs ):
        self.courses = []
        super().__init__(*args, **kwargs)

    def administrator_for(self, module):
        self.courses.append(module)

    def get_salary(self):
        return self.salary

class Lecturer(Person):
    def __init__(self, name, phone_number,academic_title,salary):
        super().__init__(name, phone_number)
        self.academictitle = academic_title
        self.lecturer_salary = salary
    
    def get_details(self):
        return super().get_profile_info() + f", {self.academictitle},{self.lecturer_salary}"

obj1 = Lecturer("Gurdit Singh", "077783333", "professor", 90000)
print(obj1.get_details())

obj2 = Lecturer("Ashish kaur", "237293274", "lector", 80000)
print(obj2.get_details())

obj2 = Lecturer("test", "131313", "Dr", 9990000)
print(obj2.get_details())

