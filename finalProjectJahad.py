class Person :
    def __init__(self, name, family, phoneNumber, gender, ID) : 
        while name.isnumeric() or family.isnumeric() :
            name = input('name should be just alphabetics! Please enter again here :')
            family = input('family should be just numbers! Please enter again here :')
        else :
            self.name = name
            self.family = family
        while phoneNumber.isalpha() and len(str(phoneNumber)) != 11 :
            phoneNumber = int(input('Phone numbers should be just numbers! Please enter again here : '))
        else :
            self.phoneNumber = phoneNumber
        self.gender = gender
        while ID.isalpha() and len(str(ID)) != 10 :
            ID = int(input('ID should be just numbers! Please enter again here : '))
        else :
            self.ID = ID
    def showInfo(self) :
        if self.gender == 'male' or self.gender == 'Male' or self.gender == 'm' or self.gender == 'M':
            return '\nMr.' + self.name + self.family + ' has ' +str(self.phoneNumber) + " as their phone number" + f' and {self.ID} is their ID number'
        elif self.gender == 'female' or self.gender == 'Female' or self.gender == 'f' or self.gender == 'F' : 
            return '\nMiss.' + self.name + self.family + ' has ' +str(self.phoneNumber) + " as their phone number" + f' and {self.ID} is their ID number'
class NewAccountCreators(Person) :
    def __init__(self, name, family, phoneNumber, gender, ID, moneyAmount) :
        super().__init__(name, family, phoneNumber, gender, ID)
        self.moneyAmount = moneyAmount
        print(f'Congratulations! Your new account created with {self.moneyAmount}$ successfully! \n')
    def showInfo(self) : return super().showInfo() + f' created a new acoount and has {self.moneyAmount}$ balance.\n'
class Sponsors(Person) :
    def __init__(self,name, family, phoneNumber, gender, ID, loaner, balance, loanAmount) : 
        super().__init__(name, family, phoneNumber, gender, ID)
        self.loaner = loaner 
        self.loanAmount = loanAmount
        while balance < loanAmount : 
            balance = int(input(f'Your balance should be more than {self.loanAmount}'))
        else :
            self.balance = balance
    def showInfo(self) :
       return super().showInfo() + f' is the sponsor of {self.loaner} with the balance of {self.balance}$.\n'
class loaners(Person) : 
    def __init__(self, name, family, phoneNumber, gender, ID, loanAmount, installmentPeriod, balance):
        super().__init__(name, family, phoneNumber, gender, ID)
        self.loanAmount = loanAmount
        self.installmentPeriod = installmentPeriod
        self.balance = balance
        print('You loan {self.loanAmount}$ successfully and have {self.installmentPeriod} months to pay it back.\n')
        s1 = Sponsors(input('Please type ypur name here : '),input('Please type your family here : '),input('Please type your phone number here : '),input('Please type your gender here m or f : '),int(input('Please type your ID number address here : ')),self.name,int(input('Please type your account balance here : ')),self.loanAmount)
        s2 = Sponsors(input('Please type ypur name here : '),input('Please type your family here : '),input('Please type your phone number here : '),input('Please type your gender here m or f : '),int(input('Please type your ID number address here : ')),self.name,int(input('Please type your account balance here : ')),self.loanAmount)
    def loanPayments(self) : 
        if self.balance >= self.loanAmount/self.installmentPeriod :
            self.balance -= self.loanAmount/self.installmentPeriod
            self.payment = self.installmentPeriod - 1
            print('You check your payment successfully!')
        else :
            print('You don\'t have enough money to pay it back!\n')
    def showInfo(self) : 
        return super().showInfo() + f' has got {self.loanAmount}$ loan with {self.installmentPeriod} months installment period which {self.payment} months remains.\n' + 'There are their sponsors:\n' + s1.showInfo() + '\n' + s2.showInfo
