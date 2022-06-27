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
            self.first += i
        for i in tempsecond:
            self.second += i
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
    
    def write_move(self,character):
        if self.head_position < 1 or character not in self.alphabet:
            return self._tape[self.head_position]
        elif character == '1' and self.state == 'q0':
            self._tape[self.head_position] = 'X'
            self.head_position += 1
            self.state = 'q1'
        elif character == '0' and self.state == 'q0':
            self._tape[self.head_position] = '0'
            self.head_position += 1
            self.state = 'q5'
        elif character == '1' and self.state == 'q1':
            self._tape[self.head_position] = '1'
            self.head_position += 1
            self.state = 'q1'
        elif character == '0' and self.state == 'q1':
            self._tape[self.head_position] = '0'
            self.head_position += 1
            self.state = 'q2'  
        elif character == 'B' and self.state == 'q2':
            self._tape[self.head_position] = 'B'
            self.head_position -= 1
            self.state = 'a>b'  
            return 1               
        elif character == 'X' and self.state == 'q2':
            self._tape[self.head_position] = 'X'
            self.head_position += 1
            self.state = 'q2'
        elif character == '1' and self.state == 'q2':
            self._tape[self.head_position] = 'X'
            self.head_position -= 1
            self.state = 'q3'    
        elif character == 'X' and self.state == 'q3':
            self._tape[self.head_position] = 'X'
            self.head_position -= 1
            self.state = 'q3'
        elif character == '0' and self.state == 'q3':
            self._tape[self.head_position] = '0'
            self.head_position -= 1
            self.state = 'q4'   
        elif character == '1' and self.state == 'q4':
            self._tape[self.head_position] = '1'
            self.head_position -= 1
            self.state = 'q4'
        elif character == 'X' and self.state == 'q4':
            self._tape[self.head_position] = 'X'
            self.head_position += 1
            self.state = 'q0'
        elif character == 'X' and self.state == 'q5':
            self._tape[self.head_position] = 'X'
            self.head_position += 1
            self.state = 'q5'
        elif character == '1' and self.state == 'q5':
            self._tape[self.head_position] = '1'
            self.head_position += 1
            self.state = 'a<b'  
            return 0    
        elif character == 'B' and self.state == 'q5':
            self._tape[self.head_position] = 'B'
            self.head_position -= 1
            self.state = 'a=b'
            return 1   
    
        
class substraction:
    def __init__(self, si , f , s):
        self.signal = si
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
    
    def write_move(self,character):
        if self.head_position < 1 or character not in self.alphabet:
            return self._tape[self.head_position]
        elif character == 'B' and self.state == 'q0':
            self._tape[self.head_position] = 'B'
            self.head_position += 1
            self.state = 'q0'
        elif character == '#' and self.state == 'q0':
            self._tape[self.head_position] = '#'
            self.state = 'q9'
            return self._tape
        elif character == '1' and self.state == 'q0':
            self._tape[self.head_position] = '1'
            self.head_position += 1
            self.state = 'q1'
        elif character == '1' and self.state == 'q1':
            self._tape[self.head_position] = '1'
            self.head_position += 1
            self.state = 'q1'
        elif character == '#' and self.state == 'q1':
            self._tape[self.head_position] = '#'
            self.head_position += 1
            self.state = 'q2'
        
    
class addition:
    def __init__(self,si,f,s):
        self.signal = si 
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
        
    def write_move(self,character):
        if self.head_position < 1 or character not in self.alphabet:
            return self._tape[self.head_position]
        elif character == 'B' and self.state == 'q0':
            self._tape[self.head_position] = 'B'
            self.head_position += 1
            self.state = 'q1'
        elif character == '#' and self.state == 'q0':
            self._tape[self.head_position] = '#'
            self.state = 'q5'
            return self._tape
        elif character == '1' and self.state == 'q1':
            self._tape[self.head_position] = '1'
            self.head_position += 1
            self.state = 'q1'
        elif character == '0' and self.state == 'q1':
            self._tape[self.head_position] = '1'
            self.head_position += 1
            self.state = 'q2'
        elif character == '1' and self.state == 'q2':
            self._tape[self.head_position] = '1'
            self.head_position += 1
            self.state = 'q2'
        elif character == '#' and self.state == 'q2':
            self._tape[self.0head_position] = '#'
            self.head_position -= 1
            self.state = 'q3'
        elif character == '1' and self.state == 'q3':
            self._tape[self.head_position] = '#'
            self.head_position -= 1
            self.state = 'q4'
        elif character == '1' and self.state == 'q4':
            self._tape[self.head_position] = '1'
            self.head_position -= 1
            self.state = 'q4'
        elif character == 'B' and self.state == 'q4':
            self._tape[self.head_position] = 'B'
            self.state = 'q5'
            return self._tape
        
        

firstNumber = int(input("enter firstNumber: "))
secondNumber = int(input("enter secondNumber: "))
comp = Comparator(firstNumber,secondNumber)
sub = substraction(comp.compare(),comp.first,comp.second)
add = addition(comp.compare(),comp.first,comp.second)
if comp.compare() == 1:
    print(sub.substract())
else:
    print(add.add())