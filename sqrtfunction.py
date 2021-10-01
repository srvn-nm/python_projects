def sqrtfunction(num):
    guess = round(num / (num-1) , 10)
    i = 0
    while i <= 20000 :
        guessNum = round(num / guess , 10)
        newGuess = round((guess + guessNum) / 2 , 10)
        i += 1
        if newGuess == guess :
            break
        else :
            guess = newGuess
    return guess
print(sqrtfunction(int(input('Please enter ther number you want to se it\'s square here : '))))