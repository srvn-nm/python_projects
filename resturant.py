class Person :
    def __init__(self, name, family, phoneNumber, gender) : 
        self.name = name
        self.family = family
        self.phoneNumber = phoneNumber
        self.gender = gender
    def showInfo(self) :
        if self.gender == 'male' or self.gender == 'Male' or self.gender == 'm' or self.gender == 'M':
            return '\nMr.' + self.name + self.family + ' has ' +str(self.phoneNumber) + " as their phone number."
        elif self.gender == 'female' or self.gender == 'Female' or self.gender == 'f' or self.gender == 'F' : 
            return '\nMiss.' + self.name + self.family + ' has ' +str(self.phoneNumber) + " as their phone number."
class Costumer(Person) : 
    def __init__(self, name, family, phoneNumber, gender, typeOfOrder) : 
        super().__init__(name, family, phoneNumber, gender)
        self.typeOfOrder = typeOfOrder
        self.order = input('Please type your order here : ')
    def showInfo(self) : 
        return super().showInfo() + f' ordered {self.order} in {self.typeOfOrder} way!\n'
class Supplier(Person) : 
    def __init__ (self, name, family, phoneNumber, gender, company, factorNumber, productNumbers) : 
        super().__init__(name, family, phoneNumber, gender)
        self.company = company
        self.factorNumber = factorNumber
        self.productNumbers = productNumbers
        self.products = []
        for i in range(int(self.productNumbers)):
            self.products.append(input(f'please enter new product number {i + 1} here : '))
    def showInfo(self) : 
        return super().showInfo() + f' provide {self.products} from company {self.company} with factor number {self.factorNumber}.\n'
class Owner(Person) : 
    def __init__(self, name, family, phoneNumber, gender, brachName, rent) : 
        super().__init__(name, family, phoneNumber, gender)
        self.brachName = brachName
        self.rent = rent
    def showInfo(self) : 
        return super().showInfo() + f' is the owner of {self.brachName} which we give them {self.rent} as our rent monthly.\n'
class Branch :
    def __init__(self):
        self.supplier = Supplier(input('Supplier name '),input('Supplier family '),input('Supplier phone number '),input('Supplier gender '),input('Supplier company '),input('Supplier factor number '),input('Supplier product number '))
        print ('\n')
        self.costumer = Costumer(input('Costumer name '),input('Costumer family '),input('Costumer phone number '),input('Costumer gender '),input('Costumer type of order '))
        print ('\n')
        self.costumer = Owner(input('Owner name '),input('Owner family '),input('Owner phone number '),input('Owner gender '),input('Owner name of branch '),input('Owner rate of rent '))
branch1 = Branch()
branch1.costumer.showInfo()
branch1.supplier.showInfo()
branch1.owner.showInfo()