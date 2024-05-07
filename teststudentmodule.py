class Student:    
    def __init__(self, name, student_number):
        self.name = name
        self.student_number = student_number
        self.modules_list = []
    
    def print_student_info(self):
        print("Student name: %s" %self.name)
        print("Student ID: %s" %self.student_number)
        print("module/s undertaken by the studen:" )
        i = 0
        for c in self.modules_list:
                i+=1
                print("%d %s" %(i,c.print_module_info()))
        
    def enrol(self, module_running):
        self.modules_list.append(module_running)



class Module:  
    def __init__(self, module_title, module_credits, department):
        self.module_title = module_title
        self.credits = module_credits
        self.department = department
    
    def print_module_info(self):
        return "Module: %s, Credits: %s, Department: %s" %(self.module_title, self.credits, self.department)
    
student1 = Student("Gurdit", "2318573")
student2 = Student("Ashish", "9876672")

module1 = Module("Medical", "80", "Secince")
module2 = Module("Computer", "90", "Technology")
module3 = Module("Finance", "70", "Economic")

student1.enrol(module1)
student2.enrol(module2)
student1.enrol(module3)

print(student1.print_student_info())
print(student2.print_student_info())



