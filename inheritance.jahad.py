# This is Person class
class Person :
    def __init__(self, fName, lName, age ,gender) :
        self.fName = fName
        self.lName = lName
        self.age = age
        self.gender = gender
    def showInfo(self) :
        if self.gender == 'male' :
            return '\nMr.' + self.fName + self.lName + ' is ' +str(self.age) + " year's old" 
        else : 
            return '\nMiss.' + self.fName + self.lName + ' is ' +str(self.age) + " year's old"
# This is teacher class
class Teacher(Person) :
    def __init__(self, fName, lName, age , teacherCode ,gender) :
        super().__init__(fName, lName, age ,gender)
        self.teacherCode = teacherCode
    def showInfo(self) :
        return super().showInfo() + f' and has {self.teacherCode} teaching code\n'
# This is student class
class Student(Person) :
    def __init__(self, fName, lName, age , studentCode ,gender , major) :
        super().__init__(fName, lName, age ,gender)
        self.studentCode = studentCode
        self.major = major
    def showInfo(self) :
        return super().showInfo() + f' and has {self.studentCode} student code ' + f' in {self.major}\n'
# This is Employee class
class Employee(Person) :
    def __init__(self, fName, lName, age ,gender , position , salary):
        super().__init__(fName, lName, age , gender)
        self.position = position
        self.salary = salary
    def showInfo(self) :
        return super().showInfo() + f' and works in {self.position} with {self.salary}$.\n'
# making objects
p1 = Person('sarvin','nami',19,'female')
print(p1.showInfo() )
t1 = Teacher('sarvin','nami',19,1818,'female')
print(t1.showInfo() )
s1 = Student('sarvin','nami',19,1818,'female','ce')
print(s1.showInfo() )
e1 = Employee('sarvin','nami',19,'female','student',19)
print(e1.showInfo() )