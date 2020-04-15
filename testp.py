class Student():
    '''This is a doc string info'''

    def __init__(self,eno,ename):
        self.eno = eno
        self.ename = ename

    def stud_info(self):
        print("Employee Name:", self.ename)

s = Student(100, "Madan")
s.stud_info()

print(Student.__doc__)
