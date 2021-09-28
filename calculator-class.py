class SimpleCalculator :
    def __init__(self, firstNumber, secondNumber) :
        while  firstNumber.isalpha() or secondNumber.isalpha(): 
            firstNumber = input('enter the first number : ')
            secondNumber = input('enter the second number : ')
        else :
            self.firstNumber = int(firstNumber)
            self.secondNumber = int(secondNumber)
            self.display()

    def addition(self) : return self.firstNumber + self.secondNumber

    def submission(self) : 
        return self.firstNumber - self.secondNumber

    def division(self) : 
        if self.secondNumber != 0 :
            return self.firstNumber / self.secondNumber
        elif self.firstNumber != 0 :
            return self.secondNumber / self.firstNumber
        else : 
            print( "division failed" )

    def multiplication(self) :
        return self.secondNumber * self.firstNumber
        
    def display(self) :
        print(f'\nthere is the result of our calculations :\naddition : {self.addition()}\nsubmission : {self.submission()}\ndivision : {self.division()}\nmultiplication : {self.multiplication()}\nthank you for cooperation  ^-^\n')
c1 = SimpleCalculator(input('enter first number : '),input('enter second number : '))