class Comparator:
    def __init__(self,f,s):
        tempfirst = []
        tempsecond = []
        for i in range(f):
            tempfirst.append(1)
        for i in range(s):
            tempsecond.append(1)
        self.first=''
        self.second=''
        for i in tempfirst:
            self.first += str(i)
        for i in tempsecond:
            self.second += str(i)
        self.alphabet = "10B#" 
        self.head_position = 0
        self.__init_tape()
        self.state = 'q0'
        self.sub = substraction(self.first,self.second)
        self.add = addition(self.first,self.second)
    
    def __init_tape(self):
        tape = "B"
        for a in (c for c in self.first if c in self.alphabet):
            tape += a
        tape += "0"
        for a in (c for c in self.second if c in self.alphabet):
            tape += a
        tape += "#"
        self._tape = list(tape)
    
    def write_move(self):
        while True:
            if self.head_position < 0 or self._tape[self.head_position] not in self.alphabet:
                return self._tape[self.head_position]
            if self.head_position == 0 and self._tape[self.head_position] == 'B':
                self.head_position += 1
            elif self._tape[self.head_position] == '1' and self.state == 'q0':
                self._tape[self.head_position] = 'X'
                self.head_position += 1
                self.state = 'q1'
            elif self._tape[self.head_position] == '0' and self.state == 'q0':
                self._tape[self.head_position] = '0'
                self.head_position += 1
                self.state = 'q5'
            elif self._tape[self.head_position] == '1' and self.state == 'q1':
                self._tape[self.head_position] = '1'
                self.head_position += 1
                self.state = 'q1'
            elif self._tape[self.head_position] == '0' and self.state == 'q1':
                self._tape[self.head_position] = '0'
                self.head_position += 1
                self.state = 'q2'  
            elif self._tape[self.head_position] == 'B' and self.state == 'q2':
                self._tape[self.head_position] = 'B'
                self.head_position -= 1
                self.state = 'a>b'  
                return self.sub.write_move()               
            elif self._tape[self.head_position] == 'X' and self.state == 'q2':
                self._tape[self.head_position] = 'X'
                self.head_position += 1
                self.state = 'q2'
            elif self._tape[self.head_position] == '1' and self.state == 'q2':
                self._tape[self.head_position] = 'X'
                self.head_position -= 1
                self.state = 'q3'    
            elif self._tape[self.head_position] == 'X' and self.state == 'q3':
                self._tape[self.head_position] = 'X'
                self.head_position -= 1
                self.state = 'q3'
            elif self._tape[self.head_position] == '0' and self.state == 'q3':
                self._tape[self.head_position] = '0'
                self.head_position -= 1
                self.state = 'q4'   
            elif self._tape[self.head_position] == '1' and self.state == 'q4':
                self._tape[self.head_position] = '1'
                self.head_position -= 1
                self.state = 'q4'
            elif self._tape[self.head_position] == 'X' and self.state == 'q4':
                self._tape[self.head_position] = 'X'
                self.head_position += 1
                self.state = 'q0'
            elif self._tape[self.head_position] == 'X' and self.state == 'q5':
                self._tape[self.head_position] = 'X'
                self.head_position += 1
                self.state = 'q5'
            elif self._tape[self.head_position] == '1' and self.state == 'q5':
                self._tape[self.head_position] = '1'
                self.head_position += 1
                self.state = 'a<b'  
                return self.add.write_move()    
            elif self._tape[self.head_position] == 'B' and self.state == 'q5':
                self._tape[self.head_position] = 'B'
                self.head_position -= 1
                self.state = 'a=b'
                return self.sub.write_move()   
    
        
class substraction:
    def __init__(self , f , s):
        self.first = f
        self.second = s
        self.alphabet = "10B#" 
        self.head_position = 0
        self.__init_tape()
        self.state = 'q0'
    
    def __init_tape(self):
        tape = "B"
        for a in (c for c in self.first if c in self.alphabet):
            tape += a
        tape += "#"
        for a in (c for c in self.second if c in self.alphabet):
            tape += a
        tape += "#"
        self._tape = list(tape)
    
    def write_move(self):
        while True:
            if self.head_position < 0 or self._tape[self.head_position] not in self.alphabet:
                return self._tape[self.head_position]
            if self.head_position == 0 and self._tape[self.head_position] == 'B':
                self.head_position += 1
            elif self._tape[self.head_position] == 'B' and self.state == 'q0':
                self._tape[self.head_position] = 'B'
                self.head_position += 1
                self.state = 'q0'
            elif self._tape[self.head_position] == '#' and self.state == 'q0':
                self._tape[self.head_position] = '#'
                self.state = 'q9'
                return self._tape
            elif self._tape[self.head_position] == '1' and self.state == 'q0':
                self._tape[self.head_position] = '1'
                self.head_position += 1
                self.state = 'q1'
            elif self._tape[self.head_position] == '1' and self.state == 'q1':
                self._tape[self.head_position] = '1'
                self.head_position += 1
                self.state = 'q1'
            elif self._tape[self.head_position] == '#' and self.state == 'q1':
                self._tape[self.head_position] = '#'
                self.head_position += 1
                self.state = 'q2'
            elif self._tape[self.head_position] == '#' and self.state == 'q2':
                self._tape[self.head_position] = '#'
                self.head_position += 1
                self.state = 'q2'
            elif self._tape[self.head_position] == '1' and self.state == 'q2':
                self._tape[self.head_position] = '1'
                self.head_position += 1
                self.state = 'q3'
            elif self._tape[self.head_position] == '1' and self.state == 'q3':
                self._tape[self.head_position] = '1'
                self.head_position -= 1
                self.state = 'q4'
            elif self._tape[self.head_position] == '#' and self.state == 'q3':
                self._tape[self.head_position] = '#'
                self.head_position -= 1
                self.state = 'q6'
            elif self._tape[self.head_position] == '1' and self.state == 'q4':
                self._tape[self.head_position] = '#'
                self.head_position -= 1
                self.state = 'q5'
            elif self._tape[self.head_position] == '#' and self.state == 'q5':
                self._tape[self.head_position] = '#'
                self.head_position -= 1
                self.state = 'q5'
            elif self._tape[self.head_position] == '1' and self.state == 'q5':
                self._tape[self.head_position] = '#'
                self.head_position += 1
                self.state = 'q2' 
            elif self._tape[self.head_position] == 'B' and self.state == 'q5':
                self._tape[self.head_position] = 'B'
                self.head_position += 1
                self.state = 'q2' 
            elif self._tape[self.head_position] == '1' and self.state == 'q6':
                self._tape[self.head_position] = '#'
                self.head_position -= 1
                self.state = 'q7'
            elif self._tape[self.head_position] == '#' and self.state == 'q7':
                self._tape[self.head_position] = '#'
                self.head_position -= 1
                self.state = 'q7' 
            elif self._tape[self.head_position] == 'B' and self.state == 'q7':
                self._tape[self.head_position] = 'B'
                self.state = 'q9'
                return self._tape
            elif self._tape[self.head_position] == '1' and self.state == 'q7':
                self._tape[self.head_position] = '#'
                self.head_position -= 1
                self.state = 'q8'
            elif self._tape[self.head_position] == '1' and self.state == 'q8':
                self._tape[self.head_position] = '1'
                self.head_position -= 1
                self.state = 'q8'
            elif self._tape[self.head_position] == 'B' and self.state == 'q8':
                self._tape[self.head_position] = 'B'
                self.state = 'q9'
                return self._tape
    
class addition:
    def __init__(self,f,s): 
        self.first = f
        self.second = s
        self.alphabet = "10B#" 
        self.head_position = 0
        self.__init_tape()
        self.state = 'q0'
    
    def __init_tape(self):
        tape = "B"
        for a in (c for c in self.first if c in self.alphabet):
            tape += a
        tape += "0"
        for a in (c for c in self.second if c in self.alphabet):
            tape += a
        tape += "#"
        self._tape = list(tape)
        
    def write_move(self):
        while True:
            if self.head_position < 0 or self._tape[self.head_position] not in self.alphabet:
                return self._tape[self.head_position]
            if self.head_position == 0 and self._tape[self.head_position] == 'B':
                self.head_position += 1
            elif self._tape[self.head_position] == 'B' and self.state == 'q0':
                self._tape[self.head_position] = 'B'
                self.head_position += 1
                self.state = 'q1'
            elif self._tape[self.head_position] == '#' and self.state == 'q0':
                self._tape[self.head_position] = '#'
                self.state = 'q5'
                return self._tape
            elif self._tape[self.head_position] == '1' and self.state == 'q1':
                self._tape[self.head_position] = '1'
                self.head_position += 1
                self.state = 'q1'
            elif self._tape[self.head_position] == '0' and self.state == 'q1':
                self._tape[self.head_position] = '1'
                self.head_position += 1
                self.state = 'q2'
            elif self._tape[self.head_position] == '1' and self.state == 'q2':
                self._tape[self.head_position] = '1'
                self.head_position += 1
                self.state = 'q2'
            elif self._tape[self.head_position] == '#' and self.state == 'q2':
                self._tape[self.head_position] = '#'
                self.head_position -= 1
                self.state = 'q3'
            elif self._tape[self.head_position] == '1' and self.state == 'q3':
                self._tape[self.head_position] = '#'
                self.head_position -= 1
                self.state = 'q4'
            elif self._tape[self.head_position] == '1' and self.state == 'q4':
                self._tape[self.head_position] = '1'
                self.head_position -= 1
                self.state = 'q4'
            elif self._tape[self.head_position] == 'B' and self.state == 'q4':
                self._tape[self.head_position] = 'B'
                self.state = 'q5'
                return self._tape
        
        
firstNumber = int(input("enter firstNumber: "))
secondNumber = int(input("enter secondNumber: "))
comp = Comparator(firstNumber,secondNumber)
print(comp.write_move())