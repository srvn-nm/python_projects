class Person :
   def _init_(self, name, lastname, addres, phoneNumber, email) :
        self.name = name
        self.lastname = lastname
        self.addres = addres
        self.phone = phoneNumber
        self.email = email
   def print_personal_information(self) :   
      print("----------------------------------")
      print("Personal information : ")
      print(f"Name : {self.name}")
      print(f"Lastname : {self.lastname}")
      print(f"Addres : {self.addres}")
      print(f"Phone : {self.phone}")
      print(f"Email : {self.email}")
class Personnel(Person) : 
    def __init__ (self, name, lastname, addres, phoneNumber, email, education, workingHours, position, salary, vacations) : 
        super().__init__(name, lastname, addres, phoneNumber, email)
        self.education = education
        self.workingHours = workingHours
        self.position = position
        self.salary = salary
        self.vacations  = vacations
        self.workingHours += int(input('Please enter your extra working hours here. If it is none just enter 0 : '))
        Resturant.personnel.append(self)
    def print_personal_information(self) : 
        super().print_PersonalInformation()
        print(f'Education : {self.education}')
        print(f'Working hours : {self.workingHours}')
        print(f'Position : {self.position}')
        print(f'Salary : {self.salary}$')
        print(f'Vacations : {self.vacations}')
        print("----------------------------------")
class Delivery(Personnel) :
    def __init__ (self, name, lastname, addres, phoneNumber, email, education, workingHours, position, salary, vacation, orderStatus = 'at the beginning') :
        Personnel().__init__(self, name, lastname, addres, phoneNumber, email, education, workingHours, position, salary, vacation)
        self.orderStatus = orderStatus
        Resturant.personnel.append(self)
    def updateStatus(self, newStatus) :
        self.orderStatus = newStatus
    def print_personal_information(self) : 
        Person().print_personal_information()
        print(f'Education : {self.education}')
        print(f'Working hours : {self.workingHours}')
        print(f'Position : {self.position}')
        print(f'Salary : {self.salary}$')
        print(f'Vacations : {self.vacations}')
        while self.orderStatus != 'at the destination' : 
            print(f'Order Status : {self.orderStatus}')
            self.updateStatus(input('Please enter the order status here : '))
        print("----------------------------------")
class Resturant : 
    def __init__ (self, name) : 
        self.name = name
        self.personnel = []
        self.costumer = []
        self.supplier = []
        self.branch = []
    def showInfo(self) : 
        print("----------------------------------")
        print(f'Resturant name : {self.name}')
        print(f'Resturant personnel : {self.personnel}')
        print(f'Resturant costumer : {self.costumer}')
        print(f'Resturant supplier : {self.supplier}')
        print("----------------------------------")
class Branch(Resturant) :
    def __init__ (self, name, rent, sale, supplimentaryCost) :
        super().__init__(name)
        self.rent = rent
        # we should add costumer's factors to this sale to update it.
        self.sale = sale
        self.score = sale / (supplimentaryCost + rent + sale) *100
        Resturant.branch.append(self)
        Resturant.branch.sort()
        self.rank = Resturant.branch.index(self) + 1
    def showInfo(self) : 
        print("----------------------------------")
        print(f'Branch name : {self.name}')
        print(f'Branch personnel : {self.personnel}')
        print(f'Branch costumer : {self.costumer}')
        print(f'Branch supplier : {self.supplier}')
        print(f'Branch rent : {self.rent}$')
        print(f'Branch sale : {self.sale}$')
        print(f'Branch score : {self.score}')
        print(f'Branch rank : {self.rank}')
        print("----------------------------------")