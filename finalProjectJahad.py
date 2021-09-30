class Person :
    def __init__(self, name, family, phoneNumber, gender, ID) : 
        while name.isnumeric() or family.isnumeric() :
            name = input('name should be just alphabetics! Please enter again here :')
            family = input('family should be just numbers! Please enter again here :')
        else :
            self.name = name
            self.family = family
        while phoneNumber.isalpha() and len(str(phoneNumber)) != 11 :
            phoneNumber = input('Phone numbers should be just numbers! Please enter again here : ')
        else :
            self.phoneNumber = phoneNumber
        while gender != 'm' and gender != 'f' : 
            gender = input('Gender should be either f or m! Please enter again here : ')
        else :
            self.gender = gender
        while ID.isalpha() and len(str(ID)) != 10 :
            ID = input('ID should be just numbers! Please enter again here : ')
        else :
            self.ID = ID
    def showInfo(self) :
        if self.gender == 'male' or self.gender == 'Male' or self.gender == 'm' or self.gender == 'M':
            return '\nMr.' + self.name + ' ' + self.family + ' has ' +str(self.phoneNumber) + " as their phone number" + f' and {self.ID} is their ID number'
        elif self.gender == 'female' or self.gender == 'Female' or self.gender == 'f' or self.gender == 'F' : 
            return '\nMiss.' + ' ' + self.name + self.family + ' has ' +str(self.phoneNumber) + " as their phone number" + f' and {self.ID} is their ID number'
class NewAccountCreators(Person) :
    def __init__(self, name, family, phoneNumber, gender, ID, moneyAmount) :
        super().__init__(name, family, phoneNumber, gender, ID)
        self.moneyAmount = moneyAmount
        print(f'Congratulations! Your new account created with {self.moneyAmount}$ successfully! \n')
    def showInfo(self) : return super().showInfo() + f' has created a new acoount with {self.moneyAmount}$ balance.\n'
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
class Loaners(Person) : 
    def __init__(self, name, family, phoneNumber, gender, ID, loanAmount, installmentPeriod, balance):
        super().__init__(name, family, phoneNumber, gender, ID)
        self.loanAmount = loanAmount
        self.installmentPeriod = installmentPeriod
        self.balance = balance
        self.payment = None
        print(f'You loan {self.loanAmount}$ successfully and have {self.installmentPeriod} months to pay it back.\n')
        s1 = Sponsors(input('Please type your name here : '),input('Please type your family here : '),input('Please type your phone number here : '),input('Please type your gender here m or f : '),input('Please type your ID number here : '),self.name,int(input('Please type your account balance here : ')),self.loanAmount)
        s2 = Sponsors(input('Please type your name here : '),input('Please type your family here : '),input('Please type your phone number here : '),input('Please type your gender here m or f : '),input('Please type your ID number here : '),self.name,int(input('Please type your account balance here : ')),self.loanAmount)
    def loanPayments(self) : 
        if self.balance >= self.loanAmount/self.installmentPeriod :
            self.balance -= self.loanAmount/self.installmentPeriod
            self.payment = self.installmentPeriod - 1
            print('You check your payment successfully!')
        else :
            print('You don\'t have enough money to pay it back!\n')
    def showInfo(self) : 
        return super().showInfo() + f' has got {self.loanAmount}$ loan with {self.installmentPeriod} months installment period which {self.payment} months remains.\n' + 'There are their sponsors:\n' + s1.showInfo() + '\n' + s2.showInfo
class AppInstallers(Person):
    def __init__(self, name, family, phoneNumber, gender, ID, usage) :
        super().__init__(name, family, phoneNumber, gender, ID, usage)
        self.usage = usage
        print(f'Congratulations! You have successfully insalled our app for {self.usage}.\n' + 'You can now install your app now.')
    def showInfo(self):
        return super().showInfo() + f' has bank application for {self.usage}.\n' + 'You can now install your app now.'
p = Person(input('Please enter your name here : '),input('Please enter your family name here : '),input('Please enter your phone number here : '),input('Please enter your gender here m or f : '), input('Please enter your ID number here : '))
def menu():
    print('\n1)Create a new account\n2)show the new account information\n3)loan\n4)show the loan information\n5)install the bank application\n6)show the bank application information\n7)pay loan bill\n8)exit\n')
menu()
choice =input('Please enter your choice here : ')
while choice != 'Exit' or choice !='exit' or choice != '8' :
    if choice == '1' : 
        c = NewAccountCreators(p.name,p.family,p.phoneNumber,p.gender,p.ID,int(input('Please type the amount of money you want to add to you new account here : ')))
        menu()
        choice =input('Please enter your choice here : ')
    if choice == '2' :
        print(c.showInfo())
        menu()
        choice =input('Please enter your choice here : ')
    if choice == '3' :
        l = Loaners(p.name,p.family,p.phoneNumber,p.gender,p.ID,int(input('Please type the amount of money you want to loan here : ')),int(input('Please type the installment Period of the loan here : ')), int(input('Please type your bank account balance here : ')))
        menu()
        choice =input('Please enter your choice here : ')
    if choice  == '4' :
        print(l.showInfo())
        menu()
        choice =input('Please enter your choice here : ')
    if choice == '5' :
        a = AppInstallers(p.name,p.family,p.phoneNumber,p.gender,p.ID,input('Please type the reason you want to instaal our bank application here : '))
        menu()
        choice =input('Please enter your choice here : ')
    if choice == '6' :
        print(a.showInfo())
        menu()
        choice =input('Please enter your choice here : ')
    if choice == '7' : 
        l.loanPayments()
        menu()
        choice =input('Please enter your choice here : ')
else : print(f'\nGoodbye {p.name} {p.family}. Have a nice day! ^-^\n') 